# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T15:27:35+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 195 | 0.99 | 6.5 | 193.1 |
| source_discovery | 195 | 3.07 | 39.8 | 599.4 |
| connector | 195 | 86322.47 | 97806.1 | 16832882.2 |
| document_discovery | 195 | 86322.62 | 97806.2 | 16832910.8 |
| document_download | 195 | 253482.74 | 1509355.9 | 49429134.3 |
| extraction | 195 | 88.87 | 274.0 | 17329.4 |
| candidate_validation | 195 | 10.06 | 37.2 | 1962.3 |
| publish_queue | 195 | 10.19 | 37.4 | 1986.7 |
| append_dataset | 195 | 42.78 | 119.7 | 8342.8 |
| export | 195 | 0.35 | 1.9 | 68.3 |
| git_commit | 195 | 0.31 | 2.1 | 60.8 |
| push | 195 | 0.32 | 0.8 | 61.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5616 |
| Documents processed | 14930 |
| Process ratio | 265.8% (target ≥90.0%) |
| Rows published (traces) | 907 |
| Sessions observed | 223 |
| Avg session duration (s) | 932.794 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.819 |
| Avg connector latency (ms) | 13654.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **265.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
