# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T22:21:02+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 187 | 0.99 | 6.5 | 185.3 |
| source_discovery | 187 | 3.08 | 39.8 | 576.4 |
| connector | 187 | 85994.97 | 97806.1 | 16081058.6 |
| document_discovery | 187 | 85995.11 | 97806.2 | 16081086.2 |
| document_download | 187 | 252906.96 | 1509355.9 | 47293601.1 |
| extraction | 187 | 88.26 | 274.0 | 16503.8 |
| candidate_validation | 187 | 9.75 | 30.0 | 1823.2 |
| publish_queue | 187 | 9.88 | 34.7 | 1847.5 |
| append_dataset | 187 | 43.02 | 119.7 | 8045.4 |
| export | 187 | 0.35 | 1.9 | 65.7 |
| git_commit | 187 | 0.31 | 2.1 | 58.3 |
| push | 187 | 0.32 | 0.8 | 59.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5378 |
| Documents processed | 14466 |
| Process ratio | 269.0% (target ≥90.0%) |
| Rows published (traces) | 867 |
| Sessions observed | 215 |
| Avg session duration (s) | 926.47 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.811 |
| Avg connector latency (ms) | 13806.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **269.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
