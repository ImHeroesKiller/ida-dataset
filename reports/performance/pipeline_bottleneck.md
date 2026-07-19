# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T21:12:28+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 120 | 1.0 | 6.5 | 120.4 |
| source_discovery | 120 | 3.08 | 39.8 | 369.3 |
| connector | 120 | 81527.15 | 97806.1 | 9783257.8 |
| document_discovery | 120 | 81527.29 | 97806.2 | 9783274.4 |
| document_download | 120 | 267022.62 | 1509355.9 | 32042713.9 |
| extraction | 120 | 82.36 | 274.0 | 9883.7 |
| candidate_validation | 120 | 8.01 | 30.0 | 961.5 |
| publish_queue | 120 | 8.2 | 34.7 | 983.5 |
| append_dataset | 120 | 45.16 | 119.7 | 5418.9 |
| export | 120 | 0.34 | 0.7 | 40.8 |
| git_commit | 120 | 0.32 | 2.1 | 37.9 |
| push | 120 | 0.31 | 0.8 | 37.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3331 |
| Documents processed | 10190 |
| Process ratio | 305.9% (target ≥90.0%) |
| Rows published (traces) | 532 |
| Sessions observed | 148 |
| Avg session duration (s) | 862.851 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.699 |
| Avg connector latency (ms) | 13701.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **305.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
