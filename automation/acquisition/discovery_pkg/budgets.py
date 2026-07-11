"""Adaptive discovery / download / extract / publish budgets.

No arbitrary session caps (5/10/20/50). Budgets scale from:
  mission priority · knowledge gap · queue health · provider health ·
  worker capacity · available runtime · provider rate limits only.
"""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from typing import Any, Optional


@dataclass
class AdaptiveBudgets:
    """Session budgets derived from live factory signals (not constants)."""

    # Discovery
    query_budget: int
    url_budget: int
    per_provider_results: int
    feed_source_budget: int
    domain_budget: int
    max_provider_rounds: int
    runtime_budget_s: float

    # Downstream
    download_budget: int
    extraction_budget: int
    publish_budget: int
    source_select_budget: int
    worker_capacity: int

    # Signals used (observability)
    gap_score: float
    gap_rows: Optional[float]
    coverage_pct: Optional[float]
    mission_priority: str
    queue_pressure: float
    providers_active: int
    providers_misconfigured: int
    stop_policy: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _clamp_int(n: float, lo: int, hi: int) -> int:
    return max(lo, min(hi, int(n)))


def _priority_weight(priority: str | None, gap_score: float) -> float:
    p = (priority or "").lower()
    if p in {"critical", "p0"} or gap_score >= 80:
        return 1.35
    if p in {"high", "bootstrap"} or gap_score >= 40:
        return 1.15
    if p in {"low"}:
        return 0.85
    return 1.0


def gap_boost_factor(gap_score: float, priority_weight: float) -> float:
    return priority_weight * (1.0 + min(1.5, max(0.0, float(gap_score or 0)) / 80.0))


def compute_adaptive_budgets(
    *,
    knowledge_gap: Optional[dict[str, Any]] = None,
    queue_health: Optional[dict[str, Any]] = None,
    providers_active: int = 0,
    providers_misconfigured: int = 0,
    providers_total: int = 0,
    worker_capacity: int = 4,
    runtime_budget_s: float | None = None,
    policy_max_documents: int | None = None,
    policy_max_per_session: int | None = None,
    trusted_domain_count: int = 0,
    avg_provider_latency_ms: float = 0.0,
) -> AdaptiveBudgets:
    """Compute budgets that grow with real knowledge demand.

    Ceiling only comes from:
    - optional policy safety rails (when explicitly configured)
    - runtime budget
    - provider rate-limit-friendly batch sizes
    Never from hard-coded 5/10/20/50 document caps.
    """
    gap = knowledge_gap or {}
    queues = queue_health or {}

    gap_score = float(gap.get("knowledge_gap_score") or 0)
    try:
        gap_rows = float(gap["gap_rows"]) if gap.get("gap_rows") is not None else None
    except (TypeError, ValueError):
        gap_rows = None
    try:
        coverage_pct = (
            float(gap["coverage_pct"]) if gap.get("coverage_pct") is not None else None
        )
    except (TypeError, ValueError):
        coverage_pct = None
    priority = str(gap.get("priority") or "medium")
    pw = _priority_weight(priority, gap_score)

    # Queue pressure 0..1 — high backlog slightly favors processing over fan-out
    dq = (queues.get("document_queue") or {}).get("depth") or 0
    cq = (queues.get("candidate_queue") or {}).get("depth") or 0
    pq = (queues.get("publish_queue") or {}).get("depth") or 0
    queue_pressure = min(1.0, (float(dq) * 0.4 + float(cq) * 0.4 + float(pq) * 0.2) / 40.0)

    active = max(0, int(providers_active))
    misconf = max(0, int(providers_misconfigured))
    total_p = max(active + misconf, int(providers_total) or (active + misconf), 1)
    workers = max(1, int(worker_capacity or 1))

    # Runtime: scale with gap & active providers; bound by practical session windows
    lat = max(0.0, float(avg_provider_latency_ms or 0))
    if runtime_budget_s is None or runtime_budget_s <= 0:
        # ~3–8 min discovery window (not infinite crawl)
        base_rt = 180.0 * pw + min(240.0, active * 25.0) + min(120.0, gap_score)
        if lat > 5000:
            base_rt *= 0.75
        elif lat > 2000:
            base_rt *= 0.9
        if queue_pressure > 0.7:
            base_rt *= 0.85
        runtime_budget_s = max(90.0, min(600.0, base_rt))
    rt = float(runtime_budget_s)

    # Domain / query scale with registry size and gap — not a fixed 16
    domains = max(1, int(trusted_domain_count or 1))
    # Aim: cover most trusted domains when gap is large
    domain_frac = 0.55 + min(0.45, gap_score / 200.0)
    domain_budget = _clamp_int(math.ceil(domains * domain_frac * pw), 1, domains)

    # ~2 queries per domain (site + intitle/open) when gap high
    queries_per_domain = 2.0 if gap_score >= 30 else 1.5
    query_budget = _clamp_int(
        math.ceil(domain_budget * queries_per_domain * pw * (1.0 - 0.15 * queue_pressure)),
        domain_budget,
        max(domain_budget * 3, domains * 2),
    )

    # Per-provider result page size — only capped by typical provider API max (≤20)
    per_provider_results = 10 if gap_score < 25 else (15 if gap_score < 80 else 20)

    # Download budget first (policy rails) — URL budget fans out above it for filter loss
    download_raw = int(math.ceil(workers * 10 * gap_boost_factor(gap_score, pw)))
    if gap_rows is not None and gap_rows > 0:
        download_raw = max(download_raw, int(min(gap_rows * 0.02, 400) * pw))
    elif gap_score > 0:
        download_raw = max(download_raw, int(40 * pw + gap_score * 0.8))

    if policy_max_per_session is not None and policy_max_per_session > 0:
        session_ceil = max(
            int(policy_max_per_session),
            int(policy_max_per_session * pw * (1.0 + min(1.0, gap_score / 100.0))),
        )
        if policy_max_documents is not None and policy_max_documents > 0:
            session_ceil = min(session_ceil, int(policy_max_documents))
        download_budget = min(download_raw, session_ceil)
    elif policy_max_documents is not None and policy_max_documents > 0:
        download_budget = min(download_raw, int(policy_max_documents))
    else:
        download_budget = download_raw

    # URL budget: enough candidates for trusted-filter loss (~3–5× downloads),
    # plus multi-provider fan-out — never a fixed 20/30 cap
    filter_fanout = 4.0 if active >= 3 else 3.0
    url_budget = max(
        int(download_budget * filter_fanout),
        domain_budget * per_provider_results,
        workers * 16,
    )
    # Soft runtime-linked ceiling (prevents pathological queues, not a doc-count stop)
    runtime_url_cap = int(max(120, rt * max(0.5, active * 0.4)))
    url_budget = min(url_budget, max(runtime_url_cap, download_budget * 3))

    feed_source_budget = domain_budget

    max_provider_rounds = max(1, int(math.ceil(query_budget / max(1, domain_budget))))

    extraction_budget = download_budget
    publish_budget = download_budget

    source_select_budget = domain_budget

    stop_policy = (
        "provider_exhausted | knowledge_gap_satisfied | "
        "runtime_budget_reached | provider_quota_reached"
    )

    return AdaptiveBudgets(
        query_budget=query_budget,
        url_budget=url_budget,
        per_provider_results=per_provider_results,
        feed_source_budget=feed_source_budget,
        domain_budget=domain_budget,
        max_provider_rounds=max_provider_rounds,
        runtime_budget_s=rt,
        download_budget=download_budget,
        extraction_budget=extraction_budget,
        publish_budget=publish_budget,
        source_select_budget=source_select_budget,
        worker_capacity=workers,
        gap_score=gap_score,
        gap_rows=gap_rows,
        coverage_pct=coverage_pct,
        mission_priority=priority,
        queue_pressure=round(queue_pressure, 4),
        providers_active=active,
        providers_misconfigured=misconf,
        stop_policy=stop_policy,
    )


def knowledge_gap_satisfied(gap: Optional[dict[str, Any]], accepted_urls: int = 0) -> bool:
    """True only when continuous manufacturing signals no remaining universe gap.

    Does NOT stop on arbitrary document counts. Continuous mode rarely satisfies.
    """
    if not gap:
        return False
    if gap.get("continuous") and gap.get("gap_rows") is None:
        return False
    try:
        gap_rows = gap.get("gap_rows")
        if gap_rows is not None and float(gap_rows) <= 0:
            return True
        cov = gap.get("coverage_pct")
        if cov is not None and float(cov) >= 100.0 and float(gap.get("knowledge_gap_score") or 0) < 1:
            return True
    except (TypeError, ValueError):
        return False
    return False
