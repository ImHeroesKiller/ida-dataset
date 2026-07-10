"""Multi-stage extraction — fast → deep → (optional) LLM → validation handoff.

Simple documents never invoke expensive extraction.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from automation.acquisition.extractor import (
    extract_business_signal_candidates,
    extract_industry_candidates,
)
from automation.lib.models import CandidateRecord


def extract_staged(
    documents: list[dict[str, Any]],
    *,
    mission_id: str = "",
    session_id: str = "",
    dataset: str = "industry_library",
    repo_root: Path | None = None,
    max_candidates: int = 5,
) -> dict[str, Any]:
    """Run staged extraction. Returns candidates + stage stats."""
    stats = {
        "fast": 0,
        "deep": 0,
        "llm": 0,
        "skipped_llm": 0,
        "documents_fast": 0,
        "documents_deep": 0,
    }
    fast_docs: list[dict[str, Any]] = []
    deep_docs: list[dict[str, Any]] = []

    for doc in documents:
        meta = doc.get("metadata") or {}
        text = str(meta.get("text_excerpt") or meta.get("snippet") or doc.get("title") or "")
        length = len(text)
        # Fast path: short metadata / abstract-only docs
        if length < 2500 or meta.get("metadata_only"):
            fast_docs.append(doc)
            stats["documents_fast"] += 1
        else:
            deep_docs.append(doc)
            stats["documents_deep"] += 1

    candidates: list[CandidateRecord] = []

    # Stage 1 — Fast extraction (alias match + short evidence)
    if fast_docs:
        batch = extract_industry_candidates(
            fast_docs,
            mission_id=mission_id,
            session_id=session_id,
            repo_root=repo_root,
            max_candidates=max_candidates,
        )
        stats["fast"] += len(batch)
        candidates.extend(batch)

    # Stage 2 — Deep extraction on longer docs if still under cap
    remaining = max_candidates - len(candidates)
    if deep_docs and remaining > 0:
        batch = extract_industry_candidates(
            deep_docs,
            mission_id=mission_id,
            session_id=session_id,
            repo_root=repo_root,
            max_candidates=remaining,
        )
        stats["deep"] += len(batch)
        candidates.extend(batch)

    # Fallback business signals if nothing grounded yet
    if not candidates:
        batch = extract_business_signal_candidates(
            documents,
            mission_id=mission_id,
            session_id=session_id,
            repo_root=repo_root,
            max_candidates=min(3, max_candidates),
        )
        stats["fast"] += len(batch)
        candidates.extend(batch)

    # Stage 3 — LLM extraction intentionally NOT invoked for simple/grounded paths
    # (no API key / cost path in factory core). Mark as skipped for observability.
    stats["skipped_llm"] = len(documents)
    stats["llm"] = 0

    for c in candidates:
        stage = "fast" if c.candidate_id and stats["deep"] == 0 else (
            "deep" if any(
                (c.metadata or {}).get("document_id") == d.get("document_id") for d in deep_docs
            )
            else "fast"
        )
        c.metadata = {**(c.metadata or {}), "extraction_stage": stage}

    return {
        "candidates": candidates,
        "stats": stats,
        "stages": ["fast", "deep", "llm_skipped", "validation_handoff"],
    }
