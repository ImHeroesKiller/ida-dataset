# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T04:32:08+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 285 | 1.38 | 70.9 | 392.5 |
| source_discovery | 285 | 4.13 | 186.3 | 1177.0 |
| connector | 285 | 88752.85 | 97806.1 | 25294561.7 |
| document_discovery | 285 | 88753.06 | 97806.2 | 25294621.2 |
| document_download | 285 | 234891.56 | 1509355.9 | 66944095.3 |
| extraction | 285 | 93.78 | 274.0 | 26727.4 |
| candidate_validation | 285 | 12.56 | 102.5 | 3578.3 |
| publish_queue | 285 | 12.64 | 102.7 | 3601.0 |
| append_dataset | 285 | 40.54 | 119.7 | 11555.0 |
| export | 285 | 0.35 | 2.1 | 99.4 |
| git_commit | 285 | 0.36 | 15.1 | 103.5 |
| push | 285 | 0.6 | 81.1 | 170.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8385 |
| Documents processed | 19931 |
| Process ratio | 237.7% (target ≥90.0%) |
| Rows published (traces) | 1354 |
| Sessions observed | 313 |
| Avg session duration (s) | 958.792 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.867 |
| Avg connector latency (ms) | 13741.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **237.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
