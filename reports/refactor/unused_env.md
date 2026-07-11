# Unused / Optional Environment Variables

**Generated:** 2026-07-11  
**Sprint:** IDA Dataset Factory Simplification v2.0

## Still read (optional; MISCONFIGURED if missing is OK)

| Variable | Role after simplification |
|----------|---------------------------|
| `TAVILY_API_KEY` | **Primary** discovery (required for paid search) |
| `GOOGLE_SEARCH_API_KEY` / `GOOGLE_SEARCH_ENGINE_ID` | Secondary — disabled default |
| `BING_SEARCH_API_KEY` | Secondary — disabled default |
| `BRAVE_SEARCH_API_KEY` | Secondary — disabled default |
| `SERPAPI_API_KEY` | Secondary — disabled default |
| `YANDEX_API_KEY` / `YANDEX_USER` | Secondary — disabled default |
| `COMMONCRAWL_ENABLED` | Free index (default on) |
| `RSS_ENABLED` / `ATOM_ENABLED` / `SITEMAP_ENABLED` | Free feeds (default on) |
| `HF_TOKEN` / `HF_DATASET_REPO` | Hugging Face publish |
| `IDA_GITHUB_TOKEN` / `GH_PAT` / `GITHUB_TOKEN` | GHA dispatch + status |
| Fulltext emails / keys | OpenAlex, Crossref, Unpaywall, CORE |

## GHA learn.yml still maps secondary keys

Keys remain in workflow env for opt-in re-enable without workflow edit. Network calls skip disabled/MISCONFIGURED providers.

## Not deleted from workflow

Removing secondary secret mappings would force a second workflow change when re-enabling fallback. Cost of keeping them: zero API traffic when registry `enabled: false`.
