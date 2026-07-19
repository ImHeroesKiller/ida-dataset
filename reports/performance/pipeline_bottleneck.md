# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T23:11:34+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 122 | 1.0 | 6.5 | 122.4 |
| source_discovery | 122 | 3.07 | 39.8 | 375.0 |
| connector | 122 | 81731.81 | 97806.1 | 9971281.4 |
| document_discovery | 122 | 81731.95 | 97806.2 | 9971298.2 |
| document_download | 122 | 266168.42 | 1509355.9 | 32472547.5 |
| extraction | 122 | 82.53 | 274.0 | 10068.5 |
| candidate_validation | 122 | 8.07 | 30.0 | 984.4 |
| publish_queue | 122 | 8.25 | 34.7 | 1006.4 |
| append_dataset | 122 | 45.07 | 119.7 | 5498.9 |
| export | 122 | 0.34 | 0.7 | 41.4 |
| git_commit | 122 | 0.32 | 2.1 | 38.5 |
| push | 122 | 0.31 | 0.8 | 38.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3393 |
| Documents processed | 10315 |
| Process ratio | 304.0% (target ≥90.0%) |
| Rows published (traces) | 542 |
| Sessions observed | 150 |
| Avg session duration (s) | 865.3 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.704 |
| Avg connector latency (ms) | 14042.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **304.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
