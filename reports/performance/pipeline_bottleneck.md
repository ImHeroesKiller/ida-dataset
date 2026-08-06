# Pipeline Bottleneck Analysis

**Generated:** 2026-08-06T02:59:53+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 305 | 1.53 | 70.9 | 465.6 |
| source_discovery | 305 | 4.29 | 186.3 | 1307.9 |
| connector | 305 | 89096.16 | 97806.1 | 27174329.9 |
| document_discovery | 305 | 89096.37 | 97806.2 | 27174391.6 |
| document_download | 305 | 234066.98 | 1509355.9 | 71390429.9 |
| extraction | 305 | 95.0 | 274.0 | 28974.4 |
| candidate_validation | 305 | 12.92 | 102.5 | 3940.7 |
| publish_queue | 305 | 13.0 | 102.7 | 3963.5 |
| append_dataset | 305 | 40.01 | 119.7 | 12202.7 |
| export | 305 | 0.35 | 2.1 | 105.8 |
| git_commit | 305 | 0.36 | 15.1 | 109.6 |
| push | 305 | 0.68 | 81.1 | 207.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8995 |
| Documents processed | 20958 |
| Process ratio | 233.0% (target ≥90.0%) |
| Rows published (traces) | 1454 |
| Sessions observed | 301 |
| Avg session duration (s) | 1058.292 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.928 |
| Avg connector latency (ms) | 13754.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **233.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
