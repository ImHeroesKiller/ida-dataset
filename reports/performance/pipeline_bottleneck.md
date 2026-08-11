# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T19:31:38+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 398 | 1.5 | 70.9 | 596.4 |
| source_discovery | 398 | 4.35 | 186.3 | 1731.7 |
| connector | 398 | 90242.39 | 97806.1 | 35916470.0 |
| document_discovery | 398 | 90242.57 | 97806.2 | 35916544.3 |
| document_download | 398 | 236058.02 | 1509355.9 | 93951093.9 |
| extraction | 398 | 98.86 | 274.0 | 39346.5 |
| candidate_validation | 398 | 15.41 | 149.0 | 6134.7 |
| publish_queue | 398 | 15.48 | 149.1 | 6160.6 |
| append_dataset | 398 | 38.68 | 119.7 | 15395.2 |
| export | 398 | 0.35 | 2.7 | 139.7 |
| git_commit | 398 | 0.35 | 15.1 | 139.3 |
| push | 398 | 0.59 | 81.1 | 235.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11838 |
| Documents processed | 26195 |
| Process ratio | 221.3% (target ≥90.0%) |
| Rows published (traces) | 1919 |
| Sessions observed | 303 |
| Avg session duration (s) | 1057.211 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13721.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
