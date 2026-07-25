# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T20:28:32+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 186 | 0.99 | 6.5 | 184.2 |
| source_discovery | 186 | 3.08 | 39.8 | 573.7 |
| connector | 186 | 85951.31 | 97806.1 | 15986943.6 |
| document_discovery | 186 | 85951.46 | 97806.2 | 15986971.1 |
| document_download | 186 | 253559.56 | 1509355.9 | 47162078.7 |
| extraction | 186 | 88.17 | 274.0 | 16399.2 |
| candidate_validation | 186 | 9.72 | 30.0 | 1808.8 |
| publish_queue | 186 | 9.86 | 34.7 | 1833.1 |
| append_dataset | 186 | 43.04 | 119.7 | 8005.4 |
| export | 186 | 0.35 | 1.9 | 65.4 |
| git_commit | 186 | 0.31 | 2.1 | 58.0 |
| push | 186 | 0.32 | 0.8 | 58.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5347 |
| Documents processed | 14404 |
| Process ratio | 269.4% (target ≥90.0%) |
| Rows published (traces) | 862 |
| Sessions observed | 214 |
| Avg session duration (s) | 926.28 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.81 |
| Avg connector latency (ms) | 13766.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **269.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
