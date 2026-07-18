# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T09:44:32+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 99 | 1.02 | 6.5 | 101.1 |
| source_discovery | 99 | 2.77 | 3.5 | 273.8 |
| connector | 99 | 78880.11 | 97806.1 | 7809131.1 |
| document_discovery | 99 | 78880.26 | 97806.2 | 7809145.3 |
| document_download | 99 | 267246.66 | 1509355.9 | 26457419.6 |
| extraction | 99 | 83.32 | 274.0 | 8248.8 |
| candidate_validation | 99 | 7.4 | 18.7 | 732.5 |
| publish_queue | 99 | 7.62 | 34.7 | 754.2 |
| append_dataset | 99 | 47.13 | 119.7 | 4665.9 |
| export | 99 | 0.34 | 0.6 | 33.4 |
| git_commit | 99 | 0.32 | 2.1 | 31.6 |
| push | 99 | 0.31 | 0.8 | 31.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2690 |
| Documents processed | 8863 |
| Process ratio | 329.5% (target ≥90.0%) |
| Rows published (traces) | 427 |
| Sessions observed | 127 |
| Avg session duration (s) | 823.323 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.63 |
| Avg connector latency (ms) | 13799.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **329.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
