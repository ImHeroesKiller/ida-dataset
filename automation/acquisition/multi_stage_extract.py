"""Multi-stage extraction — fast → medium → deep → (optional) LLM.

Skip expensive extraction whenever deterministic extraction is sufficient.
"""

from __future__ import annotations

import time
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
    t_all = time.perf_counter()
    stats: dict[str, Any] = {
        "fast": 0,
        "medium": 0,
        "deep": 0,
        "llm": 0,
        "llm_used": 0,
        "skipped_llm": 0,
        "llm_skipped": 0,
        "documents_fast": 0,
        "documents_medium": 0,
        "documents_deep": 0,
        "avg_ms": 0.0,
        "average_extraction_ms": 0.0,
        "total_ms": 0.0,
        "path_ms": {},
    }
    fast_docs: list[dict[str, Any]] = []
    medium_docs: list[dict[str, Any]] = []
    deep_docs: list[dict[str, Any]] = []

    for doc in documents:
        meta = doc.get("metadata") or {}
        text = str(meta.get("text_excerpt") or meta.get("snippet") or doc.get("title") or "")
        length = len(text)
        # Fast path: metadata only / short abstract
        if length < 1200 or meta.get("metadata_only"):
            fast_docs.append(doc)
            stats["documents_fast"] += 1
        # Medium path: normal text extraction (deterministic)
        elif length < 8000:
            medium_docs.append(doc)
            stats["documents_medium"] += 1
        else:
            deep_docs.append(doc)
            stats["documents_deep"] += 1

    candidates: list[CandidateRecord] = []

    def _run_path(
        label: str,
        docs: list[dict[str, Any]],
        remaining: int,
    ) -> list[CandidateRecord]:
        if not docs or remaining <= 0:
            return []
        t0 = time.perf_counter()
        batch = extract_industry_candidates(
            docs,
            mission_id=mission_id,
            session_id=session_id,
            repo_root=repo_root,
            max_candidates=remaining,
        )
        stats["path_ms"][label] = round((time.perf_counter() - t0) * 1000, 2)
        return batch

    # Stage 1 — Fast (metadata only)
    batch = _run_path("fast", fast_docs, max_candidates)
    stats["fast"] += len(batch)
    candidates.extend(batch)

    # Stage 2 — Medium (text extraction, still deterministic)
    remaining = max_candidates - len(candidates)
    batch = _run_path("medium", medium_docs, remaining)
    stats["medium"] += len(batch)
    candidates.extend(batch)

    # Stage 3 — Deep (long docs) only if still under cap
    remaining = max_candidates - len(candidates)
    batch = _run_path("deep", deep_docs, remaining)
    stats["deep"] += len(batch)
    candidates.extend(batch)

    # Fallback business signals if nothing grounded yet
    if not candidates:
        t0 = time.perf_counter()
        batch = extract_business_signal_candidates(
            documents,
            mission_id=mission_id,
            session_id=session_id,
            repo_root=repo_root,
            max_candidates=min(5, max_candidates),
        )
        stats["path_ms"]["signal_fallback"] = round((time.perf_counter() - t0) * 1000, 2)
        stats["fast"] += len(batch)
        candidates.extend(batch)

    # Stage 4 — LLM only if required (insufficient deterministic yield)
    # Factory core keeps LLM off; skip for cost/latency unless empty after deep.
    need_llm = len(candidates) == 0 and len(documents) > 0
    if need_llm:
        # No LLM backend in frozen factory core — record required-but-unavailable
        stats["llm"] = 0
        stats["llm_used"] = 0
        stats["skipped_llm"] = len(documents)
        stats["llm_skipped"] = len(documents)
        stats["llm_required_but_unavailable"] = True
    else:
        stats["llm"] = 0
        stats["llm_used"] = 0
        stats["skipped_llm"] = len(documents)
        stats["llm_skipped"] = len(documents)
        stats["llm_required_but_unavailable"] = False

    total_ms = (time.perf_counter() - t_all) * 1000.0
    stats["total_ms"] = round(total_ms, 2)
    stats["avg_ms"] = round(total_ms / max(1, len(documents)), 2)
    stats["average_extraction_ms"] = stats["avg_ms"]

    for c in candidates:
        did = (c.metadata or {}).get("document_id")
        if any(d.get("document_id") == did for d in deep_docs):
            stage = "deep"
        elif any(d.get("document_id") == did for d in medium_docs):
            stage = "medium"
        else:
            stage = "fast"
        c.metadata = {**(c.metadata or {}), "extraction_stage": stage}

    return {
        "candidates": candidates,
        "stats": stats,
        "stages": ["fast", "medium", "deep", "llm_skipped", "validation_handoff"],
    }
