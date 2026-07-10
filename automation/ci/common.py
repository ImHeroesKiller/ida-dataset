"""Shared CI helpers: env loading, logging, reports, dry-run, timing."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

# Ensure repo root on path
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from automation.ci import (  # noqa: E402
    EXIT_CONFIG_ERROR,
    EXIT_SUCCESS,
)
from automation.lib.simple_yaml import load_simple_yaml  # noqa: E402


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def find_repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "VERSION").exists() and (candidate / "domains").exists():
            return candidate
        if (candidate / ".git").exists() and (candidate / "domains").exists():
            return candidate
    return _REPO_ROOT


@dataclass
class RunContext:
    """CI run context shared by all workflows."""

    name: str
    repo_root: Path
    environment: str
    dry_run: bool
    started_at: str = field(default_factory=utc_now_iso)
    finished_at: Optional[str] = None
    duration_seconds: float = 0.0
    status: str = "running"
    exit_code: int = EXIT_SUCCESS
    env_config: dict[str, Any] = field(default_factory=dict)
    messages: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)
    artifacts: list[str] = field(default_factory=list)

    def finish(self, exit_code: int, status: Optional[str] = None) -> int:
        self.exit_code = exit_code
        self.finished_at = utc_now_iso()
        started = datetime.fromisoformat(self.started_at.replace("Z", "+00:00"))
        finished = datetime.fromisoformat(self.finished_at.replace("Z", "+00:00"))
        self.duration_seconds = max(0.0, (finished - started).total_seconds())
        if status:
            self.status = status
        elif exit_code == EXIT_SUCCESS:
            self.status = "success"
        else:
            self.status = "failed"
        return exit_code

    def to_log_dict(self) -> dict[str, Any]:
        return {
            "workflow": self.name,
            "environment": self.environment,
            "dry_run": self.dry_run,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "duration_seconds": self.duration_seconds,
            "status": self.status,
            "exit_code": self.exit_code,
            "messages": self.messages,
            "errors": self.errors,
            "warnings": self.warnings,
            "metrics": self.metrics,
            "artifacts": self.artifacts,
        }


def load_yaml_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(str(path))
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
    except ImportError:
        data = load_simple_yaml(text)
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError(f"YAML root must be a mapping: {path}")
    return data


def load_environment_config(
    repo_root: Path,
    environment: str,
) -> dict[str, Any]:
    """Load config/environments/{environment}.yaml — never hardcode env rules."""
    path = repo_root / "config" / "environments" / f"{environment}.yaml"
    if not path.exists():
        raise FileNotFoundError(
            f"Environment config not found: {path}. "
            f"Expected one of: development, staging, production"
        )
    data = load_yaml_file(path)
    data["_path"] = str(path)
    data["_environment"] = environment
    return data


def resolve_environment(cli_value: Optional[str] = None) -> str:
    env = (
        cli_value
        or os.environ.get("IDA_ENVIRONMENT")
        or os.environ.get("ENVIRONMENT")
        or "development"
    )
    env = env.strip().lower()
    if env not in {"development", "staging", "production"}:
        raise ValueError(
            f"Invalid environment '{env}'. Allowed: development, staging, production"
        )
    return env


def parse_bool(value: Any, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def add_common_args(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument(
        "--environment",
        "-e",
        default=None,
        help="Target environment: development | staging | production "
        "(or IDA_ENVIRONMENT). Default: development",
    )
    parser.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        default=None,
        help="Dry run: no writes, no commits, no pushes",
    )
    parser.add_argument(
        "--no-dry-run",
        dest="no_dry_run",
        action="store_true",
        help="Disable dry-run mode",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Repository root (auto-detected by default)",
    )
    return parser


def resolve_dry_run(
    args: argparse.Namespace,
    env_config: Mapping[str, Any],
    *,
    default: bool = True,
) -> bool:
    if getattr(args, "no_dry_run", False):
        return False
    if getattr(args, "dry_run", None) is True:
        return True
    # env var
    if "DRY_RUN" in os.environ:
        return parse_bool(os.environ.get("DRY_RUN"))
    # environment config
    if "dry_run" in env_config:
        return parse_bool(env_config.get("dry_run"), default=default)
    return default


def write_json_log(path: Path, ctx: RunContext, extra: Optional[Mapping[str, Any]] = None) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = ctx.to_log_dict()
    if extra:
        payload["extra"] = dict(extra)
    if ctx.dry_run:
        # still write reports in CI for visibility, but mark dry_run
        pass
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    ctx.artifacts.append(str(path))
    return path


def write_markdown_report(path: Path, content: str, ctx: RunContext) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = content.replace("\r\n", "\n").replace("\r", "\n")
    if not text.endswith("\n"):
        text += "\n"
    if ctx.dry_run:
        # Dry-run still emits reports (read-only artifacts) unless env forbids
        forbid = parse_bool(
            ctx.env_config.get("dry_run_skip_reports", False), default=False
        )
        if forbid:
            ctx.messages.append(f"dry_run: skipped report write {path}")
            return path
    path.write_text(text, encoding="utf-8", newline="\n")
    ctx.artifacts.append(str(path))
    return path


def report_header(ctx: RunContext, title: str) -> list[str]:
    return [
        f"# {title}",
        "",
        f"- **Workflow:** `{ctx.name}`",
        f"- **Environment:** `{ctx.environment}`",
        f"- **Dry run:** `{ctx.dry_run}`",
        f"- **Started:** {ctx.started_at}",
        f"- **Finished:** {ctx.finished_at or '—'}",
        f"- **Duration (s):** {ctx.duration_seconds}",
        f"- **Status:** `{ctx.status}`",
        f"- **Exit code:** `{ctx.exit_code}`",
        "",
    ]


def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def timed(fn):
    """Simple decorator alternative — returns (result, duration)."""

    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        return result, time.perf_counter() - t0

    return wrapper


def fail_config(ctx: RunContext, message: str) -> int:
    ctx.errors.append(message)
    return ctx.finish(EXIT_CONFIG_ERROR, "configuration_error")
