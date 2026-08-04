# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T13:18:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 289 | 1.37 | 70.9 | 396.3 |
| source_discovery | 289 | 4.37 | 186.3 | 1263.3 |
| connector | 289 | 88828.32 | 97806.1 | 25671385.5 |
| document_discovery | 289 | 88828.53 | 97806.2 | 25671445.4 |
| document_download | 289 | 235491.81 | 1509355.9 | 68057133.8 |
| extraction | 289 | 93.96 | 274.0 | 27155.7 |
| candidate_validation | 289 | 12.61 | 102.5 | 3643.6 |
| publish_queue | 289 | 12.68 | 102.7 | 3665.9 |
| append_dataset | 289 | 40.39 | 119.7 | 11673.0 |
| export | 289 | 0.35 | 2.1 | 100.8 |
| git_commit | 289 | 0.36 | 15.1 | 104.8 |
| push | 289 | 0.7 | 81.1 | 203.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8509 |
| Documents processed | 20137 |
| Process ratio | 236.7% (target ≥90.0%) |
| Rows published (traces) | 1374 |
| Sessions observed | 317 |
| Avg session duration (s) | 960.461 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.869 |
| Avg connector latency (ms) | 13966.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **236.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
