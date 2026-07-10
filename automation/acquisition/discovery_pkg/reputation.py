"""Source reputation scoring for discovery prioritization."""

from __future__ import annotations

from typing import Any

from automation.acquisition.source_ranker import rank_sources


def category_authority(category: str) -> float:
    c = (category or "").lower()
    if "government" in c:
        return 1.0
    if "international" in c:
        return 0.95
    if "scientific" in c or "research" in c:
        return 0.9
    if "industry" in c or "association" in c:
        return 0.75
    if "market" in c or "commercial" in c:
        return 0.65
    if "open_data" in c:
        return 0.85
    return 0.5


def score_sources_for_discovery(
    sources: list[dict[str, Any]],
    *,
    dataset: str = "industry_library",
    repo_root=None,
) -> list[dict[str, Any]]:
    """Rank trusted sources for discovery site: targeting."""
    ranked = rank_sources(
        sources,
        dataset=dataset,
        repo_root=repo_root,
        min_trust=0.80,
    )
    for s in ranked:
        auth = category_authority(str(s.get("category") or ""))
        base = float(s.get("_rank_score") or 0)
        s["_reputation"] = round(base * 0.85 + auth * 20, 3)
        s["_authority"] = auth
    ranked.sort(key=lambda r: float(r.get("_reputation") or 0), reverse=True)
    return ranked
