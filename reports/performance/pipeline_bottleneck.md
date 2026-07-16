# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T11:57:24+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 76 | 1.04 | 6.5 | 78.7 |
| source_discovery | 76 | 2.74 | 3.3 | 208.5 |
| connector | 76 | 74291.01 | 97806.1 | 5646116.4 |
| document_discovery | 76 | 74291.14 | 97806.2 | 5646127.0 |
| document_download | 76 | 271502.96 | 1509355.9 | 20634225.3 |
| extraction | 76 | 82.49 | 274.0 | 6269.1 |
| candidate_validation | 76 | 6.83 | 18.7 | 518.7 |
| publish_queue | 76 | 7.08 | 34.7 | 538.1 |
| append_dataset | 76 | 50.71 | 119.7 | 3854.3 |
| export | 76 | 0.34 | 0.6 | 25.6 |
| git_commit | 76 | 0.33 | 2.1 | 24.7 |
| push | 76 | 0.32 | 0.8 | 24.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1987 |
| Documents processed | 7496 |
| Process ratio | 377.3% (target ≥90.0%) |
| Rows published (traces) | 312 |
| Sessions observed | 104 |
| Avg session duration (s) | 766.231 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.507 |
| Avg connector latency (ms) | 13726.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **377.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
