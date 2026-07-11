# Discovery Strategy

**Generated:** 2026-07-11  
**Sprint:** IDA Dataset Factory Simplification v2.0  
**Status:** Implemented (config + layer + provider)

## Policy

| Knob | Value |
|------|------:|
| Primary paid API | **Tavily** |
| Max Tavily searches / session | **10** |
| Secondary paid APIs (Google/Bing/Brave/SerpAPI/Yandex) | **disabled by default** |
| Secondary fallback | only if `secondary_paid_api_fallback=true` **and** primary yields 0 URLs |
| Free feeds | RSS / Atom / Sitemap + trusted_site (always on) |
| Content richness | Tavily `include_raw_content=true` (Search → rich snippet → queue) |
| Routing | One discovery batch → multi-dataset routing (unchanged engine) |

## Flow

```text
Mission / knowledge gap
        ↓
  Tavily Search (≤10 live requests/session)
        ↓
  Rich content (raw_content / snippet)
        ↓
  Trusted-domain filter (source_registry)
        ↓
  Internal document queue
        ↓
  Multi-dataset routing
  (Industry · Company · Service · Persona · Decision Maker ·
   Risk · Trend · Technology · Competitor · Framework ·
   Regulation · Case Study · …)
```

**One discovery → many datasets.** No repeated multi-provider search fan-out.

## Source strategy preference

1. Operator-selected sources  
2. Knowledge-gap driven discovery  
3. Random trusted discovery  

Ranking criteria: **mission relevance · coverage · freshness · confidence**.

## Before → After

| Metric | Before | After |
|--------|--------|------:|
| Paid providers active (default) | up to 6 | 1 (Tavily) |
| Search fan-out | queries × all API providers | queries × primary only |
| Live Tavily searches / session | unbounded adaptive | ≤ 10 |
| Secondary API cost | multi-provider traffic | ~0 unless operator enables |
| Content per hit | short snippet | raw_content when available |

## Files

| Path | Change |
|------|--------|
| `automation/config/discovery_registry.yaml` | Tavily primary; secondary `enabled: false`; policy block |
| `automation/config/policies.yaml` | `discovery:` policy section |
| `automation/acquisition/discovery_pkg/layer.py` | Cap primary searches; no multi-paid fan-out by default |
| `automation/acquisition/discovery_pkg/providers.py` | Tavily rich content |
| `automation/acquisition/discovery_pkg/ranking.py` | Tavily boost when credentials present |

## Freeze compliance

- No architecture redesign  
- Search engines remain discovery-only (not knowledge sources)  
- Trusted registry still gates domains  
- Secondary adapters retained for operator opt-in (not deleted)
