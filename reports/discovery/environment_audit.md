# Environment Audit

**Generated:** 2026-07-11T12:20:30+00:00

Credentials are never logged. Status only: Loaded / Missing / Disabled.

## Local

| Variable | Status |
|----------|--------|
| `GOOGLE_SEARCH_API_KEY` | Missing |
| `GOOGLE_SEARCH_ENGINE_ID` | Missing |
| `BING_SEARCH_API_KEY` | Missing |
| `BRAVE_SEARCH_API_KEY` | Missing |
| `SERPAPI_API_KEY` | Missing |
| `TAVILY_API_KEY` | Loaded |
| `YANDEX_API_KEY` | Missing |
| `YANDEX_USER` | Missing |
| `COMMONCRAWL_ENABLED` | Loaded |
| `RSS_ENABLED` | Missing |
| `ATOM_ENABLED` | Missing |
| `SITEMAP_ENABLED` | Missing |
| `OPENALEX_EMAIL` | Missing |
| `CROSSREF_MAILTO` | Missing |

## GitHub Actions (`learn.yml`)

| Variable | Workflow mapping | Status |
|----------|------------------|--------|
| `GOOGLE_SEARCH_API_KEY` | True | Mapped (secret may be empty) |
| `GOOGLE_SEARCH_ENGINE_ID` | True | Mapped (secret may be empty) |
| `BING_SEARCH_API_KEY` | True | Mapped (secret may be empty) |
| `BRAVE_SEARCH_API_KEY` | True | Mapped (secret may be empty) |
| `SERPAPI_API_KEY` | True | Mapped (secret may be empty) |
| `TAVILY_API_KEY` | True | Loaded |
| `YANDEX_API_KEY` | True | Mapped (secret may be empty) |
| `YANDEX_USER` | True | Mapped (secret may be empty) |
| `COMMONCRAWL_ENABLED` | True | Loaded |
| `RSS_ENABLED` | False | Missing mapping |
| `ATOM_ENABLED` | False | Missing mapping |
| `SITEMAP_ENABLED` | False | Missing mapping |
| `OPENALEX_EMAIL` | True | Mapped (secret may be empty) |
| `CROSSREF_MAILTO` | True | Mapped (secret may be empty) |

## Vercel

Discovery acquisition runs in Python/GHA, not Vercel runtime. Dashboard is read-only over repo state. Keys on Vercel are optional.

| Variable | Status |
|----------|--------|
| `GOOGLE_SEARCH_API_KEY` | Not applicable for Vercel SSR |
| `GOOGLE_SEARCH_ENGINE_ID` | Not applicable for Vercel SSR |
| `BING_SEARCH_API_KEY` | Not applicable for Vercel SSR |
| `BRAVE_SEARCH_API_KEY` | Not applicable for Vercel SSR |
| `SERPAPI_API_KEY` | Not applicable for Vercel SSR |
| `TAVILY_API_KEY` | Not applicable for Vercel SSR |
| `YANDEX_API_KEY` | Not applicable for Vercel SSR |
| `YANDEX_USER` | Not applicable for Vercel SSR |
| `COMMONCRAWL_ENABLED` | Not applicable for Vercel SSR |
| `RSS_ENABLED` | Not applicable for Vercel SSR |
| `ATOM_ENABLED` | Not applicable for Vercel SSR |
| `SITEMAP_ENABLED` | Not applicable for Vercel SSR |
| `OPENALEX_EMAIL` | Not applicable for Vercel SSR |
| `CROSSREF_MAILTO` | Not applicable for Vercel SSR |

## Policy

- Never silently disable providers.
- MISCONFIGURED providers are reported with evidence and skipped for network calls only.
