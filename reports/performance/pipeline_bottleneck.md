# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T16:55:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 363 | 1.55 | 70.9 | 563.5 |
| source_discovery | 363 | 4.5 | 186.3 | 1634.1 |
| connector | 363 | 89880.13 | 97806.1 | 32626487.7 |
| document_discovery | 363 | 89880.32 | 97806.2 | 32626557.7 |
| document_download | 363 | 232555.99 | 1509355.9 | 84417824.9 |
| extraction | 363 | 97.35 | 274.0 | 35336.7 |
| candidate_validation | 363 | 14.41 | 136.9 | 5230.0 |
| publish_queue | 363 | 14.47 | 136.9 | 5254.3 |
| append_dataset | 363 | 39.01 | 119.7 | 14161.5 |
| export | 363 | 0.35 | 2.1 | 125.6 |
| git_commit | 363 | 0.35 | 15.1 | 127.7 |
| push | 363 | 0.62 | 81.1 | 224.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10773 |
| Documents processed | 24181 |
| Process ratio | 224.5% (target ≥90.0%) |
| Rows published (traces) | 1744 |
| Sessions observed | 303 |
| Avg session duration (s) | 1061.601 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13640.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **224.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
