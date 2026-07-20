# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T04:11:14+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 124 | 1.0 | 6.5 | 124.4 |
| source_discovery | 124 | 3.07 | 39.8 | 380.9 |
| connector | 124 | 81927.83 | 97806.1 | 10159051.0 |
| document_discovery | 124 | 81927.97 | 97806.2 | 10159068.0 |
| document_download | 124 | 264083.02 | 1509355.9 | 32746294.6 |
| extraction | 124 | 82.65 | 274.0 | 10249.2 |
| candidate_validation | 124 | 8.13 | 30.0 | 1007.6 |
| publish_queue | 124 | 8.3 | 34.7 | 1029.7 |
| append_dataset | 124 | 44.93 | 119.7 | 5571.8 |
| export | 124 | 0.35 | 1.9 | 43.6 |
| git_commit | 124 | 0.32 | 2.1 | 39.6 |
| push | 124 | 0.31 | 0.8 | 38.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3445 |
| Documents processed | 10430 |
| Process ratio | 302.8% (target ≥90.0%) |
| Rows published (traces) | 552 |
| Sessions observed | 152 |
| Avg session duration (s) | 866.737 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.709 |
| Avg connector latency (ms) | 13736.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **302.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
