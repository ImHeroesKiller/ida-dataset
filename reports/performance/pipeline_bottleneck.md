# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T08:45:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 29 | 0.97 | 1.4 | 28.0 |
| source_discovery | 29 | 2.62 | 3.3 | 75.9 |
| connector | 29 | 42377.08 | 97806.1 | 1228935.4 |
| document_discovery | 29 | 42377.23 | 97806.2 | 1228939.8 |
| document_download | 29 | 201148.39 | 1509355.9 | 5833303.2 |
| extraction | 29 | 53.92 | 109.5 | 1563.7 |
| candidate_validation | 29 | 4.69 | 7.8 | 135.9 |
| publish_queue | 29 | 4.77 | 8.8 | 138.2 |
| append_dataset | 29 | 33.9 | 119.7 | 983.0 |
| export | 29 | 0.32 | 0.6 | 9.4 |
| git_commit | 29 | 0.3 | 0.4 | 8.6 |
| push | 29 | 0.31 | 0.5 | 8.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 570 |
| Documents processed | 1922 |
| Process ratio | 337.2% (target ≥90.0%) |
| Rows published (traces) | 85 |
| Sessions observed | 57 |
| Avg session duration (s) | 431.561 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.818 |
| Avg connector latency (ms) | 13682.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **337.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
