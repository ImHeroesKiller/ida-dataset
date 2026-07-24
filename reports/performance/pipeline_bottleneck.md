# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T07:49:16+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 167 | 0.99 | 6.5 | 165.0 |
| source_discovery | 167 | 3.11 | 39.8 | 518.8 |
| connector | 167 | 85039.58 | 97806.1 | 14201610.0 |
| document_discovery | 167 | 85039.73 | 97806.2 | 14201635.1 |
| document_download | 167 | 250836.7 | 1509355.9 | 41889729.6 |
| extraction | 167 | 87.04 | 274.0 | 14536.3 |
| candidate_validation | 167 | 9.28 | 30.0 | 1549.2 |
| publish_queue | 167 | 9.42 | 34.7 | 1573.0 |
| append_dataset | 167 | 43.67 | 119.7 | 7292.1 |
| export | 167 | 0.35 | 1.9 | 58.8 |
| git_commit | 167 | 0.31 | 2.1 | 52.5 |
| push | 167 | 0.31 | 0.8 | 52.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4758 |
| Documents processed | 13270 |
| Process ratio | 278.9% (target ≥90.0%) |
| Rows published (traces) | 767 |
| Sessions observed | 195 |
| Avg session duration (s) | 907.564 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.787 |
| Avg connector latency (ms) | 13932.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **278.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
