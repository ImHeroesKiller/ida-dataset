# Pipeline Bottleneck Analysis

**Generated:** 2026-07-23T06:14:37+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 157 | 0.99 | 6.5 | 155.3 |
| source_discovery | 157 | 3.12 | 39.8 | 490.2 |
| connector | 157 | 84470.37 | 97806.1 | 13261848.6 |
| document_discovery | 157 | 84470.53 | 97806.2 | 13261872.6 |
| document_download | 157 | 252156.64 | 1509355.9 | 39588591.8 |
| extraction | 157 | 86.33 | 274.0 | 13554.4 |
| candidate_validation | 157 | 9.01 | 30.0 | 1414.8 |
| publish_queue | 157 | 9.16 | 34.7 | 1438.6 |
| append_dataset | 157 | 43.8 | 119.7 | 6876.6 |
| export | 157 | 0.35 | 1.9 | 55.2 |
| git_commit | 157 | 0.31 | 2.1 | 49.4 |
| push | 157 | 0.31 | 0.8 | 49.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4448 |
| Documents processed | 12622 |
| Process ratio | 283.8% (target ≥90.0%) |
| Rows published (traces) | 717 |
| Sessions observed | 185 |
| Avg session duration (s) | 898.762 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.773 |
| Avg connector latency (ms) | 15020.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **283.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
