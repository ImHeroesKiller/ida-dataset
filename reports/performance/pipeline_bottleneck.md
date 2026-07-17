# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T13:58:57+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 89 | 1.03 | 6.5 | 91.5 |
| source_discovery | 89 | 2.75 | 3.3 | 245.0 |
| connector | 89 | 77176.83 | 97806.1 | 6868737.8 |
| document_discovery | 89 | 77176.98 | 97806.2 | 6868751.1 |
| document_download | 89 | 275485.23 | 1509355.9 | 24518185.3 |
| extraction | 89 | 83.1 | 274.0 | 7396.0 |
| candidate_validation | 89 | 7.15 | 18.7 | 636.1 |
| publish_queue | 89 | 7.37 | 34.7 | 655.8 |
| append_dataset | 89 | 48.2 | 119.7 | 4289.4 |
| export | 89 | 0.34 | 0.6 | 29.9 |
| git_commit | 89 | 0.32 | 2.1 | 28.6 |
| push | 89 | 0.32 | 0.8 | 28.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2390 |
| Documents processed | 8208 |
| Process ratio | 343.4% (target ≥90.0%) |
| Rows published (traces) | 377 |
| Sessions observed | 117 |
| Avg session duration (s) | 806.026 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.585 |
| Avg connector latency (ms) | 13733.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **343.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
