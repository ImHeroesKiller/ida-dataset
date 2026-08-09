# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T15:51:53+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 362 | 1.55 | 70.9 | 562.4 |
| source_discovery | 362 | 4.51 | 186.3 | 1631.1 |
| connector | 362 | 89869.38 | 97806.1 | 32532717.2 |
| document_discovery | 362 | 89869.58 | 97806.2 | 32532786.5 |
| document_download | 362 | 232506.7 | 1509355.9 | 84167425.2 |
| extraction | 362 | 97.32 | 274.0 | 35229.5 |
| candidate_validation | 362 | 14.39 | 136.9 | 5207.7 |
| publish_queue | 362 | 14.45 | 136.9 | 5232.0 |
| append_dataset | 362 | 39.01 | 119.7 | 14122.3 |
| export | 362 | 0.35 | 2.1 | 125.3 |
| git_commit | 362 | 0.35 | 15.1 | 127.4 |
| push | 362 | 0.62 | 81.1 | 224.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10742 |
| Documents processed | 24119 |
| Process ratio | 224.5% (target ≥90.0%) |
| Rows published (traces) | 1739 |
| Sessions observed | 302 |
| Avg session duration (s) | 1061.526 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13739.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **224.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
