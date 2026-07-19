# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T10:55:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 113 | 1.0 | 6.5 | 113.5 |
| source_discovery | 113 | 3.09 | 39.8 | 348.9 |
| connector | 113 | 80756.36 | 97806.1 | 9125468.2 |
| document_discovery | 113 | 80756.5 | 97806.2 | 9125484.0 |
| document_download | 113 | 266646.51 | 1509355.9 | 30131055.3 |
| extraction | 113 | 81.89 | 274.0 | 9253.9 |
| candidate_validation | 113 | 7.85 | 30.0 | 887.2 |
| publish_queue | 113 | 8.05 | 34.7 | 909.2 |
| append_dataset | 113 | 45.5 | 119.7 | 5141.8 |
| export | 113 | 0.34 | 0.7 | 37.9 |
| git_commit | 113 | 0.32 | 2.1 | 35.9 |
| push | 113 | 0.31 | 0.8 | 35.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3114 |
| Documents processed | 9722 |
| Process ratio | 312.2% (target ≥90.0%) |
| Rows published (traces) | 497 |
| Sessions observed | 141 |
| Avg session duration (s) | 850.709 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.679 |
| Avg connector latency (ms) | 13821.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **312.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
