# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T15:48:42+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 341 | 1.59 | 70.9 | 541.8 |
| source_discovery | 341 | 4.61 | 186.3 | 1571.7 |
| connector | 341 | 89614.71 | 97806.1 | 30558616.8 |
| document_discovery | 341 | 89614.91 | 97806.2 | 30558683.0 |
| document_download | 341 | 231537.58 | 1509355.9 | 78954314.2 |
| extraction | 341 | 96.68 | 274.0 | 32967.8 |
| candidate_validation | 341 | 13.99 | 136.9 | 4772.2 |
| publish_queue | 341 | 14.06 | 136.9 | 4795.9 |
| append_dataset | 341 | 39.35 | 119.7 | 13416.9 |
| export | 341 | 0.35 | 2.1 | 118.5 |
| git_commit | 341 | 0.35 | 15.1 | 121.0 |
| push | 341 | 0.64 | 81.1 | 218.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10101 |
| Documents processed | 22946 |
| Process ratio | 227.2% (target ≥90.0%) |
| Rows published (traces) | 1634 |
| Sessions observed | 301 |
| Avg session duration (s) | 1066.226 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.977 |
| Avg connector latency (ms) | 14142.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **227.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
