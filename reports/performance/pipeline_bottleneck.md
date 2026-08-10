# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T16:23:28+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 379 | 1.52 | 70.9 | 577.8 |
| source_discovery | 379 | 4.43 | 186.3 | 1677.2 |
| connector | 379 | 90053.29 | 97806.1 | 34130197.9 |
| document_discovery | 379 | 90053.48 | 97806.2 | 34130269.7 |
| document_download | 379 | 237554.86 | 1509355.9 | 90033290.8 |
| extraction | 379 | 98.06 | 274.0 | 37164.6 |
| candidate_validation | 379 | 15.03 | 149.0 | 5695.0 |
| publish_queue | 379 | 15.09 | 149.1 | 5720.1 |
| append_dataset | 379 | 38.79 | 119.7 | 14700.4 |
| export | 379 | 0.35 | 2.7 | 133.7 |
| git_commit | 379 | 0.35 | 15.1 | 132.9 |
| push | 379 | 0.61 | 81.1 | 229.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11259 |
| Documents processed | 25086 |
| Process ratio | 222.8% (target ≥90.0%) |
| Rows published (traces) | 1824 |
| Sessions observed | 309 |
| Avg session duration (s) | 1060.702 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13781.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
