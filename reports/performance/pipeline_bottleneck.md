# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T15:27:13+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 225 | 1.3 | 70.9 | 293.3 |
| source_discovery | 225 | 3.87 | 186.3 | 869.9 |
| connector | 225 | 87354.31 | 97806.1 | 19654720.5 |
| document_discovery | 225 | 87354.46 | 97806.2 | 19654753.3 |
| document_download | 225 | 246459.07 | 1509355.9 | 55453291.6 |
| extraction | 225 | 91.29 | 274.0 | 20539.8 |
| candidate_validation | 225 | 10.83 | 37.2 | 2435.7 |
| publish_queue | 225 | 10.92 | 37.4 | 2456.2 |
| append_dataset | 225 | 41.94 | 119.7 | 9436.5 |
| export | 225 | 0.35 | 1.9 | 78.0 |
| git_commit | 225 | 0.31 | 2.1 | 70.1 |
| push | 225 | 0.31 | 0.8 | 70.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6536 |
| Documents processed | 16632 |
| Process ratio | 254.5% (target ≥90.0%) |
| Rows published (traces) | 1054 |
| Sessions observed | 253 |
| Avg session duration (s) | 945.901 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.83 |
| Avg connector latency (ms) | 13701.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **254.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
