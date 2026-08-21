# Adaptive Budget

**Generated:** 2026-08-21T18:51:16+00:00

Budgets scale with mission priority, knowledge gap, queue health, provider health, worker capacity, and runtime.

| Budget | Value |
|--------|------:|
| `query_budget` | 49 |
| `url_budget` | 708 |
| `per_provider_results` | 20 |
| `feed_source_budget` | 18 |
| `domain_budget` | 18 |
| `max_provider_rounds` | 3 |
| `runtime_budget_s` | 505.568 |
| `download_budget` | 177 |
| `extraction_budget` | 177 |
| `publish_budget` | 177 |
| `source_select_budget` | 18 |
| `worker_capacity` | 4 |
| `gap_score` | 87.568 |
| `gap_rows` | 6581.0 |
| `coverage_pct` | 0.38 |
| `mission_priority` | high |
| `queue_pressure` | 0.0 |
| `providers_active` | 7 |
| `providers_misconfigured` | 0 |
| `stop_policy` | provider_exhausted | knowledge_gap_satisfied | runtime_budget_reached | provider_quota_reached |

## Stop conditions (only)

1. Provider exhausted (empty results / no remaining queries)
2. Knowledge gap satisfied (universe gap ≤ 0)
3. Runtime budget reached
4. Provider quota reached

Never stop because an arbitrary document count was hit.
