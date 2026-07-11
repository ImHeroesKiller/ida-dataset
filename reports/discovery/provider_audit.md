# Provider Audit

**Generated:** 2026-07-11T11:54:23+00:00

Search engines are **discovery tools only**. Knowledge is extracted solely from trusted sources.

| ACTIVE | DISABLED | MISCONFIGURED |
|-------:|---------:|--------------:|
| 6 | 0 | 6 |

| Provider | Status | Enabled | Credential | Rate limit | Daily quota | Health | Latency ms | Avg URLs | Avg docs | Yield | Reason |
|----------|--------|---------|------------|----------:|------------:|--------|-----------:|---------:|---------:|------:|--------|
| Trusted Site Search (connector-backed) | **ACTIVE** | True | True | 60 | 100000 | healthy | 0.0 | 0.0 | 0.0 | 0.0 | ready |
| Google Programmable Search | **MISCONFIGURED** | True | False | 10 | 100 | offline | 0.0 | 0.0 | 0.0 | 1.0 | missing credentials: GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_ENGINE_ID |
| Bing Web Search API | **MISCONFIGURED** | True | False | 30 | 1000 | offline | 0.0 | 0.0 | 0.0 | 1.0 | missing credentials: BING_SEARCH_API_KEY |
| Brave Search API | **MISCONFIGURED** | True | False | 20 | 2000 | offline | 0.0 | 0.0 | 0.0 | 1.0 | missing credentials: BRAVE_SEARCH_API_KEY |
| Tavily | **MISCONFIGURED** | True | False | 20 | 1000 | offline | 0.0 | 0.0 | 0.0 | 1.0 | missing credentials: TAVILY_API_KEY |
| SerpAPI | **MISCONFIGURED** | True | False | 10 | 100 | offline | 0.0 | 0.0 | 0.0 | 1.0 | missing credentials: SERPAPI_API_KEY |
| Sitemap Discovery | **ACTIVE** | True | True | 20 | 5000 | healthy | 0.0 | 18.0 | 18.0 | 1.0 | ready |
| RSS Discovery | **ACTIVE** | True | True | 30 | 10000 | healthy | 0.0 | 7.5 | 2.5 | 1.0 | ready |
| Atom Discovery | **ACTIVE** | True | True | 30 | 10000 | healthy | 0.0 | 10.0 | 2.5 | 1.0 | ready |
| Yandex XML Search | **MISCONFIGURED** | True | False | 10 | 100 | offline | 0.0 | 0.0 | 0.0 | 1.0 | missing credentials: YANDEX_API_KEY, YANDEX_USER |
| Common Crawl Index | **ACTIVE** | True | True | 5 | 500 | healthy | 0.0 | 270.0 | 109.0 | 1.0 | ready |
| OpenSearch Description | **ACTIVE** | True | True | 10 | 1000 | idle | 0.0 | 0.0 | 0.0 | 0.5 | ready |

## Named provider checklist

| Requested | Mapping | Status |
|-----------|---------|--------|
| Tavily | `DISC-TAVILY` | **MISCONFIGURED** |
| Google CSE | `DISC-GOOGLE-CSE` | **MISCONFIGURED** |
| Google Programmable Search | `DISC-GOOGLE-CSE` | **MISCONFIGURED** |
| Google Search API | `DISC-GOOGLE-CSE` | **MISCONFIGURED** |
| Brave | `DISC-BRAVE` | **MISCONFIGURED** |
| Bing | `DISC-BING` | **MISCONFIGURED** |
| SerpAPI | `DISC-SERPAPI` | **MISCONFIGURED** |
| Yandex | `DISC-YANDEX` | **MISCONFIGURED** |
| RSS | `DISC-RSS` | **ACTIVE** |
| Atom | `DISC-ATOM` | **ACTIVE** |
| Sitemap | `DISC-SITEMAP` | **ACTIVE** |
| Common Crawl | `DISC-COMMONCRAWL` | **ACTIVE** |
| Trusted Registry | `DISC-TRUSTED-SITE` | **ACTIVE** |

## Connector-backed knowledge sources (not discovery search APIs)

These acquire documents via the connector framework after discovery.

| Source | Connector | Role |
|--------|-----------|------|
| OpenAlex | `CONN-OPENALEX-001` | Trusted knowledge connector |
| Crossref | `CONN-CROSSREF-001` | Trusted knowledge connector |
| World Bank | `CONN-WB-001` | Trusted knowledge connector |
| OECD | `CONN-OECD-001` | Trusted knowledge connector |
| ADB | `CONN-ADB-001` | Trusted knowledge connector |
| BPS | `CONN-BPS-001` | Trusted knowledge connector |

## Tavily connectivity (explicit)

- Operational status: **MISCONFIGURED**
- Credential loaded: `False`
- Probe: `{"probed": false, "ok": false, "status": "MISCONFIGURED", "message": "TAVILY_API_KEY missing", "latency_ms": null}`

> Providers are never silently disabled. MISCONFIGURED means enabled but credentials missing.
