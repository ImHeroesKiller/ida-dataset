# Deployment Environment — IDA Dataset Factory v2.0

Credentials are **never hardcoded**. All secrets come from environment variables (local `.env`, Vercel, or GitHub Actions secrets).

---

## Required variables

| Variable | Purpose |
|----------|---------|
| *(none hard-required for core factory)* | Core acquisition runs with open trusted APIs (World Bank, OpenAlex, Crossref) without keys |

Core factory, mission engine, validation, and exports operate without paid discovery keys.

---

## Optional — Discovery providers

| Variable | Provider | Notes |
|----------|----------|--------|
| `GOOGLE_SEARCH_API_KEY` | Google Programmable Search | Requires CSE |
| `GOOGLE_SEARCH_ENGINE_ID` | Google CSE engine id (`cx`) | Paired with API key |
| `BING_SEARCH_API_KEY` | Bing Web Search API v7 | Azure subscription key |
| `BRAVE_SEARCH_API_KEY` | Brave Search API | Header `X-Subscription-Token` |
| `SERPAPI_API_KEY` | SerpAPI | Paid organic results |
| `TAVILY_API_KEY` | Tavily | Research search API |
| `YANDEX_API_KEY` | Yandex XML | Also set `YANDEX_USER` when required |
| `YANDEX_USER` | Yandex XML user | Optional companion |
| `COMMONCRAWL_ENABLED` | Common Crawl Index | Default ON; set `0` to opt out |
| `RSS_ENABLED` | RSS discovery | Default on; set `0` to disable |
| `ATOM_ENABLED` | Atom discovery | Default on; set `0` to disable |
| `SITEMAP_ENABLED` | Sitemap discovery | Default on; set `0` to disable |

### Research APIs (connectors)

| Variable | Provider |
|----------|----------|
| `OPENALEX_EMAIL` | OpenAlex polite pool (optional mailto) |
| `CROSSREF_MAILTO` | Crossref User-Agent mailto (optional) |
| `UNPAYWALL_EMAIL` | Unpaywall API email (required for OA PDF discovery) |
| `CORE_API_KEY` | CORE API bearer (optional; higher rate limits) |
| `IDA_FULLTEXT_ENABLED` | Full-text framework toggle (default `1`; set `0` to disable) |

---

## Free-tier / zero-key alternatives

| Capability | Free path |
|------------|-----------|
| Document discovery | RSS / Atom / Sitemap on trusted domains |
| Site-targeted queries | Built-in `DISC-TRUSTED-SITE` (no network) + connectors |
| Scholarly metadata | OpenAlex (mailto recommended), Crossref |
| International docs | World Bank WDS API, OECD/ADB HTML (rate-limited) |
| Common Crawl | Default ON (public index; set `COMMONCRAWL_ENABLED=0` to opt out) |

Paid search APIs are marked **MISCONFIGURED** when keys are missing (never silently disabled). Network calls skip them; status is always reported. The factory continues with remaining ACTIVE providers.

---

## Rate limits & quotas (guidance)

| Provider | Typical free/day | Notes |
|----------|----------------:|-------|
| Google CSE | ~100 | Paid beyond free tier |
| Bing | depends on Azure SKU | Watch RPS |
| Brave | plan-dependent | |
| SerpAPI | plan-dependent | Higher cost/request |
| Tavily | plan-dependent | |
| RSS/Sitemap | high | Be polite; respect robots/rate |
| World Bank / OpenAlex / Crossref | generous public | Use User-Agent + mailto |

Configure per-provider `daily_quota` / `rate_limit` in `automation/config/discovery_registry.yaml`.

---

## Cost implications

- Discovery search APIs may charge **per request**. Prefer **site:** queries limited to trusted domains and **cache hits**.
- **Trusted Site + RSS/Sitemap** path is preferred for production cost control.
- Knowledge extraction does **not** require search engines — connectors to trusted sources remain primary.

---

## Vercel

1. Project → Settings → Environment Variables  
2. Add optional discovery keys for Production / Preview as needed  
3. Redeploy after changes  
4. Do **not** commit `.env` files  

Dashboard/API routes must never print secret values.

---

## GitHub Actions

1. Repository → Settings → Secrets and variables → Actions  
2. Add the same optional keys as repository secrets  
3. Map into workflow `env:` only when a job needs discovery APIs  
4. Prefer open providers for unattended scheduled runs to avoid unexpected cost  

---

## Startup checklist

- [ ] `source_registry.yaml` lists intended trusted sources  
- [ ] `discovery_registry.yaml` present (providers auto-disable without keys)  
- [ ] Optional discovery keys set in env **or** accept free RSS/site path  
- [ ] `OPENALEX_EMAIL` / Crossref mailto set for polite scholarly access (recommended)  
- [ ] Run one learning session; confirm `reports/discovery/` written  
- [ ] Confirm rejected non-registry domains in `rejected_urls.md`  
- [ ] Confirm published rows cite trusted `source_id`, not search engine as knowledge source  

---

## Security rules

1. Never commit API keys  
2. Never log full Authorization headers  
3. Rotate keys if exposed  
4. Discovery providers are **not** trusted knowledge sources  

---

**Related:** [PRODUCTION_FREEZE.md](../PRODUCTION_FREEZE.md) · [SOURCE_POLICY.md](../SOURCE_POLICY.md) · `automation/config/discovery_registry.yaml`
