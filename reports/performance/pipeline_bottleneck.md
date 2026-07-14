# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T15:13:47+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 55 | 1.07 | 6.5 | 58.6 |
| source_discovery | 55 | 2.71 | 3.3 | 149.3 |
| connector | 55 | 66769.19 | 97806.1 | 3672305.7 |
| document_discovery | 55 | 66769.34 | 97806.2 | 3672313.5 |
| document_download | 55 | 234113.45 | 1509355.9 | 12876239.9 |
| extraction | 55 | 77.47 | 274.0 | 4261.0 |
| candidate_validation | 55 | 5.99 | 9.5 | 329.5 |
| publish_queue | 55 | 6.04 | 9.5 | 332.2 |
| append_dataset | 55 | 47.4 | 119.7 | 2606.8 |
| export | 55 | 0.34 | 0.6 | 18.8 |
| git_commit | 55 | 0.33 | 2.1 | 18.3 |
| push | 55 | 0.32 | 0.8 | 17.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1356 |
| Documents processed | 5093 |
| Process ratio | 375.6% (target ≥90.0%) |
| Rows published (traces) | 207 |
| Sessions observed | 83 |
| Avg session duration (s) | 648.53 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.292 |
| Avg connector latency (ms) | 14156.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **375.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
