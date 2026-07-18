# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T13:37:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 101 | 1.02 | 6.5 | 102.9 |
| source_discovery | 101 | 2.77 | 3.5 | 279.4 |
| connector | 101 | 79178.28 | 97806.1 | 7997006.4 |
| document_discovery | 101 | 79178.42 | 97806.2 | 7997020.8 |
| document_download | 101 | 264183.85 | 1509355.9 | 26682569.3 |
| extraction | 101 | 83.39 | 274.0 | 8422.0 |
| candidate_validation | 101 | 7.45 | 18.7 | 752.9 |
| publish_queue | 101 | 7.67 | 34.7 | 774.6 |
| append_dataset | 101 | 46.83 | 119.7 | 4729.6 |
| export | 101 | 0.34 | 0.6 | 34.0 |
| git_commit | 101 | 0.32 | 2.1 | 32.5 |
| push | 101 | 0.31 | 0.8 | 31.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2752 |
| Documents processed | 8962 |
| Process ratio | 325.7% (target ≥90.0%) |
| Rows published (traces) | 437 |
| Sessions observed | 129 |
| Avg session duration (s) | 825.31 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.638 |
| Avg connector latency (ms) | 13734.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **325.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
