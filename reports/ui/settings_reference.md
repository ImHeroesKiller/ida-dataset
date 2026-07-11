# Settings Reference — Operator Configuration

Settings is the **central operator configuration** surface. Values are **display** of production policy (freeze: no runtime engine rewrite from UI).

## Dashboard

| Parameter | Value |
|-----------|-------|
| Refresh interval | 30 seconds |
| Console rows | 200 |
| Graph duration | 14 sessions |
| Default page | Dashboard |
| Compact mode | On (UI v1.0) |
| Dark mode | System / sidebar toggle |

## Scheduler

| Parameter | Value |
|-----------|-------|
| Learning interval | 1 hour |
| Hourly schedule | UTC :00 |
| Daily deep learning | 06:00 UTC |
| Concurrent sessions | 1 (no overlap) |
| Retry count | 3 |
| Timeout | Session concurrency queue |

## Discovery

| Parameter | Source |
|-----------|--------|
| Preferred source | `policies.discovery.source_strategy` |
| Random discovery | Enabled (trusted pool) |
| Maximum Tavily searches | `max_tavily_searches_per_session` (default 10) |
| Discovery timeout | Session runtime budget |
| Crawler workers | Adaptive download pool |

## Export

| Parameter | Value |
|-----------|-------|
| GitHub | Enabled · append-only main |
| Hugging Face | Enabled · continuous sync |
| Auto export | Learning mode auto_publish |
| Retry | Workflow retries |
| Versioning | Factory VERSION |

## Knowledge

| Parameter | Source |
|-----------|--------|
| Minimum confidence | `policies.confidence_threshold` |
| Duplicate threshold | `validation.reject_duplicates` |
| Auto publish | Learning mode |
| Quality threshold | DPS + integrity guard |

## Advanced

| Parameter | Value |
|-----------|-------|
| Factory version | VERSION file |
| Mode | development / production |
| Environment diagnostics | reports/ · console |
| Build info | Next.js · Operator UI v1.0 |
| UI freeze | Active |
