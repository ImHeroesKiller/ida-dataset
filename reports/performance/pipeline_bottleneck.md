# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T15:22:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 151 | 0.99 | 6.5 | 149.8 |
| source_discovery | 151 | 3.13 | 39.8 | 473.1 |
| connector | 151 | 84086.28 | 97806.1 | 12697028.6 |
| document_discovery | 151 | 84086.44 | 97806.2 | 12697051.8 |
| document_download | 151 | 252343.87 | 1509355.9 | 38103924.7 |
| extraction | 151 | 85.96 | 274.0 | 12980.3 |
| candidate_validation | 151 | 8.85 | 30.0 | 1336.8 |
| publish_queue | 151 | 9.01 | 34.7 | 1360.4 |
| append_dataset | 151 | 43.93 | 119.7 | 6633.8 |
| export | 151 | 0.35 | 1.9 | 52.3 |
| git_commit | 151 | 0.31 | 2.1 | 47.5 |
| push | 151 | 0.31 | 0.8 | 47.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4272 |
| Documents processed | 12234 |
| Process ratio | 286.4% (target ≥90.0%) |
| Rows published (traces) | 687 |
| Sessions observed | 179 |
| Avg session duration (s) | 892.531 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.764 |
| Avg connector latency (ms) | 13921.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **286.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
