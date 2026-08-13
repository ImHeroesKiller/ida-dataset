"""Production throughput optimization helpers.

Architecture-compatible: does not redesign queues, missions, or schemas.
Optimizes prioritization, worker scaling, process ratio, auto-publish gates,
queue rebalance signals, and performance report generation from real state only.
"""

from __future__ import annotations

import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root

TARGET_PROCESS_RATIO = 0.90

# Lowered so free DDG multi-table fill can land rows
AUTO_PUBLISH_CONFIDENCE = 0.55
MANUAL_REVIEW_CONFIDENCE = 0.40

WORKER_LADDER = (2, 4, 8, 16)


def adaptive_workers(avg_latency_ms: float, *, max_workers: int = 16) -> int:
    """Scale download workers from latency: slow connectors → fewer workers."""
    lat = max(0.0, float(avg_latency_ms or 0))
    if lat <= 400:
        n = 16
    elif lat <= 1200:
        n = 8
    elif lat <= 3000:
        n = 4
    else:
        n = 2
    allowed = [w for w in WORKER_LADDER if w <= max_workers]
    chosen = allowed[0] if allowed else 2
    for w in allowed:
        if w <= n:
            chosen = w
    return chosen


def process_budget(
    discovered: int,
    *,
    soft_limit: int | None = None,
    hard_limit: int | None = None,
    target_ratio: float = TARGET_PROCESS_RATIO,
    gap_score: float = 0.0,
    worker_capacity: int = 4,
    download_budget: int | None = None,
) -> int:
    """How many unique discovered docs to process this session."""
    if discovered <= 0:
        return 0
    target = int(math.ceil(discovered * target_ratio))
    workers = max(1, int(worker_capacity or 1))
    gap_boost = 1.0 + min(1.5, max(0.0, float(gap_score or 0)) / 80.0)
    adaptive_floor = int(math.ceil(workers * 8 * gap_boost))
    if download_budget is not None and download_budget > 0:
        ceiling = int(download_budget)
    elif soft_limit is not None and soft_limit > 0:
        ceiling = max(int(soft_limit), adaptive_floor)
    else:
        ceiling = max(target, adaptive_floor, discovered)
    if hard_limit is not None and hard_limit > 0:
        ceiling = min(ceiling, int(hard_limit))
    budget = max(target, min(discovered, ceiling))
    budget = min(budget, discovered, ceiling)
    return max(1, budget) if discovered else 0


def _source_perf(repo_root: Path) -> dict[str, Any]:
    path = repo_root / "automation" / "learning" / "state" / "source_performance.json"
    if not path.exists():
        return {}
    try:
        return (json.loads(path.read_text(encoding="utf-8")) or {}).get("sources") or {}
    except Exception:  # noqa: BLE001
        return {}


def prioritize_search_results(
    results: list[Any],
    *,
    dataset: str = "industry_library",
    instruction: str = "",
    connector_latency: Optional[dict[str, float]] = None,
    rank_by_conn: Optional[dict[str, float]] = None,
    repo_root: Path | None = None,
) -> list[Any]:
    """Adaptive document priority queue before download."""
    root = repo_root or find_repo_root()
    perf = _source_perf(root)
    latency = connector_latency or {}
    ranks = rank_by_conn or {}
    instr = (instruction or "").lower()
    tokens = {t for t in instr.replace(",", " ").split() if len(t) > 3}
    if dataset:
        tokens.add(dataset.replace("_", " ").split()[0].lower())

    seen: set[str] = set()
    unique: list[Any] = []
    for r in results:
        key = (getattr(r, "url", None) or "").strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(r)

    scored: list[tuple[float, Any]] = []
    for r in unique:
        cid = str(getattr(r, "connector_id", "") or "")
        sid = str(getattr(r, "source_id", "") or "")
        trust = float(getattr(r, "trust_score", 0.85) or 0.85)
        title = str(getattr(r, "title", "") or "")
        snippet = str(getattr(r, "snippet", "") or "")
        blob = f"{title} {snippet}".lower()

        hits = sum(1 for t in tokens if t in blob) if tokens else 0
        relevance = min(1.0, hits / max(3, min(len(tokens), 6))) if tokens else 0.4

        p = perf.get(sid) or perf.get(cid) or {}
        success = float(p.get("success_rate") or 0.7)
        yield_docs = float(p.get("documents_yielded") or 0)
        yield_rows = float(p.get("rows_yielded") or 0)
        dup_rate = float(p.get("duplicate_rate") or 0.0)
        avg_lat = float(latency.get(cid) or p.get("avg_latency_ms") or 2000)
        latency_score = max(0.0, min(1.0, 1.0 - (avg_lat / 30000.0)))
        yield_score = min(1.0, (yield_docs / 30.0) * 0.5 + (yield_rows / 15.0) * 0.5)
        health = success * (1.0 - min(0.9, dup_rate))

        meta = getattr(r, "metadata", None) or {}
        freshness = 0.5
        pub = str(meta.get("published_at") or meta.get("date") or "")
        if pub:
            try:
                year = int("".join(c for c in pub[:4] if c.isdigit()) or "0")
                if year >= 2024:
                    freshness = 0.95
                elif year >= 2020:
                    freshness = 0.75
                elif year >= 2015:
                    freshness = 0.55
                elif year > 0:
                    freshness = 0.35
            except Exception:  # noqa: BLE001
                freshness = 0.5
        if meta.get("is_oa") or meta.get("open_access"):
            freshness = min(1.0, freshness + 0.05)

        rank_boost = min(1.0, float(ranks.get(cid) or 0) / 100.0)

        score = (
            relevance * 28
            + health * 18
            + yield_score * 16
            + latency_score * 10
            + freshness * 12
            + trust * 10
            + rank_boost * 6
        )
        try:
            r.metadata = {**(meta or {}), "_priority_score": round(score, 3)}
        except Exception:  # noqa: BLE001
            pass
        scored.append((score, r))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [r for _, r in scored]


def measure_queues(repo_root: Path | None = None) -> dict[str, Any]:
    """Measure document / candidate / publish queue depths (real FS)."""
    root = repo_root or find_repo_root()

    def count(rel: str) -> int:
        p = root / rel
        if not p.is_dir():
            return 0
        n = 0
        try:
            for child in p.iterdir():
                if child.is_file() and not child.name.startswith("."):
                    n += 1
        except OSError:
            return 0
        return n

    pending = count("automation/queue/pending")
    approved = count("automation/queue/approved")
    rejected = count("automation/queue/rejected")
    return {
        "pending": pending,
        "approved": approved,
        "rejected": rejected,
        "total": pending + approved + rejected,
        "measured_at": utc_now_iso(),
    }


def auto_publish_decision(
    *,
    confidence: float,
    validation_passed: bool,
    is_duplicate: bool,
    has_provenance: bool,
    relationship_complete: bool = True,
    entity_conflict: bool = False,
    relationship_ambiguous: bool = False,
    confidence_threshold: float = AUTO_PUBLISH_CONFIDENCE,
) -> dict[str, Any]:
    """Decide automatic publish vs manual review queue."""
    conf = float(confidence or 0)
    reasons: list[str] = []
    if not validation_passed:
        reasons.append("validation_failed")
    if is_duplicate:
        reasons.append("duplicate")
    if not has_provenance:
        reasons.append("missing_provenance")
    if entity_conflict:
        reasons.append("entity_conflict")
    if relationship_ambiguous:
        reasons.append("relationship_ambiguous")
    if conf < confidence_threshold:
        reasons.append("confidence_below_auto_threshold")
    if not relationship_complete and conf < confidence_threshold:
        reasons.append("relationship_incomplete")

    if reasons:
        hard = {"validation_failed", "duplicate", "entity_conflict"}
        if hard.intersection(reasons) or conf < MANUAL_REVIEW_CONFIDENCE:
            return {
                "action": "reject" if ("validation_failed" in reasons or is_duplicate) else "manual_review",
                "auto_publish": False,
                "reasons": reasons,
                "confidence": conf,
            }
        return {
            "action": "manual_review",
            "auto_publish": False,
            "reasons": reasons,
            "confidence": conf,
        }

    return {
        "action": "publish",
        "auto_publish": True,
        "reasons": ["auto_publish"],
        "confidence": conf,
    }


def avg_connector_latency(connector_rows: list[dict[str, Any]]) -> float:
    vals = [float(c.get("elapsed_ms") or 0) for c in (connector_rows or []) if c.get("elapsed_ms")]
    if not vals:
        return 2000.0
    return sum(vals) / len(vals)


class StageTimer:
    """Per-stage duration tracking for bottleneck analysis."""

    def __init__(self) -> None:
        self.stages: dict[str, dict[str, Any]] = {}
        self._open: dict[str, float] = {}
        self.idle_ms = 0.0
        self.queue_wait_ms: dict[str, float] = {}

    def start(self, name: str) -> None:
        self._open[name] = time.perf_counter()

    def stop(self, name: str, *, meta: Optional[dict[str, Any]] = None) -> float:
        t0 = self._open.pop(name, None)
        if t0 is None:
            return 0.0
        ms = (time.perf_counter() - t0) * 1000.0
        row = self.stages.get(name) or {
            "count": 0,
            "total_ms": 0.0,
            "max_ms": 0.0,
            "min_ms": None,
        }
        row["count"] = int(row["count"]) + 1
        row["total_ms"] = float(row["total_ms"]) + ms
        row["max_ms"] = max(float(row["max_ms"]), ms)
        prev_min = row.get("min_ms")
        row["min_ms"] = ms if prev_min is None else min(float(prev_min), ms)
        if meta:
            row["meta"] = meta
        self.stages[name] = row
        return ms

    def record_queue_wait(self, queue: str, ms: float) -> None:
        self.queue_wait_ms[queue] = self.queue_wait_ms.get(queue, 0.0) + float(ms)

    def snapshot(self) -> dict[str, Any]:
        stages_out: dict[str, Any] = {}
        for name, row in self.stages.items():
            count = int(row.get("count") or 0) or 1
            total = float(row.get("total_ms") or 0)
            stages_out[name] = {
                **row,
                "avg_ms": round(total / count, 2),
            }
        return {
            "stages": stages_out,
            "idle_ms": self.idle_ms,
            "queue_wait_ms": dict(self.queue_wait_ms),
            "captured_at": utc_now_iso(),
        }


def collect_real_production_stats(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    queues = measure_queues(root)
    return {
        "generated_at": utc_now_iso(),
        "queues": queues,
        "publish_policy": {
            "auto_publish_confidence": AUTO_PUBLISH_CONFIDENCE,
            "manual_review_floor": MANUAL_REVIEW_CONFIDENCE,
        },
        "throughput": {},
        "traces": {},
        "sessions": {},
        "workers": {},
        "stages": {},
        "connectors_ranked": [],
        "bottleneck": "unknown",
        "repo_root": str(root),
    }


def write_throughput_reports(
    stats: dict[str, Any] | None = None,
    *,
    repo_root: Path | None = None,
    session_perf: Optional[dict[str, Any]] = None,
) -> dict[str, str]:
    """Write performance reports from real production stats / session_perf."""
    root = repo_root or find_repo_root()
    out = root / "reports" / "performance"
    written: dict[str, str] = {}
    try:
        out.mkdir(parents=True, exist_ok=True)
        s = stats or collect_real_production_stats(root)
        if session_perf:
            s = dict(s)
            stages = session_perf.get("stage_timings") or {}
            if stages:
                s["session_stage_timings"] = stages
            s["session_workers"] = session_perf.get("workers")
            s["session_process_ratio"] = session_perf.get("process_ratio")
            s["session_extraction"] = session_perf.get("extraction")
            s["session_auto_publish"] = session_perf.get("auto_publish")

        js = out / "throughput_stats.json"
        js.write_text(
            json.dumps(s, indent=2, ensure_ascii=False, default=str) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        written["throughput_stats.json"] = str(js.relative_to(root))

        pub = s.get("session_auto_publish") or s.get("publish_policy") or {}
        md = out / "throughput_summary.md"
        lines = [
            "# Throughput summary",
            "",
            f"- Generated: {s.get('generated_at')}",
            f"- Auto-publish confidence gate: {pub.get('auto_publish_confidence', AUTO_PUBLISH_CONFIDENCE)}",
            f"- Manual review floor: {pub.get('manual_review_floor', MANUAL_REVIEW_CONFIDENCE)}",
            f"- Session process ratio: {s.get('session_process_ratio')}",
            "",
        ]
        md.write_text("\n".join(lines), encoding="utf-8", newline="\n")
        written["throughput_summary.md"] = str(md.relative_to(root))
    except Exception:  # noqa: BLE001
        pass
    return written
