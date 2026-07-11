# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T22:14:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 23 | 0.93 | 1.3 | 21.3 |
| source_discovery | 23 | 2.57 | 3.3 | 59.1 |
| connector | 23 | 32733.27 | 97806.1 | 752865.3 |
| document_discovery | 23 | 32733.43 | 97806.2 | 752868.9 |
| document_download | 23 | 192539.22 | 1509355.9 | 4428402.1 |
| extraction | 23 | 44.07 | 109.5 | 1013.6 |
| candidate_validation | 23 | 4.28 | 7.3 | 98.5 |
| publish_queue | 23 | 4.38 | 8.8 | 100.8 |
| append_dataset | 23 | 24.58 | 119.7 | 565.3 |
| export | 23 | 0.32 | 0.6 | 7.4 |
| git_commit | 23 | 0.3 | 0.4 | 6.8 |
| push | 23 | 0.3 | 0.5 | 6.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 394 |
| Documents processed | 1108 |
| Process ratio | 281.2% (target ≥90.0%) |
| Rows published (traces) | 60 |
| Sessions observed | 51 |
| Avg session duration (s) | 360.529 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.471 |
| Avg connector latency (ms) | 13803.8 |
| Worker utilization (est) | 0.836 |
| Idle fraction (est) | 0.164 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **281.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
