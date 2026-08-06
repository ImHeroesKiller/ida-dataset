# Pipeline Bottleneck Analysis

**Generated:** 2026-08-06T06:09:47+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 306 | 1.52 | 70.9 | 466.5 |
| source_discovery | 306 | 4.28 | 186.3 | 1310.7 |
| connector | 306 | 89112.18 | 97806.1 | 27268328.5 |
| document_discovery | 306 | 89112.39 | 97806.2 | 27268390.3 |
| document_download | 306 | 234029.0 | 1509355.9 | 71612874.6 |
| extraction | 306 | 95.07 | 274.0 | 29092.1 |
| candidate_validation | 306 | 12.94 | 102.5 | 3960.8 |
| publish_queue | 306 | 13.02 | 102.7 | 3983.6 |
| append_dataset | 306 | 40.0 | 119.7 | 12241.2 |
| export | 306 | 0.35 | 2.1 | 106.2 |
| git_commit | 306 | 0.36 | 15.1 | 110.0 |
| push | 306 | 0.68 | 81.1 | 208.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9026 |
| Documents processed | 21020 |
| Process ratio | 232.9% (target ≥90.0%) |
| Rows published (traces) | 1459 |
| Sessions observed | 302 |
| Avg session duration (s) | 1058.377 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.928 |
| Avg connector latency (ms) | 13916.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **232.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
