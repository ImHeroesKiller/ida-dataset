# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T21:31:21+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 143 | 1.0 | 6.5 | 142.7 |
| source_discovery | 143 | 3.15 | 39.8 | 450.3 |
| connector | 143 | 83529.93 | 97806.1 | 11944780.5 |
| document_discovery | 143 | 83530.07 | 97806.2 | 11944800.5 |
| document_download | 143 | 254572.02 | 1509355.9 | 36403798.3 |
| extraction | 143 | 85.3 | 274.0 | 12197.3 |
| candidate_validation | 143 | 8.66 | 30.0 | 1237.7 |
| publish_queue | 143 | 8.82 | 34.7 | 1261.1 |
| append_dataset | 143 | 44.03 | 119.7 | 6296.0 |
| export | 143 | 0.35 | 1.9 | 49.6 |
| git_commit | 143 | 0.32 | 2.1 | 45.1 |
| push | 143 | 0.31 | 0.8 | 44.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4024 |
| Documents processed | 11642 |
| Process ratio | 289.3% (target ≥90.0%) |
| Rows published (traces) | 647 |
| Sessions observed | 171 |
| Avg session duration (s) | 884.924 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.75 |
| Avg connector latency (ms) | 13875.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **289.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
