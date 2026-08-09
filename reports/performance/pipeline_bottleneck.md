# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T07:17:19+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 353 | 1.57 | 70.9 | 554.1 |
| source_discovery | 353 | 4.55 | 186.3 | 1606.7 |
| connector | 353 | 89764.93 | 97806.1 | 31687019.9 |
| document_discovery | 353 | 89765.12 | 97806.2 | 31687087.8 |
| document_download | 353 | 231605.96 | 1509355.9 | 81756904.8 |
| extraction | 353 | 97.13 | 274.0 | 34287.0 |
| candidate_validation | 353 | 14.23 | 136.9 | 5022.8 |
| publish_queue | 353 | 14.3 | 136.9 | 5047.0 |
| append_dataset | 353 | 39.16 | 119.7 | 13822.7 |
| export | 353 | 0.35 | 2.1 | 122.7 |
| git_commit | 353 | 0.35 | 15.1 | 124.9 |
| push | 353 | 0.63 | 81.1 | 221.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10463 |
| Documents processed | 23605 |
| Process ratio | 225.6% (target ≥90.0%) |
| Rows published (traces) | 1694 |
| Sessions observed | 304 |
| Avg session duration (s) | 1065.651 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13823.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
