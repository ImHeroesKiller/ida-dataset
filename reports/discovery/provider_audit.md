# Provider Audit

**Generated:** 2026-07-21T19:38:47+00:00

Search engines are **discovery tools only**. Knowledge is extracted solely from trusted sources.

| ACTIVE | DISABLED | MISCONFIGURED |
|-------:|---------:|--------------:|
| 7 | 5 | 0 |

| Provider | Status | Enabled | Credential | Rate limit | Daily quota | Health | Latency ms | Avg URLs | Avg docs | Yield | Reason |
|----------|--------|---------|------------|----------:|------------:|--------|-----------:|---------:|---------:|------:|--------|
| Tavily (primary) | **ACTIVE** | True | True | 20 | 1000 | ERROR | 243.8 | 0.0 | 0.0 | 0.0 | ready |
| Trusted Site Search (connector-backed) | **ACTIVE** | True | True | 60 | 100000 | healthy | 0.0 | 0.0 | 0.0 | 0.0 | ready |
| Sitemap Discovery | **ACTIVE** | True | True | 20 | 5000 | healthy | 0.0 | 12.0 | 12.0 | 1.0 | ready |
| RSS Discovery | **ACTIVE** | True | True | 30 | 10000 | healthy | 0.0 | 12.0 | 4.0 | 1.0 | ready |
| Atom Discovery | **ACTIVE** | True | True | 30 | 10000 | healthy | 0.0 | 0.0 | 0.0 | 1.0 | ready |
| Common Crawl Index | **ACTIVE** | True | True | 5 | 500 | healthy | 0.0 | 100.0 | 50.0 | 1.0 | ready |
| OpenSearch Description | **ACTIVE** | True | True | 10 | 1000 | idle | 0.0 | 0.0 | 0.0 | 0.0 | ready |
| Google Programmable Search | **DISABLED** | False | False | 10 | 100 | offline | 0.0 | 0.0 | 0.0 | 1.0 | enabled=false in discovery_registry.yaml |
| Bing Web Search API | **DISABLED** | False | False | 30 | 1000 | offline | 0.0 | 0.0 | 0.0 | 1.0 | enabled=false in discovery_registry.yaml |
| Brave Search API | **DISABLED** | False | False | 20 | 2000 | offline | 0.0 | 0.0 | 0.0 | 1.0 | enabled=false in discovery_registry.yaml |
| SerpAPI | **DISABLED** | False | False | 10 | 100 | offline | 0.0 | 0.0 | 0.0 | 1.0 | enabled=false in discovery_registry.yaml |
| Yandex XML Search | **DISABLED** | False | False | 10 | 100 | offline | 0.0 | 0.0 | 0.0 | 1.0 | enabled=false in discovery_registry.yaml |

## Named provider checklist

| Requested | Mapping | Status |
|-----------|---------|--------|
| Tavily | `DISC-TAVILY` | **ACTIVE** |
| Google CSE | `DISC-GOOGLE-CSE` | **DISABLED** |
| Google Programmable Search | `DISC-GOOGLE-CSE` | **DISABLED** |
| Google Search API | `DISC-GOOGLE-CSE` | **DISABLED** |
| Brave | `DISC-BRAVE` | **DISABLED** |
| Bing | `DISC-BING` | **DISABLED** |
| SerpAPI | `DISC-SERPAPI` | **DISABLED** |
| Yandex | `DISC-YANDEX` | **DISABLED** |
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

- Operational status: **ACTIVE**
- Credential loaded: `True`
- Probe: `{"probed": true, "ok": false, "status": "ERROR", "message": "connectivity_failed:HTTPError", "latency_ms": 243.8}`

> Providers are never silently disabled. MISCONFIGURED means enabled but credentials missing.
