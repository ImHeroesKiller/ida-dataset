# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T16:22:13+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 117 | 1.0 | 6.5 | 117.4 |
| source_discovery | 117 | 3.08 | 39.8 | 360.7 |
| connector | 117 | 81208.25 | 97806.1 | 9501365.8 |
| document_discovery | 117 | 81208.39 | 97806.2 | 9501382.0 |
| document_download | 117 | 268660.36 | 1509355.9 | 31433262.6 |
| extraction | 117 | 82.13 | 274.0 | 9609.7 |
| candidate_validation | 117 | 7.96 | 30.0 | 930.8 |
| publish_queue | 117 | 8.14 | 34.7 | 952.8 |
| append_dataset | 117 | 45.41 | 119.7 | 5312.6 |
| export | 117 | 0.34 | 0.7 | 39.5 |
| git_commit | 117 | 0.32 | 2.1 | 37.1 |
| push | 117 | 0.31 | 0.8 | 36.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3238 |
| Documents processed | 10014 |
| Process ratio | 309.3% (target ≥90.0%) |
| Rows published (traces) | 517 |
| Sessions observed | 145 |
| Avg session duration (s) | 859.31 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.691 |
| Avg connector latency (ms) | 13800.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **309.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
