# Provider Exhaustion

**Generated:** 2026-07-14T15:07:07+00:00

**Stop reason (last run):** `runtime_budget_reached`

| Provider | Queries | URLs | Exhausted | Reason |
|----------|--------:|-----:|-----------|--------|
| Tavily (primary) | 10 | 158 | False | ready |
| Common Crawl Index | 5 | 100 | False | ready |
| Sitemap Discovery | 1 | 12 | False | ready |
| RSS Discovery | 1 | 12 | False | ready |
| Atom Discovery | 0 | 0 | False | ready |
| Trusted Site Search (connector-backed) | 10 | 0 | False | ready |
| OpenSearch Description | 5 | 0 | True | provider_exhausted_empty_results |
| Google Programmable Search | 0 | 0 | False | disabled |
| Bing Web Search API | 0 | 0 | False | disabled |
| Brave Search API | 0 | 0 | False | disabled |
| SerpAPI | 0 | 0 | False | disabled |
| Yandex XML Search | 0 | 0 | False | disabled |

## Adaptive stopping

- Infinite crawling is prevented by runtime budget + provider exhaustion + quota.
- Discovery does **not** stop at fixed document counts.
