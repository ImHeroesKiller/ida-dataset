# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T22:30:49+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 293 | 1.36 | 70.9 | 399.9 |
| source_discovery | 293 | 4.35 | 186.3 | 1273.6 |
| connector | 293 | 88897.57 | 97806.1 | 26046986.9 |
| document_discovery | 293 | 88897.77 | 97806.2 | 26047047.2 |
| document_download | 293 | 234644.15 | 1509355.9 | 68750734.5 |
| extraction | 293 | 94.13 | 274.0 | 27578.8 |
| candidate_validation | 293 | 12.67 | 102.5 | 3711.9 |
| publish_queue | 293 | 12.75 | 102.7 | 3734.3 |
| append_dataset | 293 | 40.28 | 119.7 | 11801.3 |
| export | 293 | 0.35 | 2.1 | 101.9 |
| git_commit | 293 | 0.36 | 15.1 | 105.9 |
| push | 293 | 0.7 | 81.1 | 204.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8633 |
| Documents processed | 20355 |
| Process ratio | 235.8% (target ≥90.0%) |
| Rows published (traces) | 1394 |
| Sessions observed | 321 |
| Avg session duration (s) | 960.96 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.871 |
| Avg connector latency (ms) | 13812.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **235.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
