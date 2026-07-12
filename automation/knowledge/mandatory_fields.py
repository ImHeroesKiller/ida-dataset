"""Mandatory field policy — additive configuration loader.

Does not alter CSV layouts. Field names match existing domain headers.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root

# Fallback if config file missing (mirrors knowledge_quality.yaml)
_DEFAULT_MANDATORY: dict[str, list[str]] = {
    "company_profile": ["Company Name", "Industry", "Country"],
    "product_catalog": ["Product Name", "Product Category"],
    "service_library": ["Product Name", "Product Description"],
    "industry_library": ["Industry Name", "Industry Category"],
    "buyer_persona_library": ["Persona Name", "Industry"],
    "decision_maker_library": ["Title", "Industry"],
    "risk_library": ["Risk Name", "Description"],
    "regulation_library": ["Regulation Name", "Jurisdiction"],
    "trend_library": ["Trend Title", "Description"],
    "competitor_library": ["Competitor Name", "Industry Category"],
    "framework_library": ["Framework Name", "Description"],
    "case_study_library": ["Case Name", "Challenge"],
    "solution_library": ["Solution Name", "Solution Description"],
    "pain_point_library": ["Pain Point", "Description"],
    "opportunity_analysis": ["Opportunity Name", "Opportunity Description"],
    "business_signal_library": ["Signal Name", "Description"],
}


def _config_path(repo_root: Optional[Path] = None) -> Path:
    root = repo_root or find_repo_root()
    return root / "automation" / "config" / "knowledge_quality.yaml"


@lru_cache(maxsize=4)
def _load_config_cached(config_file: str) -> dict[str, Any]:
    path = Path(config_file)
    if not path.exists():
        return {}
    try:
        from automation.lib.simple_yaml import load_simple_yaml

        data = load_simple_yaml(path.read_text(encoding="utf-8")) or {}
        return data if isinstance(data, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


def load_quality_config(repo_root: Optional[Path] = None) -> dict[str, Any]:
    """Load knowledge_quality.yaml (uncached path resolution, cached content)."""
    path = _config_path(repo_root)
    return dict(_load_config_cached(str(path.resolve())))


def clear_config_cache() -> None:
    _load_config_cached.cache_clear()


def mandatory_fields_for(
    target_dataset: str,
    *,
    repo_root: Optional[Path] = None,
) -> list[str]:
    """Return mandatory CSV column names for a dataset id."""
    ds = (target_dataset or "").strip()
    cfg = load_quality_config(repo_root)
    block = cfg.get("mandatory_fields") or {}
    if isinstance(block, dict) and ds in block:
        raw = block[ds]
        if isinstance(raw, list):
            return [str(x).strip() for x in raw if str(x).strip()]
    return list(_DEFAULT_MANDATORY.get(ds, []))


def all_mandatory_catalog(
    *,
    repo_root: Optional[Path] = None,
) -> dict[str, list[str]]:
    """Full dataset → mandatory fields map."""
    cfg = load_quality_config(repo_root)
    block = cfg.get("mandatory_fields")
    if isinstance(block, dict) and block:
        out: dict[str, list[str]] = {}
        for k, v in block.items():
            if isinstance(v, list):
                out[str(k)] = [str(x).strip() for x in v if str(x).strip()]
        if out:
            return out
    return {k: list(v) for k, v in _DEFAULT_MANDATORY.items()}


def thresholds(*, repo_root: Optional[Path] = None) -> dict[str, float]:
    cfg = load_quality_config(repo_root)
    t = cfg.get("thresholds") or {}
    if not isinstance(t, dict):
        t = {}
    return {
        "min_completeness_to_publish": float(
            t.get("min_completeness_to_publish", 0.70)
        ),
        "min_confidence_to_publish": float(t.get("min_confidence_to_publish", 0.80)),
        "enrichment_completeness_ceiling": float(
            t.get("enrichment_completeness_ceiling", 0.70)
        ),
    }
