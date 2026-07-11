# Provider Efficiency

**Generated:** 2026-07-11T13:39:39+00:00  
**Source:** last `discovery_analytics.json`

## Totals

| Metric | Value |
|--------|------:|
| Queries executed | 85 |
| URLs discovered | 595 |
| URLs accepted | 248 |
| URLs rejected | 347 |
| Accept rate | 41.68% |
| Stop reason | completed |
| Elapsed ms | 51750.1 |

## Per provider

| Provider | Status | Queries | URLs | Util | Latency ms | Exhausted | Creds |
|----------|--------|--------:|-----:|-----:|-----------:|-----------|-------|
| Sitemap Discovery | ACTIVE | 1 | 20 | 0.0118 | 4412.0 | False | True |
| Common Crawl Index | ACTIVE | 37 | 540 | 0.4353 | 43668.299999999996 | False | True |
| RSS Discovery | ACTIVE | 1 | 15 | 0.0118 | 1967.3 | False | True |
| Atom Discovery | ACTIVE | 1 | 20 | 0.0118 | 1233.4 | False | True |
| OpenSearch Description | ACTIVE | 8 | 0 | 0.0941 | 0.0 | True | True |
| Trusted Site Search (connector-backed) | ACTIVE | 37 | 0 | 0.4353 | 0.0 | False | True |
| Google Programmable Search | MISCONFIGURED | 0 | 0 | 0.0 | 0.0 | False | False |
| Bing Web Search API | MISCONFIGURED | 0 | 0 | 0.0 | 0.0 | False | False |
| Brave Search API | MISCONFIGURED | 0 | 0 | 0.0 | 0.0 | False | False |
| Tavily | MISCONFIGURED | 0 | 0 | 0.0 | 0.0 | False | False |
| SerpAPI | MISCONFIGURED | 0 | 0 | 0.0 | 0.0 | False | False |
| Yandex XML Search | MISCONFIGURED | 0 | 0 | 0.0 | 0.0 | False | False |

## Download coupling

Last acquisition: downloaded **7** / requested **20**.  
Discovery acceptance ≠ download.

## Finding

Discovery can be large (595 URLs) while publish stays low — **post-discovery download budget + extraction multiplicity** dominate after discovery.
