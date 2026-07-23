# Pipeline Bottleneck Analysis

**Generated:** 2026-07-23T11:29:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 159 | 0.99 | 6.5 | 157.3 |
| source_discovery | 159 | 3.12 | 39.8 | 496.0 |
| connector | 159 | 84588.22 | 97806.1 | 13449527.1 |
| document_discovery | 159 | 84588.37 | 97806.2 | 13449551.3 |
| document_download | 159 | 251492.12 | 1509355.9 | 39987246.6 |
| extraction | 159 | 86.5 | 274.0 | 13752.9 |
| candidate_validation | 159 | 9.07 | 30.0 | 1442.7 |
| publish_queue | 159 | 9.22 | 34.7 | 1466.5 |
| append_dataset | 159 | 43.82 | 119.7 | 6968.0 |
| export | 159 | 0.35 | 1.9 | 56.0 |
| git_commit | 159 | 0.31 | 2.1 | 50.0 |
| push | 159 | 0.31 | 0.8 | 50.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4510 |
| Documents processed | 12770 |
| Process ratio | 283.1% (target ≥90.0%) |
| Rows published (traces) | 727 |
| Sessions observed | 187 |
| Avg session duration (s) | 900.262 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.776 |
| Avg connector latency (ms) | 14014.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **283.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
