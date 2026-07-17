# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T19:30:18+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 92 | 1.02 | 6.5 | 93.8 |
| source_discovery | 92 | 2.75 | 3.3 | 253.0 |
| connector | 92 | 77728.24 | 97806.1 | 7150998.2 |
| document_discovery | 92 | 77728.39 | 97806.2 | 7151011.7 |
| document_download | 92 | 272981.47 | 1509355.9 | 25114295.0 |
| extraction | 92 | 83.2 | 274.0 | 7654.3 |
| candidate_validation | 92 | 7.19 | 18.7 | 661.6 |
| publish_queue | 92 | 7.41 | 34.7 | 681.4 |
| append_dataset | 92 | 47.79 | 119.7 | 4396.7 |
| export | 92 | 0.34 | 0.6 | 30.9 |
| git_commit | 92 | 0.32 | 2.1 | 29.4 |
| push | 92 | 0.31 | 0.8 | 28.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2473 |
| Documents processed | 8420 |
| Process ratio | 340.5% (target ≥90.0%) |
| Rows published (traces) | 392 |
| Sessions observed | 120 |
| Avg session duration (s) | 811.717 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.6 |
| Avg connector latency (ms) | 13774.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **340.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
