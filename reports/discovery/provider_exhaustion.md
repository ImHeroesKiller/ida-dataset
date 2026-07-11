# Provider Exhaustion

**Generated:** 2026-07-11T15:17:15+00:00

**Stop reason (last run):** `runtime_budget_reached`

| Provider | Queries | URLs | Exhausted | Reason |
|----------|--------:|-----:|-----------|--------|
| Tavily | 35 | 362 | False | ready |
| Sitemap Discovery | 1 | 12 | False | ready |
| RSS Discovery | 1 | 7 | False | ready |
| Atom Discovery | 0 | 0 | False | ready |
| Common Crawl Index | 35 | 660 | False | ready |
| Trusted Site Search (connector-backed) | 35 | 0 | False | ready |
| OpenSearch Description | 8 | 0 | True | provider_exhausted_empty_results |
| Google Programmable Search | 0 | 0 | False | missing credentials: GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_ENGINE_ID |
| Bing Web Search API | 0 | 0 | False | missing credentials: BING_SEARCH_API_KEY |
| Brave Search API | 0 | 0 | False | missing credentials: BRAVE_SEARCH_API_KEY |
| SerpAPI | 0 | 0 | False | missing credentials: SERPAPI_API_KEY |
| Yandex XML Search | 0 | 0 | False | missing credentials: YANDEX_API_KEY, YANDEX_USER |

## Adaptive stopping

- Infinite crawling is prevented by runtime budget + provider exhaustion + quota.
- Discovery does **not** stop at fixed document counts.
