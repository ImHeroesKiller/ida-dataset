# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T11:06:22+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 53 | 1.08 | 6.5 | 57.4 |
| source_discovery | 53 | 2.73 | 3.3 | 144.7 |
| connector | 53 | 65743.24 | 97806.1 | 3484391.9 |
| document_discovery | 53 | 65743.38 | 97806.2 | 3484399.3 |
| document_download | 53 | 227075.79 | 1509355.9 | 12035016.9 |
| extraction | 53 | 73.29 | 109.5 | 3884.5 |
| candidate_validation | 53 | 5.92 | 8.7 | 313.9 |
| publish_queue | 53 | 5.98 | 8.8 | 316.7 |
| append_dataset | 53 | 47.58 | 119.7 | 2521.6 |
| export | 53 | 0.35 | 0.6 | 18.4 |
| git_commit | 53 | 0.33 | 2.1 | 17.7 |
| push | 53 | 0.33 | 0.8 | 17.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1294 |
| Documents processed | 4837 |
| Process ratio | 373.8% (target ≥90.0%) |
| Rows published (traces) | 197 |
| Sessions observed | 81 |
| Avg session duration (s) | 636.753 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.261 |
| Avg connector latency (ms) | 13791.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **373.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
