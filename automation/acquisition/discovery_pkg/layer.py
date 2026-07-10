"""Discovery Layer orchestration.

Mission → Knowledge Gap → Discovery → Candidate URLs → Trusted Verification
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Optional

from automation.acquisition.discovery_pkg.cache import DiscoveryCache
from automation.acquisition.discovery_pkg.providers import build_provider
from automation.acquisition.discovery_pkg.query_engine import (
    build_discovery_queries,
    trusted_domains_from_sources,
)
from automation.acquisition.discovery_pkg.registry import DiscoveryRegistry
from automation.acquisition.discovery_pkg.reputation import score_sources_for_discovery
from automation.acquisition.discovery_pkg.trusted_filter import filter_discovered_urls
from automation.acquisition.source_registry import SourceRegistry
from automation.connectors.types import SearchResult
from automation.lib.models import utc_now_iso
from automation.lib.paths import find_repo_root


def _knowledge_gap(repo_root: Path, dataset: str) -> dict[str, Any]:
    """Lightweight gap signal from product targets + row counts (no architecture change)."""
    try:
        from automation.lib.config import load_yaml_file  # type: ignore
    except Exception:  # noqa: BLE001
        load_yaml_file = None
    targets = {}
    try:
        from automation.lib.simple_yaml import load_simple_yaml

        p = repo_root / "automation" / "config" / "product_targets.yaml"
        if p.exists():
            data = load_simple_yaml(p.read_text(encoding="utf-8")) or {}
            targets = data.get("targets") or {}
    except Exception:  # noqa: BLE001
        targets = {}
    target = int(targets.get(dataset) or targets.get("_default") or 100)
    current = 0
    csv_path = repo_root / "domains" / "business_development" / f"{dataset}.csv"
    if csv_path.exists():
        try:
            current = max(0, sum(1 for _ in csv_path.open(encoding="utf-8-sig")) - 1)
        except Exception:  # noqa: BLE001
            current = 0
    gap = max(0, target - current)
    coverage = round(100.0 * current / target, 2) if target else 0.0
    return {
        "dataset": dataset,
        "current_rows": current,
        "target_rows": target,
        "gap_rows": gap,
        "coverage_pct": coverage,
        "priority": "high" if coverage < 40 else ("medium" if coverage < 80 else "low"),
    }


def run_discovery(
    *,
    instruction: str,
    dataset: str = "industry_library",
    mission_id: str = "",
    session_id: str = "",
    repo_root: Path | None = None,
    max_queries: int = 16,
    max_urls: int = 30,
    log: Optional[Any] = None,
) -> dict[str, Any]:
    """Execute discovery layer. Search engines never become knowledge sources."""
    root = repo_root or find_repo_root()
    emit = log or (lambda verb, detail: print(f"[{verb}] {detail}"))

    t0 = time.perf_counter()
    gap = _knowledge_gap(root, dataset)
    emit("Knowledge Gap", f"{dataset}: {gap['current_rows']}/{gap['target_rows']} ({gap['coverage_pct']}%) gap={gap['gap_rows']}")

    src_reg = SourceRegistry(repo_root=root)
    # All sources for allowlist; reputation ranks which domains to query first
    all_sources = src_reg.list_sources(enabled_only=False)
    enabled_sources = src_reg.list_sources(enabled_only=True)
    reputation = score_sources_for_discovery(
        enabled_sources or all_sources,
        dataset=dataset,
        repo_root=root,
    )
    # Prefer high reputation domains for site: queries
    domains = trusted_domains_from_sources(reputation[:20] or all_sources)
    queries = build_discovery_queries(
        instruction,
        trusted_domains=domains,
        max_queries=max_queries,
    )
    emit("Discovery", f"Generated {len(queries)} discovery queries across {len(domains)} trusted domains")

    disc_reg = DiscoveryRegistry(repo_root=root)
    providers = disc_reg.list_providers(enabled_only=True, runnable_only=True)
    # Always ensure trusted_site is present for analytics even if empty results
    if not any(p.get("api_type") == "trusted_site" for p in providers):
        for p in disc_reg.list_providers():
            if p.get("api_type") == "trusted_site":
                providers.insert(0, p)
                break

    cache = DiscoveryCache(repo_root=root)
    raw_candidates: list[dict[str, Any]] = []
    provider_stats: list[dict[str, Any]] = []
    query_stats: list[dict[str, Any]] = []

    # Cap external API providers to avoid cost; prioritize free feeds + trusted_site
    ordered = sorted(
        providers,
        key=lambda p: (
            0 if p.get("api_type") in {"rss", "atom", "sitemap", "trusted_site"} else 1,
            -int(p.get("priority") or 0),
        ),
    )

    for prov in ordered:
        pid = str(prov.get("id"))
        api_type = str(prov.get("api_type") or "")
        inst = build_provider(prov)
        if not inst:
            continue
        h = inst.health()
        row_stat = {
            "provider_id": pid,
            "name": prov.get("name"),
            "api_type": api_type,
            "health": h,
            "queries": 0,
            "urls": 0,
            "cache_hits": 0,
            "elapsed_ms": 0.0,
            "status": prov.get("status"),
            "credentials_available": prov.get("credentials_available"),
        }
        # trusted_site: record queries only (connectors fetch)
        if api_type == "trusted_site":
            for q in queries[:12]:
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
            provider_stats.append(row_stat)
            continue

        # Feed providers: one discover call with trusted sources
        if api_type in {"rss", "atom", "sitemap"}:
            t1 = time.perf_counter()
            try:
                found = inst.discover(
                    instruction,
                    limit=min(15, max_urls),
                    trusted_sources=reputation[:15] or enabled_sources,
                )
            except Exception as exc:  # noqa: BLE001
                found = []
                row_stat["error"] = str(exc)
            elapsed = round((time.perf_counter() - t1) * 1000, 1)
            row_stat["elapsed_ms"] += elapsed
            row_stat["queries"] += 1
            row_stat["urls"] += len(found)
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
            provider_stats.append(row_stat)
            emit("Discovery Provider", f"{prov.get('name')}: {len(found)} URLs via {api_type}")
            continue

        # API search providers: run subset of site: queries (cached)
        # Limit to top domains for cost control
        site_queries = [q for q in queries if q.get("kind") == "site"][:8]
        if not site_queries:
            site_queries = queries[:4]
        for q in site_queries:
            cached = cache.get_query(pid, q["query"])
            t1 = time.perf_counter()
            if cached is not None:
                found = cached
                row_stat["cache_hits"] += 1
                elapsed = round((time.perf_counter() - t1) * 1000, 1)
            else:
                try:
                    found = inst.discover(q["query"], limit=5)
                except Exception as exc:  # noqa: BLE001
                    found = []
                    row_stat["error"] = str(exc)
                elapsed = round((time.perf_counter() - t1) * 1000, 1)
                cache.set_query(pid, q["query"], found)
            row_stat["queries"] += 1
            row_stat["urls"] += len(found)
            row_stat["elapsed_ms"] += elapsed
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
                }
            )
        provider_stats.append(row_stat)
        if row_stat["urls"] or row_stat["queries"]:
            emit(
                "Discovery Provider",
                f"{prov.get('name')}: queries={row_stat['queries']} urls={row_stat['urls']}",
            )

    # Trusted source verification — reject non-registry domains
    filtered = filter_discovered_urls(raw_candidates, sources=all_sources)
    accepted = filtered["accepted"][:max_urls]
    rejected = filtered["rejected"]

    emit(
        "Trusted Filter",
        f"accepted={len(accepted)} rejected={len(rejected)} "
        f"duplicates={filtered.get('duplicates', 0)} allowlist={filtered.get('allowlist_size')}",
    )

    # Convert accepted URLs to SearchResult-like objects for pipeline merge
    search_results: list[SearchResult] = []
    for a in accepted:
        search_results.append(
            SearchResult.create(
                connector_id="DISC-LAYER",
                source_id=str(a.get("source_id") or "SRC-UNKNOWN"),
                title=str(a.get("title") or a.get("url") or "Discovered document")[:200],
                url=str(a.get("url")),
                snippet=str(a.get("snippet") or "Discovered via discovery layer; not a knowledge claim."),
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
    analytics = {
        "started_at": utc_now_iso(),
        "mission_id": mission_id,
        "session_id": session_id,
        "instruction": instruction,
        "dataset": dataset,
        "knowledge_gap": gap,
        "queries_generated": len(queries),
        "queries_executed": sum(int(p.get("queries") or 0) for p in provider_stats),
        "urls_discovered": len(raw_candidates),
        "urls_accepted": len(accepted),
        "urls_rejected": len(rejected),
        "duplicate_urls": filtered.get("duplicates", 0),
        "elapsed_ms": elapsed_ms,
        "providers": provider_stats,
        "query_stats": query_stats[:80],
        "reputation_top": [
            {
                "id": s.get("id"),
                "name": s.get("name"),
                "reputation": s.get("_reputation"),
                "score": s.get("_rank_score"),
                "authority": s.get("_authority"),
            }
            for s in reputation[:15]
        ],
        "accepted_urls": [
            {
                "url": a.get("url"),
                "source_id": a.get("source_id"),
                "provider_id": a.get("provider_id") or a.get("discovery_provider"),
                "title": a.get("title"),
            }
            for a in accepted[:50]
        ],
        "rejected_urls": [
            {
                "url": r.get("url"),
                "reason": r.get("reject_reason"),
                "host": r.get("host"),
                "provider_id": r.get("provider_id"),
            }
            for r in rejected[:50]
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

    return {
        "ok": True,
        "knowledge_gap": gap,
        "queries": queries,
        "providers": provider_stats,
        "raw_candidates": raw_candidates,
        "accepted": accepted,
        "rejected": rejected,
        "search_results": search_results,
        "analytics": analytics,
        "reputation": reputation[:20],
    }
