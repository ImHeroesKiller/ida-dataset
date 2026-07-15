# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T22:22:43+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 70 | 1.04 | 6.5 | 73.0 |
| source_discovery | 70 | 2.74 | 3.3 | 191.9 |
| connector | 70 | 72604.07 | 97806.1 | 5082284.7 |
| document_discovery | 70 | 72604.21 | 97806.2 | 5082294.5 |
| document_download | 70 | 271947.89 | 1509355.9 | 19036352.0 |
| extraction | 70 | 81.69 | 274.0 | 5718.3 |
| candidate_validation | 70 | 6.48 | 9.5 | 453.3 |
| publish_queue | 70 | 6.52 | 9.5 | 456.5 |
| append_dataset | 70 | 50.61 | 119.7 | 3542.7 |
| export | 70 | 0.34 | 0.6 | 23.6 |
| git_commit | 70 | 0.33 | 2.1 | 22.8 |
| push | 70 | 0.32 | 0.8 | 22.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1801 |
| Documents processed | 6940 |
| Process ratio | 385.3% (target ≥90.0%) |
| Rows published (traces) | 282 |
| Sessions observed | 98 |
| Avg session duration (s) | 744.735 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.46 |
| Avg connector latency (ms) | 13964.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **385.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
