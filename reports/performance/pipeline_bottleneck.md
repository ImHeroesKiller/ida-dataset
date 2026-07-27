# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T23:20:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 209 | 1.33 | 70.9 | 277.3 |
| source_discovery | 209 | 3.94 | 186.3 | 824.4 |
| connector | 209 | 86840.15 | 97806.1 | 18149592.2 |
| document_discovery | 209 | 86840.3 | 97806.2 | 18149622.5 |
| document_download | 209 | 252361.0 | 1509355.9 | 52743448.5 |
| extraction | 209 | 89.95 | 274.0 | 18800.4 |
| candidate_validation | 209 | 10.39 | 37.2 | 2171.9 |
| publish_queue | 209 | 10.51 | 37.4 | 2197.0 |
| append_dataset | 209 | 42.42 | 119.7 | 8865.7 |
| export | 209 | 0.35 | 1.9 | 72.5 |
| git_commit | 209 | 0.31 | 2.1 | 65.1 |
| push | 209 | 0.32 | 0.8 | 65.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6050 |
| Documents processed | 15754 |
| Process ratio | 260.4% (target ≥90.0%) |
| Rows published (traces) | 977 |
| Sessions observed | 237 |
| Avg session duration (s) | 941.19 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.832 |
| Avg connector latency (ms) | 13805.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **260.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
