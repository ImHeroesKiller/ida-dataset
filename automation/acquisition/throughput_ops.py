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

# Auto-publish confidence — lowered so free DDG multi-table fill can land rows
# (still requires provenance + validation; quality gate remains in integrity)
AUTO_PUBLISH_CONFIDENCE = 0.55
MANUAL_REVIEW_CONFIDENCE = 0.40

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
    chosen = allowed[0] if allowed else 2
    for w in allowed:
        if w <= n:
            chosen = w
    return chosen


def process_budget(
    discovered: int,
    processed: int,
    *,
    target_ratio: float = TARGET_PROCESS_RATIO,
) -> dict[str, Any]:
    """Return budget signal for process ratio."""
    d = max(0, int(discovered or 0))
    p = max(0, int(processed or 0))
    ratio = (p / d) if d else 1.0
    deficit = max(0, int(math.ceil(d * target_ratio) - p))
    return {
        "discovered": d,
        "processed": p,
        "ratio": round(ratio, 4),
        "target_ratio": target_ratio,
        "deficit": deficit,
        "healthy": ratio >= target_ratio * 0.85,
    }


def measure_queues(repo_root: Path | None = None) -> dict[str, Any]:
    """Count queue depths from real directories only."""
    root = Path(repo_root) if repo_root else find_repo_root()

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
    confidence: Any,
    *,
    has_provenance: bool = True,
    schema_ok: bool = True,
    confidence_threshold: float = AUTO_PUBLISH_CONFIDENCE,
) -> dict[str, Any]:
    """Decide auto-publish vs manual review vs reject."""
    conf: Optional[float] = None
    try:
        if confidence is not None and confidence != "":
            conf = float(confidence)
            if conf > 1.0:
                conf = conf / 100.0
    except (TypeError, ValueError):
        conf = None

    if not schema_ok:
        return {"action": "reject", "reason": "schema_mismatch", "confidence": conf}
    if not has_provenance:
        return {"action": "reject", "reason": "missing_provenance", "confidence": conf}
    if conf is None:
        return {"action": "review", "reason": "confidence_unknown", "confidence": conf}
    if conf >= confidence_threshold:
        return {"action": "publish", "reason": "auto_publish", "confidence": conf}
    if conf >= MANUAL_REVIEW_CONFIDENCE:
        return {"action": "review", "reason": "below_auto_threshold", "confidence": conf}
    return {"action": "reject", "reason": "confidence_too_low", "confidence": conf}


def prioritize_search_results(
    results: list[dict[str, Any]],
    *,
    max_items: int = 50,
) -> list[dict[str, Any]]:
    """Stable rank by score/trust when present."""
    def key(r: dict[str, Any]) -> tuple:
        score = 0.0
        for k in ("score", "trust_score", "relevance", "rank"):
            v = r.get(k)
            try:
                if v is not None and v != "":
                    score = float(v)
                    break
            except (TypeError, ValueError):
                pass
        return (-score, str(r.get("url") or ""))

    ranked = sorted(list(results or []), key=key)
    return ranked[: max(1, int(max_items))]


class StageTimer:
    """Per-stage duration tracking for bottleneck analysis."""

    def __init__(self) -> None:
        self._starts: dict[str, float] = {}
        self._durations_ms: dict[str, float] = {}
        self._meta: dict[str, Any] = {}
        self._queue_waits: dict[str, list[float]] = {}

    def start(self, name: str) -> None:
        self._starts[name] = time.perf_counter()

    def stop(self, name: str, *, meta: Optional[dict[str, Any]] = None) -> float:
        t0 = self._starts.pop(name, None)
        if t0 is None:
            return 0.0
        ms = (time.perf_counter() - t0) * 1000.0
        self._durations_ms[name] = self._durations_ms.get(name, 0.0) + ms
        if meta:
            self._meta[name] = meta
        return ms

    def record_queue_wait(self, queue: str, ms: float) -> None:
        self._queue_waits.setdefault(queue, []).append(float(ms))

    def snapshot(self) -> dict[str, Any]:
        return {
            "durations_ms": dict(self._durations_ms),
            "meta": dict(self._meta),
            "queue_waits_ms": {k: list(v) for k, v in self._queue_waits.items()},
            "captured_at": utc_now_iso(),
        }


def avg_connector_latency(connector_rows: list[dict[str, Any]]) -> float:
    vals: list[float] = []
    for r in connector_rows or []:
        for k in ("latency_ms", "avg_latency_ms", "duration_ms"):
            v = r.get(k)
            try:
                if v is not None and v != "":
                    vals.append(float(v))
                    break
            except (TypeError, ValueError):
                pass
    return sum(vals) / len(vals) if vals else 0.0


def collect_real_production_stats(repo_root: Path | None = None) -> dict[str, Any]:
    """Lightweight production stats from filesystem state only."""
    root = Path(repo_root) if repo_root else find_repo_root()
    queues = measure_queues(root)
    return {
        "queues": queues,
        "publish": {
            "auto_publish_confidence": AUTO_PUBLISH_CONFIDENCE,
            "manual_review_floor": MANUAL_REVIEW_CONFIDENCE,
        },
        "collected_at": utc_now_iso(),
        "repo_root": str(root),
    }


def write_throughput_reports(
    repo_root: Path | None = None,
    *,
    stats: Optional[dict[str, Any]] = None,
) -> dict[str, str]:
    """Write throughput JSON/MD under reports/ when possible; never raises hard."""
    root = Path(repo_root) if repo_root else find_repo_root()
    out_dir = root / "reports" / "throughput"
    written: dict[str, str] = {}
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        payload = stats or collect_real_production_stats(root)
        js = out_dir / "throughput_stats.json"
        js.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        written["throughput_stats.json"] = str(js.relative_to(root))
        md = out_dir / "throughput_summary.md"
        pub = (payload.get("publish") or {}) if isinstance(payload, dict) else {}
        lines = [
            "# Throughput summary",
            "",
            f"- Collected: {payload.get('collected_at') if isinstance(payload, dict) else ''}",
            f"- Auto-publish confidence gate: {pub.get('auto_publish_confidence', AUTO_PUBLISH_CONFIDENCE)}",
            f"- Manual review floor: {pub.get('manual_review_floor', MANUAL_REVIEW_CONFIDENCE)}",
            "",
        ]
        md.write_text("\n".join(lines), encoding="utf-8", newline="\n")
        written["throughput_summary.md"] = str(md.relative_to(root))
    except Exception:
        pass
    return written
