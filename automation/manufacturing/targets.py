"""Dynamic production targets — minimum / stretch / universe / hard_limit."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root
from automation.lib.simple_yaml import load_simple_yaml

DEFAULT_PROFILE = {
    "minimum_target": 100,
    "stretch_target": 1000,
    "estimated_universe": "dynamic",
    "hard_limit": None,
}


def load_dynamic_targets(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    path = root / "automation" / "config" / "product_targets.yaml"
    if not path.exists():
        return {
            "version": "2.0",
            "continuous_manufacturing": True,
            "never_stop_at_numeric_target": True,
            "targets": {"_default": 100},
            "datasets": {"_default": dict(DEFAULT_PROFILE)},
        }
    data = load_simple_yaml(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        data = {}
    data.setdefault("continuous_manufacturing", True)
    data.setdefault("never_stop_at_numeric_target", True)
    return data


def dataset_profile(dataset: str, repo_root: Path | None = None) -> dict[str, Any]:
    cfg = load_dynamic_targets(repo_root)
    datasets = cfg.get("datasets") or {}
    flat = cfg.get("targets") or {}
    key = dataset.replace(".csv", "")
    raw = datasets.get(key) or datasets.get("_default") or {}
    if not isinstance(raw, dict):
        raw = {}
    min_t = raw.get("minimum_target")
    if min_t is None:
        min_t = flat.get(key, flat.get("_default", 100))
    stretch = raw.get("stretch_target")
    if stretch is None:
        stretch = max(int(min_t) * 10, int(min_t) + 100)
    hard = raw.get("hard_limit", None)
    # null / None / "null" → no hard limit
    if hard in (None, "null", "None", "", 0, "0"):
        hard = None
    else:
        try:
            hard = int(hard)
        except (TypeError, ValueError):
            hard = None
    return {
        "dataset": key,
        "minimum_target": int(min_t),
        "stretch_target": int(stretch),
        "estimated_universe": raw.get("estimated_universe") or "dynamic",
        "hard_limit": hard,
        "continuous": bool(cfg.get("continuous_manufacturing", True)),
        "never_stop": bool(cfg.get("never_stop_at_numeric_target", True)),
    }


def coverage_against_stretch(current: int, profile: dict[str, Any]) -> float:
    """Progress reference only — reaching 100% does NOT stop manufacturing."""
    stretch = max(1, int(profile.get("stretch_target") or 1))
    return min(100.0, round(100.0 * current / stretch, 2))


def below_minimum(current: int, profile: dict[str, Any]) -> bool:
    return current < int(profile.get("minimum_target") or 0)
