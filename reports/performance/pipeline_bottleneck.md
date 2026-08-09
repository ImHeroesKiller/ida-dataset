# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T05:23:49+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 352 | 1.57 | 70.9 | 553.1 |
| source_discovery | 352 | 4.56 | 186.3 | 1603.8 |
| connector | 352 | 89754.0 | 97806.1 | 31593409.1 |
| document_discovery | 352 | 89754.2 | 97806.2 | 31593476.8 |
| document_download | 352 | 231899.07 | 1509355.9 | 81628471.3 |
| extraction | 352 | 97.08 | 274.0 | 34173.3 |
| candidate_validation | 352 | 14.21 | 136.9 | 5001.2 |
| publish_queue | 352 | 14.28 | 136.9 | 5025.4 |
| append_dataset | 352 | 39.17 | 119.7 | 13786.3 |
| export | 352 | 0.35 | 2.1 | 122.3 |
| git_commit | 352 | 0.35 | 15.1 | 124.6 |
| push | 352 | 0.63 | 81.1 | 221.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10432 |
| Documents processed | 23551 |
| Process ratio | 225.8% (target ≥90.0%) |
| Rows published (traces) | 1689 |
| Sessions observed | 303 |
| Avg session duration (s) | 1065.898 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13717.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
