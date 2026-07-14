# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T22:18:57+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 59 | 1.06 | 6.5 | 62.8 |
| source_discovery | 59 | 2.73 | 3.3 | 160.8 |
| connector | 59 | 68612.38 | 97806.1 | 4048130.7 |
| document_discovery | 59 | 68612.53 | 97806.2 | 4048139.1 |
| document_download | 59 | 246548.23 | 1509355.9 | 14546345.6 |
| extraction | 59 | 78.86 | 274.0 | 4653.0 |
| candidate_validation | 59 | 6.13 | 9.5 | 361.7 |
| publish_queue | 59 | 6.18 | 9.5 | 364.4 |
| append_dataset | 59 | 48.44 | 119.7 | 2857.8 |
| export | 59 | 0.34 | 0.6 | 20.1 |
| git_commit | 59 | 0.33 | 2.1 | 19.4 |
| push | 59 | 0.32 | 0.8 | 19.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1470 |
| Documents processed | 5595 |
| Process ratio | 380.6% (target ≥90.0%) |
| Rows published (traces) | 227 |
| Sessions observed | 87 |
| Avg session duration (s) | 677.69 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.346 |
| Avg connector latency (ms) | 14128.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **380.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
