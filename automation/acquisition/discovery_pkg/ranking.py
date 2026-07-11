"""Dynamic discovery provider prioritization.

Rank by: yield · freshness · trust · latency · coverage · mission relevance · success rate.
Higher useful knowledge yield → higher priority automatically.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from automation.lib.paths import find_repo_root


def _load_provider_yield(repo_root: Path) -> dict[str, dict[str, Any]]:
    path = repo_root / "automation" / "learning" / "state" / "discovery_provider_yield.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8")) or {}
        return dict(data.get("providers") or {})
    except Exception:  # noqa: BLE001
        return {}


def _load_last_analytics(repo_root: Path) -> dict[str, Any]:
    path = repo_root / "automation" / "learning" / "state" / "discovery_analytics.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8")) or {}
    except Exception:  # noqa: BLE001
        return {}


def rank_providers(
    providers: list[dict[str, Any]],
    *,
    instruction: str = "",
    dataset: str = "",
    repo_root: Path | None = None,
) -> list[dict[str, Any]]:
    """Return providers sorted by adaptive score (highest first). Mutates copies only."""
    root = repo_root or find_repo_root()
    hist = _load_provider_yield(root)
    last = _load_last_analytics(root)
    last_by_id: dict[str, dict[str, Any]] = {}
    for p in last.get("providers") or []:
        if isinstance(p, dict) and p.get("provider_id"):
            last_by_id[str(p["provider_id"])] = p

    instr = (instruction or "").lower()
    tokens = {t for t in instr.replace(",", " ").split() if len(t) > 3}
    if dataset:
        tokens.add(dataset.replace("_", " ").split()[0].lower())

    free_types = {"rss", "atom", "sitemap", "trusted_site", "opensearch", "commoncrawl"}
    scored: list[tuple[float, dict[str, Any]]] = []

    for raw in providers:
        p = dict(raw)
        pid = str(p.get("id") or p.get("provider_id") or "")
        api = str(p.get("api_type") or "")
        h = hist.get(pid) or {}
        last_p = last_by_id.get(pid) or {}

        # Yield: accepted / discovered over history
        urls_total = float(h.get("urls_total") or last_p.get("urls") or 0)
        accepted = float(h.get("urls_accepted") or 0)
        queries = float(h.get("queries") or last_p.get("queries") or 0)
        success_rate = float(h.get("success_rate") or 0)
        if success_rate <= 0 and queries > 0:
            success_rate = 1.0 if urls_total > 0 else 0.2
        if success_rate <= 0:
            success_rate = 0.5 if p.get("credentials_available") else 0.0

        yield_score = min(1.0, (accepted / 40.0) * 0.6 + (urls_total / 80.0) * 0.4)
        if urls_total > 0 and accepted == 0:
            yield_score = min(0.35, urls_total / 100.0)

        # Latency: lower is better
        lat = float(h.get("avg_latency_ms") or last_p.get("elapsed_ms") or 0)
        if lat <= 0 and last_p.get("queries"):
            lat = float(last_p.get("elapsed_ms") or 0) / max(1, int(last_p.get("queries") or 1))
        latency_score = max(0.0, min(1.0, 1.0 - (lat / 60000.0))) if lat else 0.55

        # Freshness: recent successful runs
        freshness = float(h.get("freshness") or 0.5)
        if last_p.get("urls"):
            freshness = min(1.0, freshness + 0.2)

        # Trust: free trusted-path providers preferred when keys missing; API when healthy
        trust = 0.7
        if api in free_types:
            trust = 0.9 if api != "opensearch" else 0.5
        if p.get("credentials_available"):
            trust = min(1.0, trust + 0.05)
        if p.get("operational_status") == "MISCONFIGURED":
            trust = 0.05
        if p.get("operational_status") == "DISABLED":
            trust = 0.0

        # Coverage: site filter support + breadth
        coverage = 0.5
        if p.get("supports_site_filter"):
            coverage += 0.25
        if api in {"google_cse", "bing", "brave", "serpapi", "tavily"}:
            coverage += 0.15
        if api in {"rss", "atom", "sitemap"}:
            coverage += 0.1
        coverage = min(1.0, coverage)

        # Mission relevance: keyword overlap with provider notes/name
        blob = f"{p.get('name')} {p.get('notes') or ''} {api}".lower()
        hits = sum(1 for t in tokens if t in blob) if tokens else 0
        relevance = min(1.0, 0.4 + hits * 0.15) if tokens else 0.5
        # Academic datasets prefer scholarly-friendly discovery when mission says so
        if any(t in instr for t in ("research", "paper", "academic", "scholar")):
            if api in {"serpapi", "google_cse", "tavily"}:
                relevance = min(1.0, relevance + 0.15)

        config_priority = float(p.get("priority") or 50) / 100.0

        score = (
            yield_score * 26
            + success_rate * 18
            + latency_score * 12
            + freshness * 10
            + trust * 12
            + coverage * 10
            + relevance * 8
            + config_priority * 4
        )
        # Runnable providers always outrank misconfigured
        if not p.get("credentials_available") and api not in free_types:
            score *= 0.05

        p["_rank_score"] = round(score, 3)
        p["_rank_components"] = {
            "yield": round(yield_score, 3),
            "success_rate": round(success_rate, 3),
            "latency": round(latency_score, 3),
            "freshness": round(freshness, 3),
            "trust": round(trust, 3),
            "coverage": round(coverage, 3),
            "relevance": round(relevance, 3),
            "config_priority": round(config_priority, 3),
        }
        scored.append((score, p))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in scored]


def update_provider_yield(
    provider_stats: list[dict[str, Any]],
    *,
    accepted: list[dict[str, Any]] | None = None,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Persist rolling yield stats for ranking."""
    root = repo_root or find_repo_root()
    path = root / "automation" / "learning" / "state" / "discovery_provider_yield.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = _load_provider_yield(root)
    accepted = accepted or []
    accepted_by: dict[str, int] = {}
    for a in accepted:
        pid = str(a.get("provider_id") or a.get("discovery_provider") or "")
        if pid:
            accepted_by[pid] = accepted_by.get(pid, 0) + 1

    for row in provider_stats:
        pid = str(row.get("provider_id") or "")
        if not pid:
            continue
        prev = existing.get(pid) or {
            "urls_total": 0,
            "urls_accepted": 0,
            "queries": 0,
            "elapsed_ms_total": 0.0,
            "runs": 0,
            "empty_runs": 0,
        }
        urls = int(row.get("urls") or 0)
        queries = int(row.get("queries") or 0)
        elapsed = float(row.get("elapsed_ms") or 0)
        prev["urls_total"] = int(prev.get("urls_total") or 0) + urls
        prev["urls_accepted"] = int(prev.get("urls_accepted") or 0) + int(accepted_by.get(pid) or 0)
        prev["queries"] = int(prev.get("queries") or 0) + queries
        prev["elapsed_ms_total"] = float(prev.get("elapsed_ms_total") or 0) + elapsed
        prev["runs"] = int(prev.get("runs") or 0) + 1
        if urls == 0 and queries > 0:
            prev["empty_runs"] = int(prev.get("empty_runs") or 0) + 1
        runs = max(1, int(prev["runs"]))
        prev["avg_latency_ms"] = round(
            float(prev["elapsed_ms_total"]) / max(1, int(prev["queries"]) or runs), 1
        )
        prev["success_rate"] = round(
            1.0 - (float(prev.get("empty_runs") or 0) / runs), 3
        )
        prev["freshness"] = 1.0 if urls > 0 else max(0.2, float(prev.get("freshness") or 0.5) * 0.9)
        prev["name"] = row.get("name") or prev.get("name")
        prev["api_type"] = row.get("api_type") or prev.get("api_type")
        existing[pid] = prev

    payload = {"providers": existing}
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return existing
