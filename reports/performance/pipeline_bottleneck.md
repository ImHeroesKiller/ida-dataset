# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T22:10:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 121 | 1.0 | 6.5 | 121.3 |
| source_discovery | 121 | 3.08 | 39.8 | 372.1 |
| connector | 121 | 81630.29 | 97806.1 | 9877265.6 |
| document_discovery | 121 | 81630.43 | 97806.2 | 9877282.3 |
| document_download | 121 | 267520.43 | 1509355.9 | 32369971.5 |
| extraction | 121 | 82.43 | 274.0 | 9974.5 |
| candidate_validation | 121 | 8.04 | 30.0 | 972.9 |
| publish_queue | 121 | 8.22 | 34.7 | 994.9 |
| append_dataset | 121 | 45.15 | 119.7 | 5463.2 |
| export | 121 | 0.34 | 0.7 | 41.1 |
| git_commit | 121 | 0.32 | 2.1 | 38.2 |
| push | 121 | 0.31 | 0.8 | 37.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3362 |
| Documents processed | 10264 |
| Process ratio | 305.3% (target ≥90.0%) |
| Rows published (traces) | 537 |
| Sessions observed | 149 |
| Avg session duration (s) | 864.826 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.702 |
| Avg connector latency (ms) | 13656.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **305.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
