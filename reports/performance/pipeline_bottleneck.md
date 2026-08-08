# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T09:02:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 334 | 1.6 | 70.9 | 534.7 |
| source_discovery | 334 | 4.65 | 186.3 | 1552.1 |
| connector | 334 | 89521.33 | 97806.1 | 29900125.0 |
| document_discovery | 334 | 89521.53 | 97806.2 | 29900190.4 |
| document_download | 334 | 232443.73 | 1509355.9 | 77636205.9 |
| extraction | 334 | 96.45 | 274.0 | 32213.8 |
| candidate_validation | 334 | 13.86 | 136.9 | 4630.4 |
| publish_queue | 334 | 13.93 | 136.9 | 4654.1 |
| append_dataset | 334 | 39.49 | 119.7 | 13188.9 |
| export | 334 | 0.34 | 2.1 | 115.1 |
| git_commit | 334 | 0.36 | 15.1 | 118.7 |
| push | 334 | 0.65 | 81.1 | 216.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9884 |
| Documents processed | 22590 |
| Process ratio | 228.6% (target ≥90.0%) |
| Rows published (traces) | 1599 |
| Sessions observed | 309 |
| Avg session duration (s) | 1066.88 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.964 |
| Avg connector latency (ms) | 13713.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **228.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
