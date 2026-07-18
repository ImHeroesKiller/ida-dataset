# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T21:12:52+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 106 | 1.02 | 6.5 | 107.9 |
| source_discovery | 106 | 2.78 | 3.5 | 294.2 |
| connector | 106 | 79880.87 | 97806.1 | 8467371.9 |
| document_discovery | 106 | 79881.01 | 97806.2 | 8467386.8 |
| document_download | 106 | 268065.36 | 1509355.9 | 28414928.5 |
| extraction | 106 | 83.07 | 274.0 | 8805.4 |
| candidate_validation | 106 | 7.59 | 18.7 | 804.9 |
| publish_queue | 106 | 7.8 | 34.7 | 826.9 |
| append_dataset | 106 | 46.56 | 119.7 | 4935.6 |
| export | 106 | 0.34 | 0.7 | 35.9 |
| git_commit | 106 | 0.32 | 2.1 | 34.0 |
| push | 106 | 0.31 | 0.8 | 33.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2907 |
| Documents processed | 9324 |
| Process ratio | 320.7% (target ≥90.0%) |
| Rows published (traces) | 462 |
| Sessions observed | 134 |
| Avg session duration (s) | 838.754 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.657 |
| Avg connector latency (ms) | 13965.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **320.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
