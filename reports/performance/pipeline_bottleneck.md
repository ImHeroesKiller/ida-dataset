# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T03:45:05+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 220 | 1.31 | 70.9 | 288.5 |
| source_discovery | 220 | 3.89 | 186.3 | 856.2 |
| connector | 220 | 87203.58 | 97806.1 | 19184786.6 |
| document_discovery | 220 | 87203.72 | 97806.2 | 19184818.6 |
| document_download | 220 | 248240.17 | 1509355.9 | 54612837.0 |
| extraction | 220 | 91.01 | 274.0 | 20022.2 |
| candidate_validation | 220 | 10.7 | 37.2 | 2353.6 |
| publish_queue | 220 | 10.81 | 37.4 | 2379.0 |
| append_dataset | 220 | 42.13 | 119.7 | 9268.4 |
| export | 220 | 0.35 | 1.9 | 76.6 |
| git_commit | 220 | 0.31 | 2.1 | 68.5 |
| push | 220 | 0.31 | 0.8 | 69.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6381 |
| Documents processed | 16384 |
| Process ratio | 256.8% (target ≥90.0%) |
| Rows published (traces) | 1029 |
| Sessions observed | 248 |
| Avg session duration (s) | 944.532 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.826 |
| Avg connector latency (ms) | 13709.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **256.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
