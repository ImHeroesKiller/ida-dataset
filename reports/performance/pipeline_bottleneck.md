# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T10:16:58+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 87 | 1.03 | 6.5 | 89.6 |
| source_discovery | 87 | 2.75 | 3.3 | 239.4 |
| connector | 87 | 76790.26 | 97806.1 | 6680752.2 |
| document_discovery | 87 | 76790.4 | 97806.2 | 6680765.2 |
| document_download | 87 | 263376.92 | 1509355.9 | 22913791.9 |
| extraction | 87 | 82.99 | 274.0 | 7220.1 |
| candidate_validation | 87 | 7.08 | 18.7 | 615.9 |
| publish_queue | 87 | 7.3 | 34.7 | 635.5 |
| append_dataset | 87 | 48.54 | 119.7 | 4222.9 |
| export | 87 | 0.34 | 0.6 | 29.3 |
| git_commit | 87 | 0.32 | 2.1 | 28.0 |
| push | 87 | 0.32 | 0.8 | 27.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2328 |
| Documents processed | 8105 |
| Process ratio | 348.2% (target ≥90.0%) |
| Rows published (traces) | 367 |
| Sessions observed | 115 |
| Avg session duration (s) | 791.435 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.575 |
| Avg connector latency (ms) | 13954.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **348.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
