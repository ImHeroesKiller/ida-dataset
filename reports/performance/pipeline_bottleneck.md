# Pipeline Bottleneck Analysis

**Generated:** 2026-08-03T20:45:22+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 282 | 1.38 | 70.9 | 389.7 |
| source_discovery | 282 | 4.14 | 186.3 | 1168.4 |
| connector | 282 | 88698.02 | 97806.1 | 25012842.5 |
| document_discovery | 282 | 88698.23 | 97806.2 | 25012901.5 |
| document_download | 282 | 235921.03 | 1509355.9 | 66529731.0 |
| extraction | 282 | 93.64 | 274.0 | 26406.4 |
| candidate_validation | 282 | 12.49 | 102.5 | 3522.4 |
| publish_queue | 282 | 12.57 | 102.7 | 3544.9 |
| append_dataset | 282 | 40.63 | 119.7 | 11459.0 |
| export | 282 | 0.35 | 2.1 | 98.5 |
| git_commit | 282 | 0.36 | 15.1 | 102.5 |
| push | 282 | 0.6 | 81.1 | 169.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8292 |
| Documents processed | 19796 |
| Process ratio | 238.7% (target ≥90.0%) |
| Rows published (traces) | 1339 |
| Sessions observed | 310 |
| Avg session duration (s) | 959.106 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.865 |
| Avg connector latency (ms) | 13661.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **238.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
