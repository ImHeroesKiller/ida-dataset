# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T12:35:34+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 54 | 1.07 | 6.5 | 58.0 |
| source_discovery | 54 | 2.72 | 3.3 | 147.0 |
| connector | 54 | 66270.1 | 97806.1 | 3578585.6 |
| document_discovery | 54 | 66270.24 | 97806.2 | 3578593.2 |
| document_download | 54 | 230223.12 | 1509355.9 | 12432048.4 |
| extraction | 54 | 73.83 | 109.5 | 3987.0 |
| candidate_validation | 54 | 5.99 | 9.5 | 323.4 |
| publish_queue | 54 | 6.04 | 9.5 | 326.2 |
| append_dataset | 54 | 47.48 | 119.7 | 2564.1 |
| export | 54 | 0.34 | 0.6 | 18.6 |
| git_commit | 54 | 0.34 | 2.1 | 18.1 |
| push | 54 | 0.33 | 0.8 | 17.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1325 |
| Documents processed | 4962 |
| Process ratio | 374.5% (target ≥90.0%) |
| Rows published (traces) | 202 |
| Sessions observed | 82 |
| Avg session duration (s) | 641.841 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.277 |
| Avg connector latency (ms) | 13788.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **374.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
