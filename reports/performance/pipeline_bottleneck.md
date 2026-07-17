# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T00:26:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 83 | 1.03 | 6.5 | 85.4 |
| source_discovery | 83 | 2.74 | 3.3 | 227.8 |
| connector | 83 | 75959.42 | 97806.1 | 6304632.1 |
| document_discovery | 83 | 75959.57 | 97806.2 | 6304644.6 |
| document_download | 83 | 264587.73 | 1509355.9 | 21960781.9 |
| extraction | 83 | 82.82 | 274.0 | 6874.0 |
| candidate_validation | 83 | 6.98 | 18.7 | 579.6 |
| publish_queue | 83 | 7.22 | 34.7 | 599.2 |
| append_dataset | 83 | 49.14 | 119.7 | 4078.6 |
| export | 83 | 0.34 | 0.6 | 27.9 |
| git_commit | 83 | 0.32 | 2.1 | 26.8 |
| push | 83 | 0.32 | 0.8 | 26.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2204 |
| Documents processed | 7856 |
| Process ratio | 356.4% (target ≥90.0%) |
| Rows published (traces) | 347 |
| Sessions observed | 111 |
| Avg session duration (s) | 780.901 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.553 |
| Avg connector latency (ms) | 13875.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **356.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
