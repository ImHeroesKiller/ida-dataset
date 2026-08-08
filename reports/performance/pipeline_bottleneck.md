# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T21:50:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 347 | 1.58 | 70.9 | 547.9 |
| source_discovery | 347 | 4.58 | 186.3 | 1588.9 |
| connector | 347 | 89690.42 | 97806.1 | 31122577.0 |
| document_discovery | 347 | 89690.62 | 97806.2 | 31122644.2 |
| document_download | 347 | 231791.61 | 1509355.9 | 80431689.9 |
| extraction | 347 | 96.91 | 274.0 | 33627.6 |
| candidate_validation | 347 | 14.11 | 136.9 | 4894.9 |
| publish_queue | 347 | 14.17 | 136.9 | 4918.7 |
| append_dataset | 347 | 39.23 | 119.7 | 13612.7 |
| export | 347 | 0.35 | 2.1 | 120.5 |
| git_commit | 347 | 0.35 | 15.1 | 123.1 |
| push | 347 | 0.63 | 81.1 | 219.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10277 |
| Documents processed | 23272 |
| Process ratio | 226.4% (target ≥90.0%) |
| Rows published (traces) | 1664 |
| Sessions observed | 307 |
| Avg session duration (s) | 1067.075 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.977 |
| Avg connector latency (ms) | 13821.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **226.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
