"""Adaptive source prioritization — live ranking for mission acquisition.

Score uses real health / yield / latency / failure signals only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root
from automation.lib.source_health import load_metrics


def rank_sources(
    sources: list[dict[str, Any]],
    *,
    dataset: str = "industry_library",
    preferred_source_ids: Optional[list[str]] = None,
    repo_root: Path | None = None,
    min_trust: float = 0.80,
) -> list[dict[str, Any]]:
    """Return sources sorted by adaptive score (highest first), with score fields attached."""
    root = repo_root or find_repo_root()
    metrics = load_metrics(root)
    src_metrics = metrics.get("sources") or {}
    if isinstance(src_metrics, list):
        src_metrics = {s.get("source_id"): s for s in src_metrics if isinstance(s, dict)}

    # optional performance history
    perf_path = root / "automation" / "learning" / "state" / "source_performance.json"
    perf: dict[str, Any] = {}
    if perf_path.exists():
        try:
            perf = json.loads(perf_path.read_text(encoding="utf-8")).get("sources") or {}
        except Exception:  # noqa: BLE001
            perf = {}

    preferred = set(preferred_source_ids or [])
    ranked: list[dict[str, Any]] = []

    for s in sources:
        if not s.get("enabled", True):
            continue
        trust = float(s.get("trust_score") or 0)
        if trust < min_trust:
            continue
        allowed = s.get("allowed_datasets") or []
        if allowed and dataset not in allowed and "*" not in allowed:
            if trust < 0.90:
                continue

        sid = str(s.get("id") or "")
        m = src_metrics.get(sid) or {}
        p = perf.get(sid) or {}

        health = str(m.get("health_status") or "unknown")
        health_score = {
            "healthy": 1.0,
            "degraded": 0.5,
            "unknown": 0.4,
            "down": 0.0,
            "offline": 0.0,
            "rate_limited": 0.3,
            "auth_error": 0.1,
        }.get(health, 0.4)

        success_rate = float(m.get("success_rate") or p.get("success_rate") or 0.5)
        failure_rate = 1.0 - success_rate
        latency_ms = float(
            m.get("average_processing_time_ms")
            or p.get("avg_latency_ms")
            or 5000
        )
        # lower latency better → score 0..1
        latency_score = max(0.0, min(1.0, 1.0 - (latency_ms / 30000.0)))

        yield_docs = float(p.get("documents_yielded") or m.get("documents_processed") or 0)
        yield_rows = float(p.get("rows_yielded") or m.get("rows_produced") or 0)
        yield_score = min(1.0, (yield_docs / 50.0) * 0.5 + (yield_rows / 20.0) * 0.5)

        avg_conf = float(p.get("avg_confidence") or 0.85)
        conf_score = max(0.0, min(1.0, avg_conf))

        dup_rate = float(p.get("duplicate_rate") or 0.0)
        dup_score = max(0.0, 1.0 - dup_rate)

        # freshness: recency of last success (hours) — fresher better
        freshness_score = float(p.get("freshness_score") or 0.5)
        if m.get("last_successful_sync"):
            freshness_score = max(freshness_score, 0.7)

        coverage = float(m.get("coverage") or p.get("coverage_contribution") or 0.0)
        coverage_score = max(0.0, min(1.0, coverage if coverage <= 1 else coverage / 100.0))

        priority = float(s.get("priority") or 50) / 100.0

        mission_compat = 1.0 if (not allowed or dataset in allowed or "*" in allowed) else 0.4
        if sid in preferred:
            mission_compat = 1.0

        # Weighted live score (0..100)
        score = (
            health_score * 18
            + success_rate * 12
            + (1.0 - failure_rate) * 8
            + latency_score * 10
            + yield_score * 15
            + conf_score * 10
            + dup_score * 7
            + freshness_score * 8
            + coverage_score * 6
            + priority * 10
            + mission_compat * 10
            + trust * 10
        )
        if sid in preferred:
            score += 25

        # temporary disable / backoff from performance state
        if p.get("disabled_until"):
            # still list but sink score
            score *= 0.05
        if p.get("backoff_level", 0) > 0:
            score *= max(0.2, 1.0 - 0.15 * int(p.get("backoff_level") or 0))

        row = dict(s)
        row["_rank_score"] = round(score, 3)
        row["_rank_breakdown"] = {
            "health": round(health_score, 3),
            "success_rate": round(success_rate, 3),
            "latency_score": round(latency_score, 3),
            "yield_score": round(yield_score, 3),
            "confidence": round(conf_score, 3),
            "duplicate_score": round(dup_score, 3),
            "freshness": round(freshness_score, 3),
            "coverage": round(coverage_score, 3),
            "priority": round(priority, 3),
            "mission_compat": round(mission_compat, 3),
            "trust": round(trust, 3),
        }
        ranked.append(row)

    ranked.sort(key=lambda r: float(r.get("_rank_score") or 0), reverse=True)
    return ranked


def record_source_performance(
    source_id: str,
    *,
    success: bool,
    documents: int = 0,
    rows: int = 0,
    latency_ms: float = 0.0,
    duplicates: int = 0,
    confidence: float | None = None,
    repo_root: Path | None = None,
) -> None:
    """Update adaptive performance history for a source (append-only counters)."""
    root = repo_root or find_repo_root()
    path = root / "automation" / "learning" / "state" / "source_performance.json"
    data: dict[str, Any] = {"sources": {}}
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            data = {"sources": {}}
    sources = data.setdefault("sources", {})
    row = sources.get(source_id) or {
        "source_id": source_id,
        "attempts": 0,
        "successes": 0,
        "failures": 0,
        "documents_yielded": 0,
        "rows_yielded": 0,
        "duplicates": 0,
        "total_latency_ms": 0.0,
        "confidence_sum": 0.0,
        "confidence_n": 0,
        "backoff_level": 0,
        "disabled_until": None,
    }
    row["attempts"] = int(row.get("attempts") or 0) + 1
    if success:
        row["successes"] = int(row.get("successes") or 0) + 1
        row["backoff_level"] = max(0, int(row.get("backoff_level") or 0) - 1)
        row["disabled_until"] = None
    else:
        row["failures"] = int(row.get("failures") or 0) + 1
        row["backoff_level"] = min(8, int(row.get("backoff_level") or 0) + 1)
        # temporary disable after repeated failures
        if int(row["backoff_level"]) >= 5:
            import time

            row["disabled_until"] = time.time() + (60 * (2 ** min(row["backoff_level"], 6)))
    row["documents_yielded"] = int(row.get("documents_yielded") or 0) + int(documents)
    row["rows_yielded"] = int(row.get("rows_yielded") or 0) + int(rows)
    row["duplicates"] = int(row.get("duplicates") or 0) + int(duplicates)
    row["total_latency_ms"] = float(row.get("total_latency_ms") or 0) + float(latency_ms)
    attempts = max(1, int(row["attempts"]))
    row["success_rate"] = round(int(row["successes"]) / attempts, 4)
    row["avg_latency_ms"] = round(float(row["total_latency_ms"]) / attempts, 1)
    total_docs = max(1, int(row["documents_yielded"]) + int(row["duplicates"]))
    row["duplicate_rate"] = round(int(row["duplicates"]) / total_docs, 4)
    if confidence is not None:
        row["confidence_sum"] = float(row.get("confidence_sum") or 0) + float(confidence)
        row["confidence_n"] = int(row.get("confidence_n") or 0) + 1
        row["avg_confidence"] = round(
            float(row["confidence_sum"]) / max(1, int(row["confidence_n"])), 4
        )
    sources[source_id] = row
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
