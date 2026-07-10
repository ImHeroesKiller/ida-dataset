"""Load learning scheduler configuration (YAML, no hardcoding)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from automation.lib.paths import find_repo_root
from automation.lib.simple_yaml import load_simple_yaml


def load_learning_config(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    path = root / "automation" / "config" / "learning.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Learning config not found: {path}")
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
    except ImportError:
        data = load_simple_yaml(text)
    if not isinstance(data, dict):
        raise ValueError("learning.yaml root must be a mapping")
    data["_repo_root"] = str(root)
    data["_config_path"] = str(path)
    return data


def resolve_path(config: dict[str, Any], key: str, default: str) -> Path:
    root = Path(config["_repo_root"])
    rel = (config.get("paths") or {}).get(key, default)
    p = Path(rel)
    return p if p.is_absolute() else root / p


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
