"""Knowledge Gap Engine — multi-dimensional gap scoring (not coverage-only)."""

from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root
from automation.manufacturing.targets import (
    below_minimum,
    coverage_against_stretch,
    dataset_profile,
)
from automation.manufacturing.universe import estimate_universe


def _row_count(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8-sig", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def _field_coverage(path: Path, sample: int = 50) -> float:
    if not path.exists():
        return 0.0
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return 0.0
    fields = list(rows[0].keys())
    if not fields:
        return 0.0
    scores = []
    for r in rows[:sample]:
        filled = sum(1 for h in fields if str(r.get(h) or "").strip())
        scores.append(filled / len(fields))
    return round(sum(scores) / len(scores), 4)


def _confidence_avg(path: Path, sample: int = 80) -> float:
    if not path.exists():
        return 0.0
    vals: list[float] = []
    with path.open(encoding="utf-8-sig", newline="") as f:
        for i, r in enumerate(csv.DictReader(f)):
            if i >= sample:
                break
            blob = " ".join(str(r.get(k) or "") for k in ("Notes", "Data Sources", "Confidence"))
            m = re.search(r"confidence[=:\s]+([0-9]*\.?[0-9]+)", blob, re.I)
            if m:
                v = float(m.group(1))
                vals.append(v / 100.0 if v > 1 else v)
    if not vals:
        return 0.85  # neutral when unknown
    return round(sum(vals) / len(vals), 4)


def _freshness_score(path: Path, window_days: int = 90) -> float:
    """Share of rows with Last Updated / retrieved in window — heuristic."""
    if not path.exists():
        return 0.0
    from datetime import datetime, timezone, timedelta

    cutoff = datetime.now(timezone.utc) - timedelta(days=window_days)
    total = 0
    fresh = 0
    with path.open(encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            total += 1
            blob = " ".join(
                str(r.get(k) or "")
                for k in ("Last Updated", "Notes", "Data Sources", "Retrieved Date")
            )
            # ISO-like dates
            dates = re.findall(r"20\d{2}-\d{2}-\d{2}", blob)
            if not dates:
                continue
            try:
                d = datetime.fromisoformat(dates[-1]).replace(tzinfo=timezone.utc)
                if d >= cutoff:
                    fresh += 1
            except ValueError:
                continue
    if total == 0:
        return 0.0
    return round(fresh / total, 4)


def _relationship_gap(dataset: str, counts: dict[str, int]) -> float:
    """0 = well linked, 1 = severe relationship gap."""
    if dataset == "company_profile":
        ind = counts.get("industry_library", 0)
        return 0.0 if ind >= 50 else 0.8
    if dataset == "pain_point_library":
        return 0.0 if counts.get("industry_library", 0) >= 25 else 0.7
    if dataset == "solution_library":
        return 0.0 if counts.get("pain_point_library", 0) >= 10 else 0.75
    if dataset == "case_study_library":
        return 0.0 if counts.get("company_profile", 0) >= 25 else 0.7
    if dataset == "opportunity_analysis":
        return 0.0 if counts.get("company_profile", 0) >= 25 else 0.6
    if dataset in {"competitor_library", "buyer_persona_library"}:
        return 0.5 if counts.get(dataset, 0) == 0 else 0.2
    return 0.2


def evaluate_dataset(
    dataset: str,
    *,
    path: Path | None = None,
    counts: Optional[dict[str, int]] = None,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Full multi-dimensional knowledge gap evaluation."""
    root = repo_root or find_repo_root()
    profile = dataset_profile(dataset, root)
    if path is None:
        path = root / "domains" / "business_development" / f"{dataset}.csv"
    current = _row_count(path) if path else 0
    if counts and dataset in counts:
        current = counts[dataset]

    universe = estimate_universe(dataset, current_rows=current, repo_root=root)
    stretch_cov = coverage_against_stretch(current, profile)
    min_gap = max(0, int(profile["minimum_target"]) - current)
    stretch_gap = max(0, int(profile["stretch_target"]) - current)
    universe_gap = int(universe["remaining_estimate"])

    density = _field_coverage(path) if path else 0.0
    conf = _confidence_avg(path) if path else 0.0
    fresh = _freshness_score(path) if path else 0.0
    rel_gap = _relationship_gap(dataset, counts or {})

    # Knowledge opportunity: remaining universe + empty boost
    opportunity = universe_gap + (500 if current == 0 else 0)

    # Composite knowledge gap score (higher = more urgent manufacturing demand)
    # Not coverage-only
    knowledge_gap_score = (
        (universe_gap / max(1, universe["estimated_universe"])) * 40
        + (1.0 - min(1.0, stretch_cov / 100.0)) * 20
        + (1.0 - conf) * 15
        + (1.0 - fresh) * 10
        + (1.0 - density) * 10
        + rel_gap * 15
        + (25.0 if current == 0 else 0.0)
        + (15.0 if below_minimum(current, profile) else 0.0)
    )

    return {
        "dataset": dataset,
        "current_rows": current,
        "profile": profile,
        "universe": universe,
        "coverage_stretch_pct": stretch_cov,
        "coverage_minimum_pct": round(
            100.0 * current / max(1, int(profile["minimum_target"])), 2
        ),
        "knowledge_gap": universe_gap + min_gap,
        "minimum_gap": min_gap,
        "stretch_gap": stretch_gap,
        "universe_gap": universe_gap,
        "knowledge_opportunity": opportunity,
        "freshness_gap": round(1.0 - fresh, 4),
        "confidence_gap": round(1.0 - conf, 4),
        "relationship_gap": rel_gap,
        "knowledge_density": density,
        "avg_confidence": conf,
        "freshness": fresh,
        "knowledge_gap_score": round(knowledge_gap_score, 3),
        "below_minimum": below_minimum(current, profile),
        "hard_limit": profile.get("hard_limit"),
        "should_continue": True,  # never stop for numeric target alone
    }


def rank_datasets(
    datasets: list[str],
    *,
    counts: Optional[dict[str, int]] = None,
    repo_root: Path | None = None,
) -> list[dict[str, Any]]:
    root = repo_root or find_repo_root()
    out = [evaluate_dataset(d, counts=counts, repo_root=root) for d in datasets]
    out.sort(key=lambda x: -float(x.get("knowledge_gap_score") or 0))
    return out
