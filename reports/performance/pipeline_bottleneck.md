# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T18:19:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 259 | 1.26 | 70.9 | 326.6 |
| source_discovery | 259 | 3.73 | 186.3 | 967.0 |
| connector | 259 | 88224.5 | 97806.1 | 22850144.9 |
| document_discovery | 259 | 88224.71 | 97806.2 | 22850200.5 |
| document_download | 259 | 239052.3 | 1509355.9 | 61914546.8 |
| extraction | 259 | 92.87 | 274.0 | 24052.9 |
| candidate_validation | 259 | 12.02 | 102.5 | 3114.2 |
| publish_queue | 259 | 12.11 | 102.7 | 3136.2 |
| append_dataset | 259 | 41.24 | 119.7 | 10681.9 |
| export | 259 | 0.35 | 2.1 | 91.2 |
| git_commit | 259 | 0.37 | 15.1 | 95.7 |
| push | 259 | 0.63 | 81.1 | 162.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7579 |
| Documents processed | 18579 |
| Process ratio | 245.1% (target ≥90.0%) |
| Rows published (traces) | 1224 |
| Sessions observed | 287 |
| Avg session duration (s) | 954.411 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.853 |
| Avg connector latency (ms) | 13745.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **245.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
