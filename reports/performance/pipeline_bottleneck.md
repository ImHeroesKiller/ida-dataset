# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T23:47:39+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 349 | 1.58 | 70.9 | 550.3 |
| source_discovery | 349 | 4.57 | 186.3 | 1595.5 |
| connector | 349 | 89716.04 | 97806.1 | 31310897.5 |
| document_discovery | 349 | 89716.23 | 97806.2 | 31310964.9 |
| document_download | 349 | 232401.25 | 1509355.9 | 81108037.7 |
| extraction | 349 | 96.98 | 274.0 | 33846.5 |
| candidate_validation | 349 | 14.15 | 136.9 | 4938.8 |
| publish_queue | 349 | 14.22 | 136.9 | 4962.8 |
| append_dataset | 349 | 39.19 | 119.7 | 13679.0 |
| export | 349 | 0.35 | 2.1 | 121.3 |
| git_commit | 349 | 0.35 | 15.1 | 123.7 |
| push | 349 | 0.63 | 81.1 | 220.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10339 |
| Documents processed | 23365 |
| Process ratio | 226.0% (target ≥90.0%) |
| Rows published (traces) | 1674 |
| Sessions observed | 309 |
| Avg session duration (s) | 1067.916 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.977 |
| Avg connector latency (ms) | 13737.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **226.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
