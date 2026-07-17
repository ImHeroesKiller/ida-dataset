# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T17:32:48+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 91 | 1.02 | 6.5 | 92.9 |
| source_discovery | 91 | 2.75 | 3.3 | 250.1 |
| connector | 91 | 77548.09 | 97806.1 | 7056876.5 |
| document_discovery | 91 | 77548.24 | 97806.2 | 7056890.0 |
| document_download | 91 | 273143.76 | 1509355.9 | 24856082.6 |
| extraction | 91 | 83.07 | 274.0 | 7559.4 |
| candidate_validation | 91 | 7.17 | 18.7 | 652.1 |
| publish_queue | 91 | 7.38 | 34.7 | 671.8 |
| append_dataset | 91 | 47.85 | 119.7 | 4354.4 |
| export | 91 | 0.34 | 0.6 | 30.6 |
| git_commit | 91 | 0.32 | 2.1 | 29.1 |
| push | 91 | 0.31 | 0.8 | 28.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2442 |
| Documents processed | 8346 |
| Process ratio | 341.8% (target ≥90.0%) |
| Rows published (traces) | 387 |
| Sessions observed | 119 |
| Avg session duration (s) | 809.336 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.595 |
| Avg connector latency (ms) | 13723.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **341.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
