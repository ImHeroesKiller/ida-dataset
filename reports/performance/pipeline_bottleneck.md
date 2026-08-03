# Pipeline Bottleneck Analysis

**Generated:** 2026-08-03T06:44:09+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 276 | 1.39 | 70.9 | 383.5 |
| source_discovery | 276 | 4.17 | 186.3 | 1150.5 |
| connector | 276 | 88582.3 | 97806.1 | 24448715.9 |
| document_discovery | 276 | 88582.51 | 97806.2 | 24448774.1 |
| document_download | 276 | 237652.38 | 1509355.9 | 65592056.5 |
| extraction | 276 | 93.38 | 274.0 | 25774.0 |
| candidate_validation | 276 | 12.35 | 102.5 | 3409.4 |
| publish_queue | 276 | 12.43 | 102.7 | 3431.7 |
| append_dataset | 276 | 40.82 | 119.7 | 11265.5 |
| export | 276 | 0.35 | 2.1 | 96.5 |
| git_commit | 276 | 0.36 | 15.1 | 100.6 |
| push | 276 | 0.61 | 81.1 | 167.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8106 |
| Documents processed | 19530 |
| Process ratio | 240.9% (target ≥90.0%) |
| Rows published (traces) | 1309 |
| Sessions observed | 304 |
| Avg session duration (s) | 959.408 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.862 |
| Avg connector latency (ms) | 13788.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **240.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
