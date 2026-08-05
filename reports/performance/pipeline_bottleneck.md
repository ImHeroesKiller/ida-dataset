# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T04:29:07+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 295 | 1.36 | 70.9 | 401.8 |
| source_discovery | 295 | 4.34 | 186.3 | 1279.5 |
| connector | 295 | 88931.37 | 97806.1 | 26234753.9 |
| document_discovery | 295 | 88931.57 | 97806.2 | 26234814.5 |
| document_download | 295 | 235480.12 | 1509355.9 | 69466634.0 |
| extraction | 295 | 94.21 | 274.0 | 27792.5 |
| candidate_validation | 295 | 12.71 | 102.5 | 3750.2 |
| publish_queue | 295 | 12.79 | 102.7 | 3772.6 |
| append_dataset | 295 | 40.25 | 119.7 | 11874.9 |
| export | 295 | 0.35 | 2.1 | 102.6 |
| git_commit | 295 | 0.36 | 15.1 | 106.6 |
| push | 295 | 0.69 | 81.1 | 204.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8695 |
| Documents processed | 20468 |
| Process ratio | 235.4% (target ≥90.0%) |
| Rows published (traces) | 1404 |
| Sessions observed | 323 |
| Avg session duration (s) | 962.492 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.872 |
| Avg connector latency (ms) | 13757.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **235.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
