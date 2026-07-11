"""Discovery Layer orchestration.

Mission → Knowledge Gap → Multi-Provider Discovery → Candidate URLs → Trusted Verification

Discovery continues until:
  provider exhausted | knowledge gap satisfied | runtime budget reached | quota reached
Never stops because an arbitrary document count was hit.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Optional

from automation.acquisition.discovery_pkg.budgets import (
    AdaptiveBudgets,
    compute_adaptive_budgets,
    knowledge_gap_satisfied,
)
from automation.acquisition.discovery_pkg.cache import DiscoveryCache
from automation.acquisition.discovery_pkg.providers import build_provider
from automation.acquisition.discovery_pkg.query_engine import (
    build_discovery_queries,
    trusted_domains_from_sources,
)
from automation.acquisition.discovery_pkg.ranking import rank_providers, update_provider_yield
from automation.acquisition.discovery_pkg.registry import DiscoveryRegistry
from automation.acquisition.discovery_pkg.reputation import score_sources_for_discovery
from automation.acquisition.discovery_pkg.trusted_filter import filter_discovered_urls
from automation.acquisition.source_registry import SourceRegistry
from automation.connectors.types import SearchResult
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


def _knowledge_gap(repo_root: Path, dataset: str) -> dict[str, Any]:
    """Knowledge gap for discovery — uses manufacturing engine when available."""
    try:
        from automation.manufacturing.knowledge_gap import evaluate_dataset

        e = evaluate_dataset(dataset, repo_root=repo_root)
        return {
            "dataset": dataset,
            "current_rows": e.get("current_rows"),
            "target_rows": (e.get("profile") or {}).get("stretch_target"),
            "minimum_target": (e.get("profile") or {}).get("minimum_target"),
            "gap_rows": e.get("universe_gap"),
            "coverage_pct": e.get("coverage_stretch_pct"),
            "knowledge_gap_score": e.get("knowledge_gap_score"),
            "estimated_universe": (e.get("universe") or {}).get("estimated_universe"),
            "priority": "high"
            if float(e.get("knowledge_gap_score") or 0) > 40
            else "medium",
            "continuous": True,
        }
    except Exception:  # noqa: BLE001
        pass
    current = 0
    csv_path = repo_root / "domains" / "business_development" / f"{dataset}.csv"
    if csv_path.exists():
        try:
            current = max(0, sum(1 for _ in csv_path.open(encoding="utf-8-sig")) - 1)
        except Exception:  # noqa: BLE001
            current = 0
    return {
        "dataset": dataset,
        "current_rows": current,
        "target_rows": None,
        "gap_rows": None,
        "coverage_pct": None,
        "priority": "high",
        "continuous": True,
    }


def _policy_limits(repo_root: Path) -> dict[str, Optional[int]]:
    try:
        from automation.lib.simple_yaml import load_simple_yaml

        path = repo_root / "automation" / "config" / "policies.yaml"
        if not path.exists():
            return {}
        data = load_simple_yaml(path.read_text(encoding="utf-8")) or {}
        lim = data.get("limits") or {}
        return {
            "max_documents": int(lim["max_documents"])
            if lim.get("max_documents") is not None
            else None,
            "max_documents_per_session": int(lim["max_documents_per_session"])
            if lim.get("max_documents_per_session") is not None
            else None,
        }
    except Exception:  # noqa: BLE001
        return {}


def _discovery_policy(repo_root: Path) -> dict[str, Any]:
    """Tavily-first discovery policy (simplification sprint). Safe defaults if missing."""
    defaults: dict[str, Any] = {
        "primary_api": "tavily",
        "max_tavily_searches_per_session": 10,
        "secondary_paid_api_fallback": False,
        "free_feeds_enabled": True,
        "one_discovery_multi_dataset": True,
    }
    try:
        from automation.lib.simple_yaml import load_simple_yaml

        path = repo_root / "automation" / "config" / "policies.yaml"
        if not path.exists():
            return defaults
        data = load_simple_yaml(path.read_text(encoding="utf-8")) or {}
        disc = data.get("discovery") or {}
        if not isinstance(disc, dict):
            return defaults
        out = dict(defaults)
        if disc.get("primary_api"):
            out["primary_api"] = str(disc["primary_api"]).strip().lower()
        if disc.get("max_tavily_searches_per_session") is not None:
            out["max_tavily_searches_per_session"] = max(
                1, int(disc["max_tavily_searches_per_session"])
            )
        if "secondary_paid_api_fallback" in disc:
            out["secondary_paid_api_fallback"] = bool(disc["secondary_paid_api_fallback"])
        if "free_feeds_enabled" in disc:
            out["free_feeds_enabled"] = bool(disc["free_feeds_enabled"])
        if "one_discovery_multi_dataset" in disc:
            out["one_discovery_multi_dataset"] = bool(disc["one_discovery_multi_dataset"])
        # Registry policy block can override max searches
        reg_path = repo_root / "automation" / "config" / "discovery_registry.yaml"
        if reg_path.exists():
            reg = load_simple_yaml(reg_path.read_text(encoding="utf-8")) or {}
            reg_pol = reg.get("policy") or {}
            if isinstance(reg_pol, dict) and reg_pol.get("max_tavily_searches_per_session") is not None:
                out["max_tavily_searches_per_session"] = max(
                    1, int(reg_pol["max_tavily_searches_per_session"])
                )
        return out
    except Exception:  # noqa: BLE001
        return defaults


def _empty_provider_stat(prov: dict[str, Any], *, h: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "provider_id": str(prov.get("id")),
        "name": prov.get("name"),
        "api_type": prov.get("api_type"),
        "health": h or {},
        "queries": 0,
        "urls": 0,
        "cache_hits": 0,
        "elapsed_ms": 0.0,
        "status": prov.get("status"),
        "operational_status": prov.get("operational_status"),
        "credentials_available": prov.get("credentials_available"),
        "disable_reason": prov.get("disable_reason"),
        "exhausted": False,
        "exhaustion_reason": "",
        "rank_score": prov.get("_rank_score"),
        "utilization": 0.0,
    }


def run_discovery(
    *,
    instruction: str,
    dataset: str = "industry_library",
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_queries: int | None = None,
    max_urls: int | None = None,
    runtime_budget_s: float | None = None,
    budgets: AdaptiveBudgets | dict[str, Any] | None = None,
    log: Optional[Any] = None,
) -> dict[str, Any]:
    """Execute multi-provider discovery until adaptive stop conditions.

    Search engines never become knowledge sources.
    max_queries / max_urls are optional overrides; default is adaptive budgets.
    """
    root = repo_root or find_repo_root()
    emit = log or (lambda verb, detail: print(f"[{verb}] {detail}"))

    t0 = time.perf_counter()
    gap = _knowledge_gap(root, dataset)
    emit(
        "Knowledge Gap",
        f"{dataset}: {gap.get('current_rows')}/{gap.get('target_rows')} "
        f"({gap.get('coverage_pct')}%) gap={gap.get('gap_rows')}",
    )

    src_reg = SourceRegistry(repo_root=root)
    all_sources = src_reg.list_sources(enabled_only=False)
    enabled_sources = src_reg.list_sources(enabled_only=True)
    reputation = score_sources_for_discovery(
        enabled_sources or all_sources,
        dataset=dataset,
        repo_root=root,
    )

    disc_reg = DiscoveryRegistry(repo_root=root)
    # Full inventory for observability (never silent)
    all_providers = disc_reg.list_providers(enabled_only=False, runnable_only=False)
    active_providers = [p for p in all_providers if p.get("operational_status") == "ACTIVE"]
    misconfigured = [
        p for p in all_providers if p.get("operational_status") == "MISCONFIGURED"
    ]
    disabled = [p for p in all_providers if p.get("operational_status") == "DISABLED"]

    for p in misconfigured:
        emit(
            "Discovery Provider",
            f"MISCONFIGURED {p.get('name')}: {p.get('disable_reason')} "
            f"(not silently disabled)",
        )

    # Queue + policy for adaptive budgets
    try:
        from automation.acquisition.throughput_ops import measure_queues

        queue_health = measure_queues(root)
    except Exception:  # noqa: BLE001
        queue_health = {}
    policy = _policy_limits(root)

    if isinstance(budgets, AdaptiveBudgets):
        budget = budgets
    elif isinstance(budgets, dict) and budgets.get("url_budget"):
        budget = compute_adaptive_budgets(
            knowledge_gap=gap,
            queue_health=queue_health,
            providers_active=len(active_providers),
            providers_misconfigured=len(misconfigured),
            providers_total=len(all_providers),
            trusted_domain_count=len(reputation or all_sources),
            runtime_budget_s=runtime_budget_s,
            policy_max_documents=policy.get("max_documents"),
            policy_max_per_session=policy.get("max_documents_per_session"),
        )
        # apply dict overrides
        for k, v in budgets.items():
            if hasattr(budget, k) and v is not None:
                setattr(budget, k, v)
    else:
        budget = compute_adaptive_budgets(
            knowledge_gap=gap,
            queue_health=queue_health,
            providers_active=len(active_providers),
            providers_misconfigured=len(misconfigured),
            providers_total=len(all_providers),
            trusted_domain_count=len(reputation or all_sources),
            runtime_budget_s=runtime_budget_s,
            policy_max_documents=policy.get("max_documents"),
            policy_max_per_session=policy.get("max_documents_per_session"),
        )

    # Optional caller overrides still adaptive-floor (never shrink below demand unless explicit)
    q_budget = int(max_queries) if max_queries is not None else budget.query_budget
    url_budget = int(max_urls) if max_urls is not None else budget.url_budget
    # Prefer adaptive when override is an old small constant and gap is large
    if max_urls is not None and max_urls < budget.url_budget and float(gap.get("knowledge_gap_score") or 0) > 20:
        url_budget = budget.url_budget
    if max_queries is not None and max_queries < budget.query_budget and float(gap.get("knowledge_gap_score") or 0) > 20:
        q_budget = budget.query_budget

    domains = trusted_domains_from_sources(
        (reputation or all_sources)[: budget.domain_budget]
        if budget.domain_budget
        else (reputation or all_sources)
    )
    # If reputation shorter than domain budget, use all
    if len(domains) < budget.domain_budget:
        domains = trusted_domains_from_sources(reputation or all_sources)

    queries = build_discovery_queries(
        instruction,
        trusted_domains=domains,
        max_queries=q_budget,
    )
    emit(
        "Discovery",
        f"Adaptive budgets query={q_budget} url={url_budget} "
        f"runtime={budget.runtime_budget_s}s · {len(queries)} queries · "
        f"{len(domains)} domains · active_providers={len(active_providers)}",
    )

    # Dynamic provider ranking
    ranked_all = rank_providers(
        all_providers,
        instruction=instruction,
        dataset=dataset,
        repo_root=root,
    )
    ranked_active = [p for p in ranked_all if p.get("operational_status") == "ACTIVE"]

    cache = DiscoveryCache(repo_root=root)
    raw_candidates: list[dict[str, Any]] = []
    provider_stats_map: dict[str, dict[str, Any]] = {}
    query_stats: list[dict[str, Any]] = []

    # Seed stats for ALL providers (observability — never silent)
    for prov in ranked_all:
        pid = str(prov.get("id"))
        inst = build_provider(prov) if prov.get("operational_status") == "ACTIVE" else None
        h = inst.health() if inst else {
            "ok": False,
            "status": "offline",
            "message": prov.get("disable_reason") or prov.get("operational_status"),
        }
        provider_stats_map[pid] = _empty_provider_stat(prov, h=h)

    paid_api_types = {
        "google_cse",
        "bing",
        "brave",
        "serpapi",
        "tavily",
        "yandex",
    }
    free_index_types = {"commoncrawl", "opensearch"}
    feed_types = {"rss", "atom", "sitemap"}

    disc_policy = _discovery_policy(root)
    primary_api = str(disc_policy.get("primary_api") or "tavily")
    max_primary_searches = int(disc_policy.get("max_tavily_searches_per_session") or 10)
    secondary_fallback = bool(disc_policy.get("secondary_paid_api_fallback"))

    all_paid_api = [p for p in ranked_active if str(p.get("api_type")) in paid_api_types]
    primary_providers = [
        p for p in all_paid_api if str(p.get("api_type")) == primary_api
    ]
    secondary_paid = [
        p for p in all_paid_api if str(p.get("api_type")) != primary_api
    ]
    free_index_providers = [
        p for p in ranked_active if str(p.get("api_type")) in free_index_types
    ]
    # Tavily-first: only primary paid API by default (secondary only if policy + needed)
    api_providers = list(primary_providers)
    feed_providers = (
        [p for p in ranked_active if str(p.get("api_type")) in feed_types]
        if disc_policy.get("free_feeds_enabled", True)
        else []
    )
    trusted_site = [p for p in ranked_active if str(p.get("api_type")) == "trusted_site"]

    emit(
        "Discovery Policy",
        f"primary={primary_api} max_searches={max_primary_searches} "
        f"secondary_fallback={secondary_fallback} "
        f"primary_active={len(primary_providers)} secondary_enabled_in_registry={len(secondary_paid)}",
    )

    stop_reason = "completed"
    runtime_limit = float(budget.runtime_budget_s)
    per_results = int(budget.per_provider_results)
    # Cap query fan-out to primary search budget (one search = one live request when uncached)
    if max_primary_searches > 0 and len(queries) > max_primary_searches:
        queries = queries[:max_primary_searches]
        emit(
            "Discovery",
            f"Query list capped to {max_primary_searches} (Tavily-first session budget)",
        )

    def runtime_exceeded() -> bool:
        return (time.perf_counter() - t0) >= runtime_limit

    def unique_url_count() -> int:
        return len({str(c.get("url") or "").lower() for c in raw_candidates if c.get("url")})

    def remaining_s() -> float:
        return max(0.0, runtime_limit - (time.perf_counter() - t0))

    # --- Trusted site: record query plan (connectors fulfill fetch) ---
    for prov in trusted_site:
        pid = str(prov.get("id"))
        row_stat = provider_stats_map[pid]
        for q in queries:
            if runtime_exceeded():
                break
            query_stats.append(
                {
                    "provider_id": pid,
                    "query": q["query"],
                    "domain": q.get("domain"),
                    "source_id": q.get("source_id"),
                    "kind": q.get("kind"),
                    "urls": 0,
                    "cached": False,
                }
            )
            row_stat["queries"] += 1
        emit("Discovery Provider", f"{prov.get('name')}: planned {row_stat['queries']} site queries")

    # --- PRIMARY paid API only (default: Tavily), max N live searches/session ---
    # Avoids queries × multi-provider fan-out that burned API budget.
    empty_streak_by_provider: dict[str, int] = {str(p.get("id")): 0 for p in api_providers}
    providers_exhausted: set[str] = set()
    live_primary_searches = 0
    primary_urls = 0

    def _run_api_provider(
        prov: dict[str, Any],
        q: dict[str, Any],
        *,
        count_live: bool,
    ) -> int:
        """Execute one provider×query. Returns live request count (0 if cache/skip)."""
        nonlocal live_primary_searches
        pid = str(prov.get("id"))
        if pid in providers_exhausted:
            return 0
        row_stat = provider_stats_map[pid]
        inst = build_provider(prov)
        if not inst:
            providers_exhausted.add(pid)
            row_stat["exhausted"] = True
            row_stat["exhaustion_reason"] = "adapter_missing"
            return 0

        cached = cache.get_query(pid, q["query"])
        t1 = time.perf_counter()
        live = 0
        if cached is not None:
            found = cached
            row_stat["cache_hits"] += 1
            elapsed = round((time.perf_counter() - t1) * 1000, 1)
        else:
            if count_live and live_primary_searches >= max_primary_searches:
                return 0
            try:
                found = inst.discover(q["query"], limit=per_results)
            except Exception as exc:  # noqa: BLE001
                found = []
                row_stat["error"] = str(exc)
                if "429" in str(exc) or "quota" in str(exc).lower():
                    providers_exhausted.add(pid)
                    row_stat["exhausted"] = True
                    row_stat["exhaustion_reason"] = "provider_quota_reached"
            elapsed = round((time.perf_counter() - t1) * 1000, 1)
            cache.set_query(pid, q["query"], found)
            live = 1
            if count_live:
                live_primary_searches += 1

        row_stat["queries"] += 1
        row_stat["urls"] += len(found)
        row_stat["elapsed_ms"] += elapsed

        if not found:
            empty_streak_by_provider[pid] = empty_streak_by_provider.get(pid, 0) + 1
            if empty_streak_by_provider[pid] >= max(3, min(8, len(queries) // 2 or 3)):
                providers_exhausted.add(pid)
                row_stat["exhausted"] = True
                row_stat["exhaustion_reason"] = "provider_exhausted_empty_results"
        else:
            empty_streak_by_provider[pid] = 0

        for f in found:
            f["provider_id"] = pid
            f["provider_name"] = prov.get("name")
            f["discovery_provider"] = pid
            f["discovery_query"] = q["query"]
            f["target_source_id"] = q.get("source_id")
        raw_candidates.extend(found)
        query_stats.append(
            {
                "provider_id": pid,
                "query": q["query"],
                "domain": q.get("domain"),
                "source_id": q.get("source_id"),
                "urls": len(found),
                "elapsed_ms": elapsed,
                "cached": cached is not None,
                "live_search": live == 1,
            }
        )
        return live

    for q in queries:
        if runtime_exceeded():
            stop_reason = "runtime_budget_reached"
            break
        if knowledge_gap_satisfied(gap, unique_url_count()):
            stop_reason = "knowledge_gap_satisfied"
            break
        if live_primary_searches >= max_primary_searches:
            stop_reason = "primary_search_budget_reached"
            break
        # Reserve a slice of runtime for feeds when feeds are active
        if feed_providers and remaining_s() < max(12.0, runtime_limit * 0.25):
            break

        for prov in api_providers:
            if runtime_exceeded():
                stop_reason = "runtime_budget_reached"
                break
            if live_primary_searches >= max_primary_searches:
                break
            _run_api_provider(prov, q, count_live=True)

        if api_providers and len(providers_exhausted) >= len(api_providers):
            break

    primary_urls = unique_url_count()

    # Optional secondary paid APIs — only if policy allows AND primary yielded nothing
    if (
        secondary_fallback
        and secondary_paid
        and primary_urls == 0
        and not runtime_exceeded()
    ):
        emit(
            "Discovery",
            f"Primary {primary_api} yielded 0 URLs — secondary paid fallback "
            f"({len(secondary_paid)} providers, remaining budget "
            f"{max(0, max_primary_searches - live_primary_searches)})",
        )
        for q in queries:
            if runtime_exceeded() or live_primary_searches >= max_primary_searches:
                break
            for prov in secondary_paid:
                if live_primary_searches >= max_primary_searches:
                    break
                _run_api_provider(prov, q, count_live=True)

    # Free index providers (Common Crawl etc.) — no paid budget
    for prov in free_index_providers:
        if runtime_exceeded():
            break
        for q in queries[: min(5, len(queries))]:
            if runtime_exceeded():
                break
            _run_api_provider(prov, q, count_live=False)

    for prov in api_providers + secondary_paid + free_index_providers:
        pid = str(prov.get("id"))
        row_stat = provider_stats_map.get(pid) or {}
        if row_stat.get("queries") or row_stat.get("urls"):
            emit(
                "Discovery Provider",
                f"{prov.get('name')}: queries={row_stat.get('queries')} "
                f"urls={row_stat.get('urls')} exhausted={row_stat.get('exhausted')}",
            )
    emit(
        "Discovery Budget",
        f"live_{primary_api}_searches={live_primary_searches}/{max_primary_searches} "
        f"unique_urls={unique_url_count()}",
    )

    # --- Feed providers: harvest trusted sources (remaining-runtime adaptive) ---
    for prov in feed_providers:
        if runtime_exceeded():
            stop_reason = "runtime_budget_reached"
            break
        if knowledge_gap_satisfied(gap, unique_url_count()):
            stop_reason = "knowledge_gap_satisfied"
            break
        rem = remaining_s()
        if rem < 5.0:
            stop_reason = "runtime_budget_reached"
            break
        # ~2.5s per source estimate → scale source count to remaining runtime
        adaptive_sources = max(3, min(budget.feed_source_budget, int(rem / 2.5)))
        feed_sources = (reputation or enabled_sources or all_sources)[
            :adaptive_sources
        ] or enabled_sources
        pid = str(prov.get("id"))
        api_type = str(prov.get("api_type") or "")
        inst = build_provider(prov)
        if not inst:
            continue
        row_stat = provider_stats_map[pid]
        t1 = time.perf_counter()
        try:
            found = inst.discover(
                instruction,
                limit=max(per_results * 4, adaptive_sources * 4),
                trusted_sources=feed_sources,
                source_budget=adaptive_sources,
            )
        except Exception as exc:  # noqa: BLE001
            found = []
            row_stat["error"] = str(exc)
        elapsed = round((time.perf_counter() - t1) * 1000, 1)
        row_stat["elapsed_ms"] += elapsed
        row_stat["queries"] += 1
        row_stat["urls"] += len(found)
        if not found:
            row_stat["exhausted"] = True
            row_stat["exhaustion_reason"] = "empty_feed_results"
        for f in found:
            f["provider_id"] = pid
            f["provider_name"] = prov.get("name")
            f["discovery_provider"] = pid
        raw_candidates.extend(found)
        query_stats.append(
            {
                "provider_id": pid,
                "query": f"{api_type}:trusted_feeds",
                "urls": len(found),
                "elapsed_ms": elapsed,
            }
        )
        emit(
            "Discovery Provider",
            f"{prov.get('name')}: {len(found)} URLs via {api_type} "
            f"(sources={adaptive_sources})",
        )

    if stop_reason == "completed" and runtime_exceeded():
        stop_reason = "runtime_budget_reached"
    if stop_reason == "completed" and knowledge_gap_satisfied(gap, unique_url_count()):
        stop_reason = "knowledge_gap_satisfied"
    if stop_reason == "completed" and api_providers and len(providers_exhausted) >= len(api_providers):
        stop_reason = "provider_exhausted"

    # Trusted source verification — reject non-registry domains
    filtered = filter_discovered_urls(raw_candidates, sources=all_sources)
    accepted_all = filtered["accepted"]
    # Adaptive accept budget: prefer all accepted within url_budget for download capacity
    accepted = accepted_all[:url_budget] if url_budget > 0 else accepted_all
    rejected = filtered["rejected"]
    urls_remaining = max(0, len(accepted_all) - len(accepted))

    emit(
        "Trusted Filter",
        f"accepted={len(accepted)} rejected={len(rejected)} "
        f"remaining={urls_remaining} duplicates={filtered.get('duplicates', 0)} "
        f"allowlist={filtered.get('allowlist_size')}",
    )

    # Provider utilization metrics
    provider_stats = list(provider_stats_map.values())
    total_q = sum(int(p.get("queries") or 0) for p in provider_stats) or 1
    for p in provider_stats:
        p["utilization"] = round(int(p.get("queries") or 0) / total_q, 4)
        if p.get("operational_status") == "MISCONFIGURED":
            p["exhausted"] = False
            p["exhaustion_reason"] = p.get("disable_reason") or "misconfigured"

    # Persist yield for ranking
    try:
        update_provider_yield(provider_stats, accepted=accepted, repo_root=root)
    except Exception:  # noqa: BLE001
        pass

    # Convert accepted URLs to SearchResult-like objects for pipeline merge
    search_results: list[SearchResult] = []
    for a in accepted:
        search_results.append(
            SearchResult.create(
                connector_id="DISC-LAYER",
                source_id=str(a.get("source_id") or "SRC-UNKNOWN"),
                title=str(a.get("title") or a.get("url") or "Discovered document")[:200],
                url=str(a.get("url")),
                snippet=str(
                    a.get("snippet")
                    or "Discovered via discovery layer; not a knowledge claim."
                ),
                trust_score=0.85,
                dry_run=False,
                metadata={
                    "discovery_provider": a.get("provider_id") or a.get("discovery_provider"),
                    "discovery_provider_name": a.get("provider_name"),
                    "discovery_query": a.get("discovery_query") or "",
                    "discovery_only": True,
                    "verified_host": a.get("verified_host"),
                    "published_at": a.get("published_at") or "",
                    "api": "discovery_layer",
                },
            )
        )

    elapsed_ms = round((time.perf_counter() - t0) * 1000, 1)
    rows_per_provider = {
        str(p.get("provider_id")): int(p.get("urls") or 0) for p in provider_stats
    }
    hours = max(elapsed_ms / 3_600_000.0, 1e-9)
    analytics = {
        "started_at": utc_now_iso(),
        "mission_id": mission_id,
        "session_id": session_id,
        "instruction": instruction,
        "dataset": dataset,
        "knowledge_gap": gap,
        "budgets": budget.to_dict(),
        "discovery_policy": {
            "primary_api": primary_api,
            "max_primary_searches": max_primary_searches,
            "live_primary_searches": live_primary_searches,
            "secondary_paid_api_fallback": secondary_fallback,
            "one_discovery_multi_dataset": bool(
                disc_policy.get("one_discovery_multi_dataset", True)
            ),
        },
        "queries_generated": len(queries),
        "queries_executed": sum(int(p.get("queries") or 0) for p in provider_stats),
        "urls_discovered": len(raw_candidates),
        "urls_accepted": len(accepted),
        "urls_rejected": len(rejected),
        "urls_remaining": urls_remaining,
        "duplicate_urls": filtered.get("duplicates", 0),
        "elapsed_ms": elapsed_ms,
        "stop_reason": stop_reason,
        "providers_active": len(active_providers),
        "providers_misconfigured": len(misconfigured),
        "providers_disabled": len(disabled),
        "providers_exhausted": sum(1 for p in provider_stats if p.get("exhausted")),
        "provider_utilization": {
            str(p.get("provider_id")): p.get("utilization") for p in provider_stats
        },
        "rows_per_provider": rows_per_provider,
        "urls_per_hour": round(len(raw_candidates) / hours, 2),
        "accepted_per_hour": round(len(accepted) / hours, 2),
        "providers": provider_stats,
        "query_stats": query_stats[:200],
        "reputation_top": [
            {
                "id": s.get("id"),
                "name": s.get("name"),
                "reputation": s.get("_reputation"),
                "score": s.get("_rank_score"),
                "authority": s.get("_authority"),
            }
            for s in reputation[: budget.domain_budget]
        ],
        "provider_ranking": [
            {
                "id": p.get("id"),
                "name": p.get("name"),
                "score": p.get("_rank_score"),
                "status": p.get("operational_status"),
                "components": p.get("_rank_components"),
            }
            for p in ranked_all
        ],
        "accepted_urls": [
            {
                "url": a.get("url"),
                "source_id": a.get("source_id"),
                "provider_id": a.get("provider_id") or a.get("discovery_provider"),
                "title": a.get("title"),
            }
            for a in accepted[:200]
        ],
        "rejected_urls": [
            {
                "url": r.get("url"),
                "reason": r.get("reject_reason"),
                "host": r.get("host"),
                "provider_id": r.get("provider_id"),
            }
            for r in rejected[:100]
        ],
        "cache": cache.stats(),
        "note": "Search engines are discovery tools only; knowledge comes from trusted sources.",
    }

    # Persist analytics + reports
    state_path = root / "automation" / "learning" / "state" / "discovery_analytics.json"
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps(analytics, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    try:
        from automation.acquisition.discovery_pkg.reports import write_discovery_reports

        write_discovery_reports(analytics, repo_root=root)
    except Exception:  # noqa: BLE001
        pass
    try:
        from automation.acquisition.discovery_pkg.audit import write_audit_reports

        write_audit_reports(
            repo_root=root,
            analytics=analytics,
            budgets=budget.to_dict(),
        )
    except Exception:  # noqa: BLE001
        pass

    return {
        "ok": True,
        "knowledge_gap": gap,
        "budgets": budget.to_dict(),
        "queries": queries,
        "providers": provider_stats,
        "raw_candidates": raw_candidates,
        "accepted": accepted,
        "rejected": rejected,
        "search_results": search_results,
        "analytics": analytics,
        "reputation": reputation[: budget.domain_budget],
        "stop_reason": stop_reason,
    }
