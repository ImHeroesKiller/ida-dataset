"""Configuration loader for KAS YAML files."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping, MutableMapping

from .paths import find_repo_root
from .simple_yaml import load_simple_yaml


class ConfigError(RuntimeError):
    """Raised when configuration is missing or invalid."""


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")
    text = path.read_text(encoding="utf-8")

    data: Any
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
    except ImportError:
        data = load_simple_yaml(text)

    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ConfigError(f"Config root must be a mapping: {path}")
    return data


def load_config(
    config_dir: Path | None = None,
    *,
    root: Path | None = None,
) -> dict[str, Any]:
    """Load sources, policies, and scheduler configs into one mapping."""
    repo_root = root or find_repo_root()
    cfg_dir = config_dir or (repo_root / "automation" / "config")

    sources = _load_yaml(cfg_dir / "sources.yaml")
    policies = _load_yaml(cfg_dir / "policies.yaml")
    scheduler = _load_yaml(cfg_dir / "scheduler.yaml")

    return {
        "sources": sources,
        "policies": policies,
        "scheduler": scheduler,
        "config_dir": str(cfg_dir),
        "repo_root": str(repo_root),
    }


def get_nested(config: Mapping[str, Any], *keys: str, default: Any = None) -> Any:
    current: Any = config
    for key in keys:
        if not isinstance(current, Mapping) or key not in current:
            return default
        current = current[key]
    return current


def deep_merge(
    base: MutableMapping[str, Any],
    override: Mapping[str, Any],
) -> MutableMapping[str, Any]:
    """Recursively merge override into base (mutates base)."""
    for key, value in override.items():
        if (
            key in base
            and isinstance(base[key], dict)
            and isinstance(value, Mapping)
        ):
            deep_merge(base[key], value)
        else:
            base[key] = value
    return base
