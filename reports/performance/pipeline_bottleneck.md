# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T03:14:05+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 110 | 1.01 | 6.5 | 110.9 |
| source_discovery | 110 | 3.1 | 39.8 | 341.4 |
| connector | 110 | 80395.58 | 97806.1 | 8843514.0 |
| document_discovery | 110 | 80395.72 | 97806.2 | 8843529.5 |
| document_download | 110 | 267876.39 | 1509355.9 | 29466402.9 |
| extraction | 110 | 82.28 | 274.0 | 9050.6 |
| candidate_validation | 110 | 7.62 | 18.7 | 838.3 |
| publish_queue | 110 | 7.82 | 34.7 | 860.2 |
| append_dataset | 110 | 45.84 | 119.7 | 5042.8 |
| export | 110 | 0.34 | 0.7 | 37.1 |
| git_commit | 110 | 0.32 | 2.1 | 35.1 |
| push | 110 | 0.31 | 0.8 | 34.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3021 |
| Documents processed | 9530 |
| Process ratio | 315.5% (target ≥90.0%) |
| Rows published (traces) | 482 |
| Sessions observed | 138 |
| Avg session duration (s) | 846.261 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.67 |
| Avg connector latency (ms) | 13875.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **315.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
