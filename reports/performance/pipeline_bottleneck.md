# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T22:55:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 385 | 1.52 | 70.9 | 584.1 |
| source_discovery | 385 | 4.4 | 186.3 | 1695.1 |
| connector | 385 | 90114.22 | 97806.1 | 34693973.4 |
| document_discovery | 385 | 90114.41 | 97806.2 | 34694046.2 |
| document_download | 385 | 238504.79 | 1509355.9 | 91824345.0 |
| extraction | 385 | 98.35 | 274.0 | 37866.4 |
| candidate_validation | 385 | 15.17 | 149.0 | 5839.7 |
| publish_queue | 385 | 15.23 | 149.1 | 5865.0 |
| append_dataset | 385 | 38.79 | 119.7 | 14934.4 |
| export | 385 | 0.35 | 2.7 | 135.8 |
| git_commit | 385 | 0.35 | 15.1 | 135.1 |
| push | 385 | 0.6 | 81.1 | 231.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11445 |
| Documents processed | 25443 |
| Process ratio | 222.3% (target ≥90.0%) |
| Rows published (traces) | 1854 |
| Sessions observed | 303 |
| Avg session duration (s) | 1062.914 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13824.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
