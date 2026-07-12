# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T19:36:28+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 36 | 1.11 | 6.5 | 40.0 |
| source_discovery | 36 | 2.66 | 3.3 | 95.7 |
| connector | 36 | 52407.63 | 97806.1 | 1886674.6 |
| document_discovery | 36 | 52407.77 | 97806.2 | 1886679.9 |
| document_download | 36 | 211635.74 | 1509355.9 | 7618886.8 |
| extraction | 36 | 61.49 | 109.5 | 2213.6 |
| candidate_validation | 36 | 5.07 | 8.7 | 182.4 |
| publish_queue | 36 | 5.13 | 8.8 | 184.8 |
| append_dataset | 36 | 39.37 | 119.7 | 1417.2 |
| export | 36 | 0.32 | 0.6 | 11.6 |
| git_commit | 36 | 0.35 | 2.1 | 12.5 |
| push | 36 | 0.31 | 0.6 | 11.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 787 |
| Documents processed | 2809 |
| Process ratio | 356.9% (target ≥90.0%) |
| Rows published (traces) | 116 |
| Sessions observed | 64 |
| Avg session duration (s) | 506.391 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.966 |
| Avg connector latency (ms) | 13706.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **356.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
