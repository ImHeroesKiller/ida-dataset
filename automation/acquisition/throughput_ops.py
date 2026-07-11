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

# Process ratio target: discovered → processed
TARGET_PROCESS_RATIO = 0.90

# Auto-publish confidence (maintain published quality ≥ 0.92)
AUTO_PUBLISH_CONFIDENCE = 0.92
MANUAL_REVIEW_CONFIDENCE = 0.80

# Adaptive download workers based on observed connector latency
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
    # pick highest allowed ≤ n
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
    """How many unique discovered docs to process this session.

    Targets ≥90% process ratio. Soft/hard limits are optional policy rails only —
    never arbitrary 5/10/20/50 document caps. When download_budget is provided
    (adaptive discovery budget), it is preferred as the session ceiling.
    """
    if discovered <= 0:
        return 0
    target = int(math.ceil(discovered * target_ratio))
    # Adaptive floor: workers × gap-scaled batch — not a fixed 32
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
    """Adaptive document priority queue before download.

    Weights: freshness · connector health · mission relevance · trust · ROI rank.
    Dedupes by URL first.
    """
    root = repo_root or find_repo_root()
    perf = _source_perf(root)
    latency = connector_latency or {}
    ranks = rank_by_conn or {}
    instr = (instruction or "").lower()
    tokens = {t for t in instr.replace(",", " ").split() if len(t) > 3}
    if dataset:
        tokens.add(dataset.replace("_", " ").split()[0].lower())

    # URL dedupe before ranking
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

        # Mission relevance
        hits = sum(1 for t in tokens if t in blob) if tokens else 0
        relevance = min(1.0, hits / max(3, min(len(tokens), 6))) if tokens else 0.4

        # Connector / source health from live performance
        p = perf.get(sid) or perf.get(cid) or {}
        success = float(p.get("success_rate") or 0.7)
        yield_docs = float(p.get("documents_yielded") or 0)
        yield_rows = float(p.get("rows_yielded") or 0)
        dup_rate = float(p.get("duplicate_rate") or 0.0)
        avg_lat = float(latency.get(cid) or p.get("avg_latency_ms") or 2000)
        latency_score = max(0.0, min(1.0, 1.0 - (avg_lat / 30000.0)))
        yield_score = min(1.0, (yield_docs / 30.0) * 0.5 + (yield_rows / 15.0) * 0.5)
        health = success * (1.0 - min(0.9, dup_rate))

        # Freshness: prefer results with published_at / recent metadata
        meta = getattr(r, "metadata", None) or {}
        freshness = 0.5
        pub = str(meta.get("published_at") or meta.get("date") or "")
        if pub:
            try:
                # year in string → crude freshness
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
        # attach for observability
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
        if not p.exists():
            return 0
        return len([f for f in p.iterdir() if f.suffix == ".json"])

    doc_incoming = count("automation/documents/incoming") + count(
        "automation/queue/documents/incoming"
    )
    doc_processing = count("automation/documents/processing") + count(
        "automation/queue/documents/processing"
    )
    doc_processed = count("automation/documents/processed") + count(
        "automation/queue/documents/processed"
    )
    cand_pending = count("automation/queue/pending") + count(
        "automation/queue/candidates/pending"
    )
    cand_approved = count("automation/queue/approved")
    cand_rejected = count("automation/queue/rejected")
    publish = count("automation/queue/publish")

    total_doc = doc_incoming + doc_processing + doc_processed
    total_cand = cand_pending + cand_approved + cand_rejected + publish

    # Starvation / imbalance heuristics (observability, not redesign)
    starvation: list[str] = []
    if doc_incoming > 0 and doc_processing == 0:
        starvation.append("document_queue_idle_workers")
    if cand_pending > 5 and publish == 0 and cand_approved == 0:
        starvation.append("candidate_queue_not_advancing")
    if cand_approved > 10 and publish == 0:
        starvation.append("publish_queue_starved_of_approved")
    if publish > 20:
        starvation.append("publish_queue_backlog")
    if doc_incoming > doc_processed * 2 and doc_processed > 0:
        starvation.append("discovery_outpaces_processing")

    rebalance = {
        "prefer_process_incoming": doc_incoming > 0,
        "prefer_drain_publish": publish > 5,
        "prefer_review_pending": cand_pending > 0 and cand_approved == 0,
        "document_weight": min(1.0, doc_incoming / max(1, total_doc)),
        "candidate_weight": min(1.0, cand_pending / max(1, total_cand or 1)),
        "publish_weight": min(1.0, publish / max(1, total_cand or 1)),
    }

    return {
        "document_queue": {
            "incoming": doc_incoming,
            "processing": doc_processing,
            "processed": doc_processed,
            "depth": doc_incoming + doc_processing,
        },
        "candidate_queue": {
            "pending": cand_pending,
            "approved": cand_approved,
            "rejected": cand_rejected,
            "depth": cand_pending,
        },
        "publish_queue": {
            "depth": publish,
        },
        "starvation": starvation,
        "rebalance": rebalance,
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
    """Decide automatic publish vs manual review queue.

    Auto when: confidence ≥ threshold, validation passed, no duplicate,
    relationships complete, provenance present.
    Manual when: low confidence, ambiguous relationship, entity conflict,
    missing provenance.
    """
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

    auto = (
        validation_passed
        and not is_duplicate
        and has_provenance
        and not entity_conflict
        and not relationship_ambiguous
        and conf >= confidence_threshold
        and relationship_complete
    )
    # Medium band: validated but below auto threshold → manual
    if not auto and validation_passed and not is_duplicate and has_provenance:
        if conf >= MANUAL_REVIEW_CONFIDENCE:
            return {
                "action": "manual_review",
                "auto_publish": False,
                "reasons": reasons or ["confidence_requires_review"],
                "confidence": conf,
            }
    if auto:
        return {
            "action": "auto_publish",
            "auto_publish": True,
            "reasons": [],
            "confidence": conf,
        }
    return {
        "action": "manual_review" if validation_passed else "reject",
        "auto_publish": False,
        "reasons": reasons or ["gated"],
        "confidence": conf,
    }


def avg_connector_latency(connector_rows: list[dict[str, Any]]) -> float:
    vals = [float(c.get("elapsed_ms") or 0) for c in connector_rows if c.get("elapsed_ms")]
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
        row["min_ms"] = ms if row["min_ms"] is None else min(float(row["min_ms"]), ms)
        row["avg_ms"] = round(float(row["total_ms"]) / int(row["count"]), 2)
        if meta:
            row["meta"] = meta
        self.stages[name] = row
        return round(ms, 2)

    def record_queue_wait(self, queue: str, ms: float) -> None:
        self.queue_wait_ms[queue] = float(self.queue_wait_ms.get(queue) or 0) + float(ms)

    def snapshot(self) -> dict[str, Any]:
        return {
            "stages": self.stages,
            "queue_wait_ms": self.queue_wait_ms,
            "idle_ms": self.idle_ms,
        }


def _parse_ts(s: str | None) -> Optional[datetime]:
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None


def collect_real_production_stats(repo_root: Path | None = None) -> dict[str, Any]:
    """Aggregate real sessions, traces, queues, connector stats — no simulation."""
    root = repo_root or find_repo_root()
    sessions: list[dict[str, Any]] = []
    sessions_root = root / "automation" / "sessions"
    if sessions_root.exists():
        for day in sorted(sessions_root.iterdir(), reverse=True):
            if not day.is_dir():
                continue
            for f in day.glob("SESSION-*.json"):
                try:
                    sessions.append(json.loads(f.read_text(encoding="utf-8")))
                except Exception:  # noqa: BLE001
                    continue
            if len(sessions) > 300:
                break

    traces: list[dict[str, Any]] = []
    prod = root / "reports" / "production"
    if prod.exists():
        for f in prod.glob("production_trace_*.json"):
            try:
                traces.append(json.loads(f.read_text(encoding="utf-8")))
            except Exception:  # noqa: BLE001
                continue

    acq: dict[str, Any] = {}
    ap = root / "automation" / "learning" / "state" / "acquisition_performance.json"
    if ap.exists():
        try:
            acq = json.loads(ap.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            acq = {}

    src_perf = _source_perf(root)
    queues = measure_queues(root)

    # Session aggregates
    total_rows = sum(int(s.get("knowledge_added") or 0) for s in sessions)
    durs = [float(s.get("duration_seconds") or 0) for s in sessions]
    avg_dur = (sum(durs) / len(durs)) if durs else 0.0
    max_dur = max(durs) if durs else 0.0
    sessions_with_rows = [s for s in sessions if int(s.get("knowledge_added") or 0) > 0]
    rows_per_session = (
        sum(int(s.get("knowledge_added") or 0) for s in sessions_with_rows)
        / max(1, len(sessions_with_rows))
        if sessions_with_rows
        else 0.0
    )

    # Trace aggregates (real discovery → process ratio)
    disc = 0
    down = 0
    rows_tr = 0
    stage_durs: dict[str, list[float]] = {}
    for t in traces:
        disc += int(t.get("documents_discovered") or (t.get("summary") or {}).get("documents_discovered") or 0)
        down += int(t.get("documents_downloaded") or (t.get("summary") or {}).get("documents_downloaded") or 0)
        rows_tr += int(t.get("rows_published") or (t.get("summary") or {}).get("rows_published") or 0)
        for st in t.get("stages") or []:
            name = str(st.get("name") or st.get("stage") or "unknown")
            ms = float(st.get("duration_ms") or st.get("elapsed_ms") or 0)
            if ms > 0:
                stage_durs.setdefault(name, []).append(ms)

    process_ratio = (down / disc) if disc else 0.0
    thr = (acq.get("throughput") or {}) if acq else {}
    connectors = acq.get("connectors") or []
    avg_lat = avg_connector_latency(connectors) if connectors else 0.0
    for c in connectors:
        if not avg_lat and c.get("elapsed_ms"):
            avg_lat = float(c["elapsed_ms"])

    # Worker utilization estimate from last run
    elapsed_s = float(acq.get("elapsed_seconds") or 0) or 1.0
    workers_used = int((acq.get("downloads") or {}).get("max_workers") or 6)
    busy_ratio = min(1.0, (down * 2.0) / max(1.0, elapsed_s * workers_used))

    # Connector ranking by ROI
    connector_rank: list[dict[str, Any]] = []
    for sid, p in src_perf.items():
        attempts = max(1, int(p.get("attempts") or 1))
        docs = int(p.get("documents_yielded") or 0)
        rows = int(p.get("rows_yielded") or 0)
        lat = float(p.get("avg_latency_ms") or 0)
        dups = int(p.get("duplicates") or 0)
        success = float(p.get("success_rate") or 0)
        # ROI: rows per second of connector time, quality-adjusted
        hours = (lat * attempts) / 3_600_000.0 if lat else 0.001
        docs_h = docs / max(hours, 0.0001)
        rows_h = rows / max(hours, 0.0001)
        cost = lat * attempts  # ms proxy
        bandwidth = docs  # proxy
        conf = float(p.get("avg_confidence") or 0.85)
        roi = (rows * conf * success) / max(1.0, (lat / 1000.0) * attempts + dups * 0.5)
        connector_rank.append(
            {
                "source_id": sid,
                "yield_docs": docs,
                "yield_rows": rows,
                "confidence": conf,
                "latency_ms": lat,
                "duplicates": dups,
                "success_rate": success,
                "cost_ms": round(cost, 1),
                "bandwidth_docs": bandwidth,
                "documents_per_hour": round(docs_h, 2),
                "rows_per_hour": round(rows_h, 2),
                "roi": round(roi, 4),
            }
        )
    connector_rank.sort(key=lambda r: float(r["roi"]), reverse=True)

    # Top mission from sessions
    mission_counts: dict[str, int] = {}
    for s in sessions:
        m = str(s.get("mission") or "unknown")
        mission_counts[m] = mission_counts.get(m, 0) + int(s.get("knowledge_added") or 0)
    top_mission = max(mission_counts.items(), key=lambda x: x[1])[0] if mission_counts else "—"

    stage_summary: dict[str, Any] = {}
    for name, vals in stage_durs.items():
        stage_summary[name] = {
            "count": len(vals),
            "avg_ms": round(sum(vals) / len(vals), 2),
            "max_ms": round(max(vals), 2),
            "total_ms": round(sum(vals), 2),
        }

    # Bottleneck = stage with highest avg when present; else inferred from process ratio
    bottleneck = "document_download"
    if stage_summary:
        bottleneck = max(stage_summary.items(), key=lambda x: float(x[1]["avg_ms"]))[0]
    elif process_ratio < TARGET_PROCESS_RATIO:
        bottleneck = "process_budget_limit"
    elif disc == 0:
        bottleneck = "discovery"

    auto_pub = acq.get("publish") or {}
    auto_n = int(auto_pub.get("published") or 0)
    manual_n = int(auto_pub.get("queued") or 0) - auto_n
    if manual_n < 0:
        manual_n = int(auto_pub.get("skipped") or 0)

    return {
        "generated_at": utc_now_iso(),
        "sessions": {
            "count": len(sessions),
            "total_rows": total_rows,
            "avg_duration_s": round(avg_dur, 3),
            "max_duration_s": round(max_dur, 3),
            "rows_per_session": round(rows_per_session, 3),
            "sessions_with_rows": len(sessions_with_rows),
        },
        "traces": {
            "count": len(traces),
            "documents_discovered": disc,
            "documents_processed": down,
            "rows_published": rows_tr,
            "process_ratio": round(process_ratio, 4),
            "process_ratio_pct": round(process_ratio * 100, 1),
            "target_process_ratio_pct": TARGET_PROCESS_RATIO * 100,
        },
        "throughput": {
            "documents_per_hour": thr.get("documents_per_hour") or 0,
            "rows_per_hour": thr.get("rows_per_hour") or 0,
            "documents": thr.get("documents") or down,
            "rows": thr.get("rows") or rows_tr,
            "elapsed_seconds": acq.get("elapsed_seconds"),
        },
        "workers": {
            "configured": workers_used,
            "adaptive_recommended": adaptive_workers(avg_lat),
            "avg_connector_latency_ms": round(avg_lat, 1),
            "utilization_est": round(busy_ratio, 3),
            "idle_fraction_est": round(max(0.0, 1.0 - busy_ratio), 3),
        },
        "stages": stage_summary,
        "bottleneck": bottleneck,
        "queues": queues,
        "connectors_ranked": connector_rank,
        "top_connector": (connector_rank[0]["source_id"] if connector_rank else "—"),
        "top_source": (connector_rank[0]["source_id"] if connector_rank else "—"),
        "top_mission": top_mission[:80],
        "extraction": acq.get("extraction") or {},
        "publish_policy": {
            "auto_publish_confidence": AUTO_PUBLISH_CONFIDENCE,
            "manual_review_floor": MANUAL_REVIEW_CONFIDENCE,
            "last_published": auto_n,
            "last_manual_or_skipped": max(0, manual_n),
        },
        "acquisition_snapshot": {
            "session_id": acq.get("session_id"),
            "mission_id": acq.get("mission_id"),
            "connectors": len(connectors),
            "downloads": acq.get("downloads") or {},
            "cache": acq.get("cache") or {},
        },
    }


def write_throughput_reports(
    stats: dict[str, Any] | None = None,
    *,
    repo_root: Path | None = None,
    session_perf: Optional[dict[str, Any]] = None,
) -> dict[str, str]:
    """Write all Phase 1/6/10 performance reports from real production stats."""
    root = repo_root or find_repo_root()
    out = root / "reports" / "performance"
    out.mkdir(parents=True, exist_ok=True)
    s = stats or collect_real_production_stats(root)
    if session_perf:
        # merge latest session stage timings
        stages = (session_perf.get("stage_timings") or {})
        if stages:
            s = dict(s)
            s["session_stage_timings"] = stages
            s["session_workers"] = session_perf.get("workers")
            s["session_process_ratio"] = session_perf.get("process_ratio")
            s["session_extraction"] = session_perf.get("extraction")
            s["session_auto_publish"] = session_perf.get("auto_publish")

    written: dict[str, str] = {}

    def w(name: str, body: str) -> None:
        p = out / name
        p.write_text(body.rstrip() + "\n", encoding="utf-8", newline="\n")
        written[name] = str(p.relative_to(root))

    thr = s.get("throughput") or {}
    tr = s.get("traces") or {}
    sess = s.get("sessions") or {}
    wrk = s.get("workers") or {}
    q = s.get("queues") or {}
    stages = s.get("stages") or s.get("session_stage_timings") or {}
    ranked = s.get("connectors_ranked") or []
    ext = s.get("session_extraction") or s.get("extraction") or {}
    pub = s.get("session_auto_publish") or s.get("publish_policy") or {}

    # --- pipeline_bottleneck.md ---
    blines = [
        "# Pipeline Bottleneck Analysis",
        "",
        f"**Generated:** {s.get('generated_at')}",
        f"**Primary bottleneck:** `{s.get('bottleneck')}`",
        "",
        "Measured from real production sessions and acquisition traces only.",
        "",
        "## Stage durations",
        "",
        "| Stage | Count | Avg ms | Max ms | Total ms |",
        "|-------|------:|-------:|-------:|---------:|",
    ]
    if isinstance(stages, dict):
        for name, st in stages.items():
            if not isinstance(st, dict):
                continue
            blines.append(
                f"| {name} | {st.get('count', 1)} | {st.get('avg_ms', st.get('total_ms', 0))} | "
                f"{st.get('max_ms', 0)} | {st.get('total_ms', 0)} |"
            )
    if len(blines) == 10:
        blines.append("| — | 0 | 0 | 0 | 0 |")
    blines += [
        "",
        "## End-to-end funnel",
        "",
        "| Metric | Value |",
        "|--------|------:|",
        f"| Documents discovered | {tr.get('documents_discovered', 0)} |",
        f"| Documents processed | {tr.get('documents_processed', 0)} |",
        f"| Process ratio | {tr.get('process_ratio_pct', 0)}% (target ≥{tr.get('target_process_ratio_pct', 90)}%) |",
        f"| Rows published (traces) | {tr.get('rows_published', 0)} |",
        f"| Sessions observed | {sess.get('count', 0)} |",
        f"| Avg session duration (s) | {sess.get('avg_duration_s', 0)} |",
        f"| Max session duration (s) | {sess.get('max_duration_s', 0)} |",
        f"| Rows / session (productive) | {sess.get('rows_per_session', 0)} |",
        f"| Avg connector latency (ms) | {wrk.get('avg_connector_latency_ms', 0)} |",
        f"| Worker utilization (est) | {wrk.get('utilization_est', 0)} |",
        f"| Idle fraction (est) | {wrk.get('idle_fraction_est', 0)} |",
        f"| Queue wait (doc depth) | {(q.get('document_queue') or {}).get('depth', 0)} |",
        "",
        "## Bottleneck notes",
        "",
        f"- Historical process ratio **{tr.get('process_ratio_pct', 0)}%** vs target **≥90%**.",
        "- Primary levers: per-session document budget, concurrent downloads, prioritization.",
        "- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.",
        "",
    ]
    w("pipeline_bottleneck.md", "\n".join(blines))

    # --- source_efficiency.md ---
    slines = [
        "# Source Efficiency / Connector ROI",
        "",
        f"**Generated:** {s.get('generated_at')}",
        "",
        "Ranked by real yield · confidence · latency · duplicates · cost proxy.",
        "",
        "| Rank | Source | Yield docs | Yield rows | Conf | Latency ms | Dups | Docs/h | Rows/h | ROI |",
        "|-----:|--------|----------:|-----------:|-----:|-----------:|-----:|-------:|-------:|----:|",
    ]
    for i, r in enumerate(ranked[:25], 1):
        slines.append(
            f"| {i} | {r.get('source_id')} | {r.get('yield_docs')} | {r.get('yield_rows')} | "
            f"{r.get('confidence')} | {r.get('latency_ms')} | {r.get('duplicates')} | "
            f"{r.get('documents_per_hour')} | {r.get('rows_per_hour')} | {r.get('roi')} |"
        )
    if not ranked:
        slines.append("| — | — | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |")
    slines += [
        "",
        f"**Top ROI source:** `{s.get('top_source')}`",
        "",
        "Highest-ROI connectors are preferred first in adaptive mission source selection.",
        "",
    ]
    w("source_efficiency.md", "\n".join(slines))

    # --- production_capacity.md ---
    rph = float(thr.get("rows_per_hour") or 0)
    dph = float(thr.get("documents_per_hour") or 0)
    w(
        "production_capacity.md",
        "\n".join(
            [
                "# Production Capacity",
                "",
                f"**Generated:** {s.get('generated_at')}",
                "",
                "| Metric | Value |",
                "|--------|------:|",
                f"| Rows/hour (last acquisition) | {rph} |",
                f"| Docs/hour (last acquisition) | {dph} |",
                f"| Projected rows/night (12h × rph) | {round(rph * 12, 1)} |",
                f"| Sessions observed | {sess.get('count', 0)} |",
                f"| Total rows (sessions) | {sess.get('total_rows', 0)} |",
                f"| Rows/session | {sess.get('rows_per_session', 0)} |",
                f"| Process ratio | {tr.get('process_ratio_pct', 0)}% |",
                f"| Target process ratio | ≥{tr.get('target_process_ratio_pct', 90)}% |",
                f"| Target rows/night | ≥50 |",
                "",
            ]
        ),
    )

    # --- throughput_report.md ---
    w(
        "throughput_report.md",
        "\n".join(
            [
                "# Throughput Report",
                "",
                f"**Generated:** {s.get('generated_at')}",
                "",
                "| Metric | Value |",
                "|--------|------:|",
                f"| Documents (last run) | {thr.get('documents', 0)} |",
                f"| Rows (last run) | {thr.get('rows', 0)} |",
                f"| Documents/hour | {dph} |",
                f"| Rows/hour | {rph} |",
                f"| Elapsed seconds | {thr.get('elapsed_seconds', 0)} |",
                f"| Knowledge growth velocity (rows/session) | {sess.get('rows_per_session', 0)} |",
                f"| Production efficiency (rows/doc) | {round((thr.get('rows') or 0) / max(1, thr.get('documents') or 1), 3)} |",
                f"| LLM skipped | {ext.get('skipped_llm', ext.get('llm_skipped', '—'))} |",
                f"| LLM used | {ext.get('llm', ext.get('llm_used', 0))} |",
                f"| Avg extraction time (ms) | {ext.get('avg_ms', ext.get('average_extraction_ms', '—'))} |",
                "",
            ]
        ),
    )

    # --- worker_utilization.md ---
    w(
        "worker_utilization.md",
        "\n".join(
            [
                "# Worker Utilization",
                "",
                f"**Generated:** {s.get('generated_at')}",
                "",
                "| Metric | Value |",
                "|--------|------:|",
                f"| Configured workers (last) | {wrk.get('configured', 0)} |",
                f"| Adaptive recommended | {wrk.get('adaptive_recommended', 0)} |",
                f"| Avg connector latency (ms) | {wrk.get('avg_connector_latency_ms', 0)} |",
                f"| Utilization (est) | {wrk.get('utilization_est', 0)} |",
                f"| Idle fraction (est) | {wrk.get('idle_fraction_est', 0)} |",
                "",
                "Adaptive ladder: 2 → 4 → 8 → 16 workers based on connector latency.",
                "",
                f"Session workers: `{s.get('session_workers')}`",
                "",
            ]
        ),
    )

    # --- connector_ranking.md ---
    clines = [
        "# Connector Ranking",
        "",
        f"**Generated:** {s.get('generated_at')}",
        "",
        "| Rank | Connector/Source | ROI | Rows/h | Docs/h | Latency | Success |",
        "|-----:|------------------|----:|-------:|-------:|--------:|--------:|",
    ]
    for i, r in enumerate(ranked[:20], 1):
        clines.append(
            f"| {i} | {r.get('source_id')} | {r.get('roi')} | {r.get('rows_per_hour')} | "
            f"{r.get('documents_per_hour')} | {r.get('latency_ms')} | {r.get('success_rate')} |"
        )
    if not ranked:
        clines.append("| — | — | 0 | 0 | 0 | 0 | 0 |")
    clines.append("")
    w("connector_ranking.md", "\n".join(clines))

    # --- session_efficiency.md ---
    w(
        "session_efficiency.md",
        "\n".join(
            [
                "# Session Efficiency",
                "",
                f"**Generated:** {s.get('generated_at')}",
                "",
                "| Metric | Value |",
                "|--------|------:|",
                f"| Sessions | {sess.get('count', 0)} |",
                f"| Sessions with rows | {sess.get('sessions_with_rows', 0)} |",
                f"| Total rows | {sess.get('total_rows', 0)} |",
                f"| Avg duration (s) | {sess.get('avg_duration_s', 0)} |",
                f"| Max duration (s) | {sess.get('max_duration_s', 0)} |",
                f"| Rows/session | {sess.get('rows_per_session', 0)} |",
                f"| Top mission | {s.get('top_mission')} |",
                "",
                "Mission density: hourly `learn.yml` + non-overlapping concurrency.",
                "Throughput gains use idle window capacity by processing more docs per session.",
                "",
            ]
        ),
    )

    # --- queue_efficiency.md ---
    dq = q.get("document_queue") or {}
    cq = q.get("candidate_queue") or {}
    pq = q.get("publish_queue") or {}
    starvation = q.get("starvation") or []
    rebalance = q.get("rebalance") or {}
    w(
        "queue_efficiency.md",
        "\n".join(
            [
                "# Queue Efficiency",
                "",
                f"**Generated:** {s.get('generated_at')}",
                "",
                "## Depths",
                "",
                "| Queue | Metric | Value |",
                "|-------|--------|------:|",
                f"| Document | incoming | {dq.get('incoming', 0)} |",
                f"| Document | processing | {dq.get('processing', 0)} |",
                f"| Document | processed | {dq.get('processed', 0)} |",
                f"| Document | depth | {dq.get('depth', 0)} |",
                f"| Candidate | pending | {cq.get('pending', 0)} |",
                f"| Candidate | approved | {cq.get('approved', 0)} |",
                f"| Candidate | rejected | {cq.get('rejected', 0)} |",
                f"| Publish | depth | {pq.get('depth', 0)} |",
                "",
                "## Starvation / imbalance",
                "",
                *(
                    [f"- `{x}`" for x in starvation]
                    if starvation
                    else ["- None detected"]
                ),
                "",
                "## Rebalance signals",
                "",
                "```json",
                json.dumps(rebalance, indent=2),
                "```",
                "",
            ]
        ),
    )

    # --- factory_capacity.md ---
    w(
        "factory_capacity.md",
        "\n".join(
            [
                "# Factory Capacity",
                "",
                f"**Generated:** {s.get('generated_at')}",
                "",
                "| Dimension | Value |",
                "|-----------|------:|",
                f"| Rows/hour | {rph} |",
                f"| Docs/hour | {dph} |",
                f"| Rows/session | {sess.get('rows_per_session', 0)} |",
                f"| Top connector | {s.get('top_connector')} |",
                f"| Top source | {s.get('top_source')} |",
                f"| Top mission | {s.get('top_mission')} |",
                f"| Avg connector latency (ms) | {wrk.get('avg_connector_latency_ms', 0)} |",
                f"| Worker utilization | {wrk.get('utilization_est', 0)} |",
                f"| Document queue depth | {dq.get('depth', 0)} |",
                f"| Candidate queue depth | {cq.get('depth', 0)} |",
                f"| Publish queue depth | {pq.get('depth', 0)} |",
                f"| Process ratio | {tr.get('process_ratio_pct', 0)}% |",
                f"| Knowledge growth velocity | {sess.get('rows_per_session', 0)} rows/productive session |",
                f"| Production efficiency | {round((thr.get('rows') or 0) / max(1, thr.get('documents') or 1), 3)} rows/doc |",
                f"| Auto-publish confidence gate | {pub.get('auto_publish_confidence', AUTO_PUBLISH_CONFIDENCE)} |",
                f"| Automatic publish (last) | {pub.get('last_published', pub.get('auto_publish_count', '—'))} |",
                f"| Manual review (last) | {pub.get('last_manual_or_skipped', pub.get('manual_review_count', '—'))} |",
                "",
                "## Success targets",
                "",
                "| Target | Status basis |",
                "|--------|--------------|",
                "| ≥50 rows/night | Use rows/hour × overnight window after optimization |",
                "| ≥90% docs processed | Process budget + priority queue |",
                "| Maximize scheduler utilization | More work per non-overlapping hourly slot |",
                "| 0 rejects (quality) | Integrity guard + provenance retained |",
                "| Confidence ≥92% | Auto-publish gate |",
                "",
            ]
        ),
    )

    # Persist stats JSON for dashboard consumers
    state_path = (
        root / "automation" / "learning" / "state" / "throughput_stats.json"
    )
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps(s, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    written["throughput_stats.json"] = str(
        state_path.relative_to(root)
    )

    return written
