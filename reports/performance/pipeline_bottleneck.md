# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T09:45:25+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 137 | 1.0 | 6.5 | 137.2 |
| source_discovery | 137 | 3.16 | 39.8 | 433.4 |
| connector | 137 | 83072.3 | 97806.1 | 11380905.4 |
| document_discovery | 137 | 83072.44 | 97806.2 | 11380924.5 |
| document_download | 137 | 255744.38 | 1509355.9 | 35036980.1 |
| extraction | 137 | 84.76 | 274.0 | 11612.1 |
| candidate_validation | 137 | 8.45 | 30.0 | 1157.7 |
| publish_queue | 137 | 8.62 | 34.7 | 1180.5 |
| append_dataset | 137 | 44.34 | 119.7 | 6075.2 |
| export | 137 | 0.35 | 1.9 | 47.9 |
| git_commit | 137 | 0.32 | 2.1 | 43.4 |
| push | 137 | 0.31 | 0.8 | 43.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3838 |
| Documents processed | 11267 |
| Process ratio | 293.6% (target ≥90.0%) |
| Rows published (traces) | 617 |
| Sessions observed | 165 |
| Avg session duration (s) | 878.406 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.738 |
| Avg connector latency (ms) | 14008.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **293.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
