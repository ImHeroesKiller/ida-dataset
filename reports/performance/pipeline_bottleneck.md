# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T23:15:09+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 262 | 1.26 | 70.9 | 329.3 |
| source_discovery | 262 | 3.72 | 186.3 | 975.4 |
| connector | 262 | 88291.85 | 97806.1 | 23132464.4 |
| document_discovery | 262 | 88292.06 | 97806.2 | 23132520.4 |
| document_download | 262 | 239195.62 | 1509355.9 | 62669252.0 |
| extraction | 262 | 92.92 | 274.0 | 24344.6 |
| candidate_validation | 262 | 12.07 | 102.5 | 3163.2 |
| publish_queue | 262 | 12.16 | 102.7 | 3185.3 |
| append_dataset | 262 | 41.18 | 119.7 | 10789.2 |
| export | 262 | 0.35 | 2.1 | 92.0 |
| git_commit | 262 | 0.37 | 15.1 | 96.6 |
| push | 262 | 0.62 | 81.1 | 163.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7672 |
| Documents processed | 18765 |
| Process ratio | 244.6% (target ≥90.0%) |
| Rows published (traces) | 1239 |
| Sessions observed | 290 |
| Avg session duration (s) | 955.662 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.855 |
| Avg connector latency (ms) | 13766.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **244.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
