# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T10:42:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 169 | 0.99 | 6.5 | 167.0 |
| source_discovery | 169 | 3.11 | 39.8 | 525.0 |
| connector | 169 | 85146.72 | 97806.1 | 14389795.9 |
| document_discovery | 169 | 85146.87 | 97806.2 | 14389821.3 |
| document_download | 169 | 249400.92 | 1509355.9 | 42148754.8 |
| extraction | 169 | 87.21 | 274.0 | 14739.3 |
| candidate_validation | 169 | 9.33 | 30.0 | 1576.4 |
| publish_queue | 169 | 9.47 | 34.7 | 1600.3 |
| append_dataset | 169 | 43.6 | 119.7 | 7368.5 |
| export | 169 | 0.35 | 1.9 | 59.5 |
| git_commit | 169 | 0.31 | 2.1 | 53.1 |
| push | 169 | 0.31 | 0.8 | 53.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4820 |
| Documents processed | 13394 |
| Process ratio | 277.9% (target ≥90.0%) |
| Rows published (traces) | 777 |
| Sessions observed | 197 |
| Avg session duration (s) | 908.086 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.79 |
| Avg connector latency (ms) | 13749.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **277.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
