"""Structured runtime failure records.

Every failure must include:
  timestamp, component, exception, stack_trace,
  correlation_id, session_id, recovery_action
"""

from __future__ import annotations

import json
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional
from uuid import uuid4

from automation.lib.paths import find_repo_root
from automation.runtime.lifecycle import logs_dir, write_status, RuntimeState


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


# Failures that may be retried automatically (limited)
RECOVERABLE_EXCEPTION_TYPES = {
    "OSError",
    "TimeoutError",
    "ConnectionError",
    "ConnectionResetError",
    "BrokenPipeError",
    "TemporaryFailure",
    "QueueBusy",
    "ConnectorTimeout",
}

# Never auto-recover these — stop runtime and surface to dashboard
UNRECOVERABLE_EXCEPTION_TYPES = {
    "ImportError",
    "ModuleNotFoundError",
    "PermissionError",
    "SystemExit",
    "KeyboardInterrupt",
    "ConfigError",
    "LockError",
    "ValidationError",
}


def classify_recoverable(exc: BaseException | str, *, component: str = "") -> bool:
    name = type(exc).__name__ if isinstance(exc, BaseException) else str(exc)
    if name in UNRECOVERABLE_EXCEPTION_TYPES:
        return False
    if name in RECOVERABLE_EXCEPTION_TYPES:
        return True
    # component-level heuristics
    if component.startswith("connector") or component.startswith("queue"):
        msg = str(exc).lower()
        if any(x in msg for x in ("timeout", "temporarily", "busy", "reset", "unavailable")):
            return True
    return False


def recovery_suggestion(
    *,
    exception_name: str,
    component: str,
    recoverable: bool,
    message: str = "",
) -> str:
    if not recoverable:
        if exception_name in {"ImportError", "ModuleNotFoundError"}:
            return (
                "Install missing Python dependencies and verify "
                "`python3 -m automation.learning.live_runtime` runs from the repo root."
            )
        if exception_name == "PermissionError":
            return "Fix filesystem permissions on automation/runtime and domain CSVs, then restart."
        if "lock" in component.lower() or "already" in message.lower():
            return "Wait for the existing session to finish, or stop the held process, then retry."
        if "VERCEL" in message or "ECC_DISABLE_PYTHON" in message:
            return (
                "Live Python runtime cannot run on this host. "
                "Run locally with `python3 -m automation.learning.live_runtime` "
                "or unset ECC_DISABLE_PYTHON on a host that has Python."
            )
        return "Inspect /api/runtime/logs and automation/runtime/logs/, fix the root cause, then retry."
    if component.startswith("connector"):
        return "Temporary connector failure — runtime will retry; if it persists check connector health."
    if component.startswith("queue"):
        return "Temporary queue IO issue — runtime will retry; check disk space and queue directories."
    return "Temporary failure — automatic recovery will retry a limited number of times."


def record_failure(
    *,
    component: str,
    exception: BaseException | str,
    session_id: str | None = None,
    correlation_id: str | None = None,
    recovery_action: str | None = None,
    stack_trace: str | None = None,
    meta: dict[str, Any] | None = None,
    update_status: bool = True,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Write a JSON failure record under automation/runtime/logs/."""
    root = repo_root or find_repo_root()
    log_dir = logs_dir(root)
    cid = correlation_id or f"CORR-{uuid4().hex[:12].upper()}"
    if isinstance(exception, BaseException):
        exc_name = type(exception).__name__
        message = str(exception)
        stack = stack_trace or "".join(
            traceback.format_exception(type(exception), exception, exception.__traceback__)
        )
    else:
        exc_name = str(exception)
        message = str(exception)
        stack = stack_trace or ""

    recoverable = classify_recoverable(
        exception if isinstance(exception, BaseException) else exc_name,
        component=component,
    )
    action = recovery_action or (
        "auto_retry" if recoverable else "stop_and_notify"
    )
    suggestion = recovery_suggestion(
        exception_name=exc_name,
        component=component,
        recoverable=recoverable,
        message=message,
    )

    record = {
        "timestamp": utc_now_iso(),
        "component": component,
        "exception": exc_name,
        "message": message,
        "stack_trace": stack,
        "correlation_id": cid,
        "session_id": session_id,
        "recovery_action": action,
        "recoverable": recoverable,
        "recovery_suggestion": suggestion,
        "meta": meta or {},
    }

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    fname = f"error_{stamp}_{cid}.json"
    path = log_dir / fname
    path.write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    # also append to channel log
    channel = log_dir / "errors.jsonl"
    with channel.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    if update_status and not recoverable:
        write_status(
            {
                "status": RuntimeState.FAILED.value,
                "session_id": session_id,
                "correlation_id": cid,
                "stopped_at": utc_now_iso(),
                "last_error": record,
                "health": {
                    "runtime": "failed",
                    "scheduler": "warning",
                    "connector": "warning",
                    "queue": "warning",
                    "sse": "healthy",
                    "publisher": "warning",
                },
            },
            repo_root=root,
        )
    return record


def list_error_logs(limit: int = 50, repo_root: Path | None = None) -> list[dict[str, Any]]:
    root = repo_root or find_repo_root()
    channel = logs_dir(root) / "errors.jsonl"
    if not channel.exists():
        return []
    lines = channel.read_text(encoding="utf-8").splitlines()
    out: list[dict[str, Any]] = []
    for line in lines[-limit:]:
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return list(reversed(out))
