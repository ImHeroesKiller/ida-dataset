# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T22:17:27+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 94 | 1.02 | 6.5 | 95.9 |
| source_discovery | 94 | 2.75 | 3.3 | 258.7 |
| connector | 94 | 78075.58 | 97806.1 | 7339104.6 |
| document_discovery | 94 | 78075.73 | 97806.2 | 7339118.3 |
| document_download | 94 | 271448.6 | 1509355.9 | 25516168.7 |
| extraction | 94 | 83.18 | 274.0 | 7818.5 |
| candidate_validation | 94 | 7.25 | 18.7 | 681.7 |
| publish_queue | 94 | 7.46 | 34.7 | 701.7 |
| append_dataset | 94 | 47.56 | 119.7 | 4470.6 |
| export | 94 | 0.34 | 0.6 | 31.6 |
| git_commit | 94 | 0.32 | 2.1 | 30.0 |
| push | 94 | 0.31 | 0.8 | 29.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2535 |
| Documents processed | 8542 |
| Process ratio | 337.0% (target ≥90.0%) |
| Rows published (traces) | 402 |
| Sessions observed | 122 |
| Avg session duration (s) | 815.336 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.609 |
| Avg connector latency (ms) | 13975.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **337.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
