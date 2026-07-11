# Adaptive Budget

**Generated:** 2026-07-11T11:54:23+00:00

Budgets scale with mission priority, knowledge gap, queue health, provider health, worker capacity, and runtime.

| Budget | Value |
|--------|------:|
| `query_budget` | 28 |
| `url_budget` | 452 |
| `per_provider_results` | 15 |
| `feed_source_budget` | 12 |
| `domain_budget` | 12 |
| `max_provider_rounds` | 3 |
| `runtime_budget_s` | 436.467 |
| `download_budget` | 113 |
| `extraction_budget` | 113 |
| `publish_budget` | 113 |
| `source_select_budget` | 12 |
| `worker_capacity` | 4 |
| `gap_score` | 79.467 |
| `gap_rows` | 4947.0 |
| `coverage_pct` | 1.06 |
| `mission_priority` | high |
| `queue_pressure` | 0.1 |
| `providers_active` | 6 |
| `providers_misconfigured` | 6 |
| `stop_policy` | provider_exhausted | knowledge_gap_satisfied | runtime_budget_reached | provider_quota_reached |

## Stop conditions (only)

1. Provider exhausted (empty results / no remaining queries)
2. Knowledge gap satisfied (universe gap ≤ 0)
3. Runtime budget reached
4. Provider quota reached

Never stop because an arbitrary document count was hit.
