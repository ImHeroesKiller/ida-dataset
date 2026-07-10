"""Production economics — bandwidth, API, cache, rows, ROI proxies."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from automation.lib.paths import find_repo_root


def collect_economics(repo_root: Path | None = None) -> dict[str, Any]:
    root = repo_root or find_repo_root()
    perf = {}
    acq = {}
    disc = {}
    cache = {}
    try:
        p = root / "automation" / "learning" / "state" / "acquisition_performance.json"
        if p.exists():
            acq = json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        pass
    try:
        p = root / "automation" / "learning" / "state" / "source_performance.json"
        if p.exists():
            perf = json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        pass
    try:
        p = root / "automation" / "learning" / "state" / "discovery_analytics.json"
        if p.exists():
            disc = json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        pass
    try:
        p = root / "automation" / "connectors" / "cache" / "http_cache.json"
        if p.exists():
            cache = (json.loads(p.read_text(encoding="utf-8")) or {}).get("stats") or {}
    except Exception:  # noqa: BLE001
        pass

    thr = acq.get("throughput") or {}
    dl = acq.get("downloads") or {}
    sources = perf.get("sources") or {}
    rows = sum(int(s.get("rows_yielded") or 0) for s in sources.values())
    docs = sum(int(s.get("documents_yielded") or 0) for s in sources.values())
    attempts = sum(int(s.get("attempts") or 0) for s in sources.values())
    fails = sum(int(s.get("failures") or 0) for s in sources.values())

    bytes_dl = int(dl.get("bytes") or 0)
    gb = bytes_dl / (1024**3) if bytes_dl else 0.0
    api_calls = int(disc.get("queries_executed") or 0) + int(dl.get("requested") or 0)
    rows_pub = int(thr.get("rows") or rows)
    cache_hits = int(cache.get("hits") or 0) + int(cache.get("not_modified") or 0)
    cache_miss = int(cache.get("misses") or 0)

    # Cost proxy: free open APIs ≈ 0; discovery paid keys unknown → estimate by call count only
    est_cost_usd = round(api_calls * 0.001, 4)  # conservative placeholder economics unit

    rows_per_api = round(rows_pub / api_calls, 4) if api_calls else float(rows_pub)
    rows_per_gb = round(rows_pub / gb, 2) if gb > 0 else None
    roi = round(rows_pub / max(0.0001, est_cost_usd), 2) if est_cost_usd else float(rows_pub)

    by_source = []
    for sid, s in list(sources.items())[:30]:
        by_source.append(
            {
                "source_id": sid,
                "rows": int(s.get("rows_yielded") or 0),
                "documents": int(s.get("documents_yielded") or 0),
                "success_rate": s.get("success_rate"),
            }
        )
    by_source.sort(key=lambda x: -x["rows"])

    return {
        "bandwidth_bytes": bytes_dl,
        "bandwidth_gb": round(gb, 6),
        "api_requests": api_calls,
        "cache_hits": cache_hits,
        "cache_misses": cache_miss,
        "cache_hit_rate": round(
            cache_hits / max(1, cache_hits + cache_miss), 4
        ),
        "rows_produced": rows_pub,
        "rows_rejected": fails,  # proxy from connector failures
        "documents_processed": docs or int(dl.get("downloaded") or thr.get("documents") or 0),
        "rows_per_source": by_source[:15],
        "rows_per_connector": (acq.get("connectors") or [])[:15],
        "rows_per_gb": rows_per_gb,
        "rows_per_api_call": rows_per_api,
        "estimated_production_cost_usd": est_cost_usd,
        "knowledge_roi": roi,
        "attempts": attempts,
    }
