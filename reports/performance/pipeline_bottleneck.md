# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T06:37:49+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 73 | 1.04 | 6.5 | 75.6 |
| source_discovery | 73 | 2.74 | 3.3 | 199.8 |
| connector | 73 | 73483.3 | 97806.1 | 5364280.8 |
| document_discovery | 73 | 73483.44 | 97806.2 | 5364290.9 |
| document_download | 73 | 275398.82 | 1509355.9 | 20104113.9 |
| extraction | 73 | 82.11 | 274.0 | 5994.2 |
| candidate_validation | 73 | 6.72 | 18.7 | 490.2 |
| publish_queue | 73 | 6.98 | 34.7 | 509.5 |
| append_dataset | 73 | 51.07 | 119.7 | 3728.2 |
| export | 73 | 0.34 | 0.6 | 24.6 |
| git_commit | 73 | 0.32 | 2.1 | 23.7 |
| push | 73 | 0.32 | 0.8 | 23.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1894 |
| Documents processed | 7297 |
| Process ratio | 385.3% (target ≥90.0%) |
| Rows published (traces) | 297 |
| Sessions observed | 101 |
| Avg session duration (s) | 758.921 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.485 |
| Avg connector latency (ms) | 13638.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **385.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
