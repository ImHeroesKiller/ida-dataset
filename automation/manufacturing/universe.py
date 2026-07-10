"""Knowledge universe estimation — dynamic, not hardcoded ceilings."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from automation.lib.paths import find_repo_root
from automation.manufacturing.targets import dataset_profile


def _trusted_source_count(repo: Path) -> int:
    try:
        from automation.acquisition.source_registry import SourceRegistry

        return len(SourceRegistry(repo_root=repo).list_sources())
    except Exception:  # noqa: BLE001
        return 10


def _perf_yield(repo: Path) -> dict[str, float]:
    path = repo / "automation" / "learning" / "state" / "source_performance.json"
    if not path.exists():
        return {"docs": 0.0, "rows": 0.0, "attempts": 0.0}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        sources = data.get("sources") or {}
        docs = sum(float(s.get("documents_yielded") or 0) for s in sources.values())
        rows = sum(float(s.get("rows_yielded") or 0) for s in sources.values())
        attempts = sum(float(s.get("attempts") or 0) for s in sources.values())
        return {"docs": docs, "rows": rows, "attempts": attempts}
    except Exception:  # noqa: BLE001
        return {"docs": 0.0, "rows": 0.0, "attempts": 0.0}


def estimate_universe(
    dataset: str,
    *,
    current_rows: int,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Estimate total possible entities for a dataset using live signals."""
    root = repo_root or find_repo_root()
    profile = dataset_profile(dataset, root)
    stretch = int(profile["stretch_target"])
    minimum = int(profile["minimum_target"])
    n_sources = max(1, _trusted_source_count(root))
    perf = _perf_yield(root)

    # Historical rows-per-source attempt as growth signal
    rows_per_attempt = (perf["rows"] / perf["attempts"]) if perf["attempts"] else 0.5
    # New source growth potential: each trusted source can contribute more entities
    source_capacity = n_sources * max(20.0, rows_per_attempt * 40)

    # Publication frequency proxy: more business_signal / docs → larger universe
    pub_freq = 1.0 + min(5.0, perf["docs"] / 50.0)

    # Dynamic estimate: max of stretch, current+room, source-driven capacity
    base = max(stretch, minimum * 5, int(source_capacity * pub_freq))
    # Grow estimate as we approach previous estimate (never shrink below stretch)
    if current_rows > base * 0.6:
        base = int(current_rows * 1.8 + stretch * 0.2)
    if current_rows > base:
        base = int(current_rows * 1.5) + stretch

    # hard_limit only caps estimate display if set
    hard = profile.get("hard_limit")
    if hard is not None:
        base = min(base, int(hard))

    remaining = max(0, base - current_rows)
    return {
        "dataset": dataset,
        "estimated_universe": base,
        "current_rows": current_rows,
        "remaining_estimate": remaining,
        "fill_pct": round(100.0 * current_rows / base, 2) if base else 0.0,
        "method": "sources_x_yield_x_publication_frequency",
        "signals": {
            "trusted_sources": n_sources,
            "historical_rows_yielded": perf["rows"],
            "historical_docs": perf["docs"],
            "rows_per_attempt": round(rows_per_attempt, 3),
            "publication_frequency_factor": round(pub_freq, 3),
            "stretch_target": stretch,
            "minimum_target": minimum,
            "hard_limit": hard,
        },
    }
