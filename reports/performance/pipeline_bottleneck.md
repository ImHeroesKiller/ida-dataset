# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T00:24:09+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 284 | 1.38 | 70.9 | 391.5 |
| source_discovery | 284 | 4.13 | 186.3 | 1174.1 |
| connector | 284 | 88734.24 | 97806.1 | 25200523.4 |
| document_discovery | 284 | 88734.45 | 97806.2 | 25200582.7 |
| document_download | 284 | 235265.27 | 1509355.9 | 66815335.3 |
| extraction | 284 | 93.74 | 274.0 | 26621.8 |
| candidate_validation | 284 | 12.53 | 102.5 | 3559.2 |
| publish_queue | 284 | 12.61 | 102.7 | 3581.8 |
| append_dataset | 284 | 40.58 | 119.7 | 11523.4 |
| export | 284 | 0.35 | 2.1 | 99.1 |
| git_commit | 284 | 0.36 | 15.1 | 103.1 |
| push | 284 | 0.6 | 81.1 | 170.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8354 |
| Documents processed | 19889 |
| Process ratio | 238.1% (target ≥90.0%) |
| Rows published (traces) | 1349 |
| Sessions observed | 312 |
| Avg session duration (s) | 959.41 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.866 |
| Avg connector latency (ms) | 13886.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **238.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
