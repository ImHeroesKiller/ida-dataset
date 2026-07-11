# Adaptive Budget

**Generated:** 2026-07-11T14:45:55+00:00

Budgets scale with mission priority, knowledge gap, queue health, provider health, worker capacity, and runtime.

| Budget | Value |
|--------|------:|
| `query_budget` | 42 |
| `url_budget` | 600 |
| `per_provider_results` | 15 |
| `feed_source_budget` | 18 |
| `domain_budget` | 18 |
| `max_provider_rounds` | 3 |
| `runtime_budget_s` | 461.56 |
| `download_budget` | 150 |
| `extraction_budget` | 150 |
| `publish_budget` | 150 |
| `source_select_budget` | 18 |
| `worker_capacity` | 4 |
| `gap_score` | 79.56 |
| `gap_rows` | 6545.0 |
| `coverage_pct` | 1.1 |
| `mission_priority` | high |
| `queue_pressure` | 0.03 |
| `providers_active` | 7 |
| `providers_misconfigured` | 5 |
| `stop_policy` | provider_exhausted | knowledge_gap_satisfied | runtime_budget_reached | provider_quota_reached |

## Stop conditions (only)

1. Provider exhausted (empty results / no remaining queries)
2. Knowledge gap satisfied (universe gap ≤ 0)
3. Runtime budget reached
4. Provider quota reached

Never stop because an arbitrary document count was hit.
