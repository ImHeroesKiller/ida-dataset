# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T13:25:28+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 394 | 1.51 | 70.9 | 593.0 |
| source_discovery | 394 | 4.37 | 186.3 | 1721.1 |
| connector | 394 | 90203.97 | 97806.1 | 35540363.1 |
| document_discovery | 394 | 90204.15 | 97806.2 | 35540436.8 |
| document_download | 394 | 236685.71 | 1509355.9 | 93254170.5 |
| extraction | 394 | 98.66 | 274.0 | 38873.5 |
| candidate_validation | 394 | 15.35 | 149.0 | 6049.8 |
| publish_queue | 394 | 15.42 | 149.1 | 6075.6 |
| append_dataset | 394 | 38.74 | 119.7 | 15262.0 |
| export | 394 | 0.35 | 2.7 | 138.4 |
| git_commit | 394 | 0.35 | 15.1 | 137.7 |
| push | 394 | 0.59 | 81.1 | 234.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11714 |
| Documents processed | 25958 |
| Process ratio | 221.6% (target ≥90.0%) |
| Rows published (traces) | 1899 |
| Sessions observed | 312 |
| Avg session duration (s) | 1061.048 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13883.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
