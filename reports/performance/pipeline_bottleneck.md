# Pipeline Bottleneck Analysis

**Generated:** 2026-08-03T03:13:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 275 | 1.39 | 70.9 | 382.3 |
| source_discovery | 275 | 4.17 | 186.3 | 1147.6 |
| connector | 275 | 88561.51 | 97806.1 | 24354416.2 |
| document_discovery | 275 | 88561.72 | 97806.2 | 24354474.2 |
| document_download | 275 | 237812.37 | 1509355.9 | 65398402.0 |
| extraction | 275 | 93.35 | 274.0 | 25670.0 |
| candidate_validation | 275 | 12.33 | 102.5 | 3391.3 |
| publish_queue | 275 | 12.41 | 102.7 | 3413.6 |
| append_dataset | 275 | 40.82 | 119.7 | 11226.1 |
| export | 275 | 0.35 | 2.1 | 96.2 |
| git_commit | 275 | 0.36 | 15.1 | 100.3 |
| push | 275 | 0.61 | 81.1 | 167.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8075 |
| Documents processed | 19468 |
| Process ratio | 241.1% (target ≥90.0%) |
| Rows published (traces) | 1304 |
| Sessions observed | 303 |
| Avg session duration (s) | 959.175 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.862 |
| Avg connector latency (ms) | 13821.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **241.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
