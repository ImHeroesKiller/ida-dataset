# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T21:15:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 383 | 1.52 | 70.9 | 582.0 |
| source_discovery | 383 | 4.41 | 186.3 | 1689.2 |
| connector | 383 | 90094.51 | 97806.1 | 34506196.1 |
| document_discovery | 383 | 90094.7 | 97806.2 | 34506268.6 |
| document_download | 383 | 238259.14 | 1509355.9 | 91253250.1 |
| extraction | 383 | 98.27 | 274.0 | 37638.3 |
| candidate_validation | 383 | 15.12 | 149.0 | 5789.4 |
| publish_queue | 383 | 15.18 | 149.1 | 5814.6 |
| append_dataset | 383 | 38.79 | 119.7 | 14857.2 |
| export | 383 | 0.35 | 2.7 | 135.1 |
| git_commit | 383 | 0.35 | 15.1 | 134.4 |
| push | 383 | 0.6 | 81.1 | 230.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11383 |
| Documents processed | 25330 |
| Process ratio | 222.5% (target ≥90.0%) |
| Rows published (traces) | 1844 |
| Sessions observed | 301 |
| Avg session duration (s) | 1062.528 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13772.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
