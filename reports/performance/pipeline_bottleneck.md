# Pipeline Bottleneck Analysis

**Generated:** 2026-07-23T16:48:41+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 161 | 0.99 | 6.5 | 159.2 |
| source_discovery | 161 | 3.12 | 39.8 | 501.6 |
| connector | 161 | 84706.76 | 97806.1 | 13637787.8 |
| document_discovery | 161 | 84706.91 | 97806.2 | 13637812.3 |
| document_download | 161 | 251695.01 | 1509355.9 | 40522896.0 |
| extraction | 161 | 86.67 | 274.0 | 13954.0 |
| candidate_validation | 161 | 9.13 | 30.0 | 1469.5 |
| publish_queue | 161 | 9.27 | 34.7 | 1493.2 |
| append_dataset | 161 | 43.83 | 119.7 | 7056.4 |
| export | 161 | 0.35 | 1.9 | 56.7 |
| git_commit | 161 | 0.31 | 2.1 | 50.6 |
| push | 161 | 0.31 | 0.8 | 50.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4572 |
| Documents processed | 12918 |
| Process ratio | 282.5% (target ≥90.0%) |
| Rows published (traces) | 737 |
| Sessions observed | 189 |
| Avg session duration (s) | 902.487 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.779 |
| Avg connector latency (ms) | 13779.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **282.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
