# Adaptive Budget

**Generated:** 2026-07-17T21:10:18+00:00

Budgets scale with mission priority, knowledge gap, queue health, provider health, worker capacity, and runtime.

| Budget | Value |
|--------|------:|
| `query_budget` | 46 |
| `url_budget` | 1506 |
| `per_provider_results` | 20 |
| `feed_source_budget` | 17 |
| `domain_budget` | 17 |
| `max_provider_rounds` | 3 |
| `runtime_budget_s` | 538.0 |
| `download_budget` | 500 |
| `extraction_budget` | 500 |
| `publish_budget` | 500 |
| `source_select_budget` | 17 |
| `worker_capacity` | 4 |
| `gap_score` | 138.0 |
| `gap_rows` | 50000.0 |
| `coverage_pct` | 0.0 |
| `mission_priority` | high |
| `queue_pressure` | 0.035 |
| `providers_active` | 7 |
| `providers_misconfigured` | 0 |
| `stop_policy` | provider_exhausted | knowledge_gap_satisfied | runtime_budget_reached | provider_quota_reached |

## Stop conditions (only)

1. Provider exhausted (empty results / no remaining queries)
2. Knowledge gap satisfied (universe gap ≤ 0)
3. Runtime budget reached
4. Provider quota reached

Never stop because an arbitrary document count was hit.
