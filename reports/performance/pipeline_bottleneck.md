# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T18:22:09+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 185 | 0.99 | 6.5 | 183.2 |
| source_discovery | 185 | 3.08 | 39.8 | 570.7 |
| connector | 185 | 85909.19 | 97806.1 | 15893199.7 |
| document_discovery | 185 | 85909.34 | 97806.2 | 15893227.1 |
| document_download | 185 | 253643.92 | 1509355.9 | 46924125.2 |
| extraction | 185 | 88.07 | 274.0 | 16293.6 |
| candidate_validation | 185 | 9.7 | 30.0 | 1794.1 |
| publish_queue | 185 | 9.83 | 34.7 | 1818.3 |
| append_dataset | 185 | 43.05 | 119.7 | 7964.6 |
| export | 185 | 0.35 | 1.9 | 65.0 |
| git_commit | 185 | 0.31 | 2.1 | 57.7 |
| push | 185 | 0.32 | 0.8 | 58.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5316 |
| Documents processed | 14342 |
| Process ratio | 269.8% (target ≥90.0%) |
| Rows published (traces) | 857 |
| Sessions observed | 213 |
| Avg session duration (s) | 925.62 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.809 |
| Avg connector latency (ms) | 13790.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **269.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
