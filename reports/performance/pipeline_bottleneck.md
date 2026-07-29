# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T06:50:53+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 221 | 1.31 | 70.9 | 289.5 |
| source_discovery | 221 | 3.89 | 186.3 | 859.0 |
| connector | 221 | 87233.17 | 97806.1 | 19278531.4 |
| document_discovery | 221 | 87233.32 | 97806.2 | 19278563.5 |
| document_download | 221 | 247598.3 | 1509355.9 | 54719224.6 |
| extraction | 221 | 91.08 | 274.0 | 20127.7 |
| candidate_validation | 221 | 10.72 | 37.2 | 2369.8 |
| publish_queue | 221 | 10.84 | 37.4 | 2395.0 |
| append_dataset | 221 | 42.08 | 119.7 | 9299.2 |
| export | 221 | 0.35 | 1.9 | 76.9 |
| git_commit | 221 | 0.31 | 2.1 | 68.9 |
| push | 221 | 0.31 | 0.8 | 69.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6412 |
| Documents processed | 16415 |
| Process ratio | 256.0% (target ≥90.0%) |
| Rows published (traces) | 1034 |
| Sessions observed | 249 |
| Avg session duration (s) | 944.546 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.827 |
| Avg connector latency (ms) | 13712.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **256.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
