# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T19:37:13+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 227 | 1.3 | 70.9 | 295.1 |
| source_discovery | 227 | 3.86 | 186.3 | 875.4 |
| connector | 227 | 87412.98 | 97806.1 | 19842747.3 |
| document_discovery | 227 | 87413.13 | 97806.2 | 19842780.2 |
| document_download | 227 | 246309.22 | 1509355.9 | 55912193.4 |
| extraction | 227 | 91.43 | 274.0 | 20754.3 |
| candidate_validation | 227 | 10.87 | 37.2 | 2468.3 |
| publish_queue | 227 | 10.96 | 37.4 | 2489.0 |
| append_dataset | 227 | 41.9 | 119.7 | 9512.1 |
| export | 227 | 0.35 | 1.9 | 78.6 |
| git_commit | 227 | 0.31 | 2.1 | 70.7 |
| push | 227 | 0.31 | 0.8 | 71.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6598 |
| Documents processed | 16745 |
| Process ratio | 253.8% (target ≥90.0%) |
| Rows published (traces) | 1064 |
| Sessions observed | 255 |
| Avg session duration (s) | 946.894 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.832 |
| Avg connector latency (ms) | 13737.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **253.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
