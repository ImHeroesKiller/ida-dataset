# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T06:23:11+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 264 | 1.25 | 70.9 | 331.0 |
| source_discovery | 264 | 3.72 | 186.3 | 980.8 |
| connector | 264 | 88336.1 | 97806.1 | 23320729.7 |
| document_discovery | 264 | 88336.31 | 97806.2 | 23320786.1 |
| document_download | 264 | 238650.59 | 1509355.9 | 63003756.0 |
| extraction | 264 | 92.96 | 274.0 | 24541.3 |
| candidate_validation | 264 | 12.1 | 102.5 | 3194.9 |
| publish_queue | 264 | 12.19 | 102.7 | 3217.0 |
| append_dataset | 264 | 41.07 | 119.7 | 10842.4 |
| export | 264 | 0.35 | 2.1 | 92.5 |
| git_commit | 264 | 0.37 | 15.1 | 97.2 |
| push | 264 | 0.62 | 81.1 | 163.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7734 |
| Documents processed | 18858 |
| Process ratio | 243.8% (target ≥90.0%) |
| Rows published (traces) | 1249 |
| Sessions observed | 292 |
| Avg session duration (s) | 955.387 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.856 |
| Avg connector latency (ms) | 13669.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **243.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
