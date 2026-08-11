# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T21:08:47+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 399 | 1.5 | 70.9 | 597.4 |
| source_discovery | 399 | 4.35 | 186.3 | 1734.6 |
| connector | 399 | 90251.85 | 97806.1 | 36010488.3 |
| document_discovery | 399 | 90252.04 | 97806.2 | 36010562.8 |
| document_download | 399 | 235880.95 | 1509355.9 | 94116498.9 |
| extraction | 399 | 98.89 | 274.0 | 39458.1 |
| candidate_validation | 399 | 15.44 | 149.0 | 6160.8 |
| publish_queue | 399 | 15.51 | 149.1 | 6186.9 |
| append_dataset | 399 | 38.7 | 119.7 | 15439.9 |
| export | 399 | 0.35 | 2.7 | 140.1 |
| git_commit | 399 | 0.35 | 15.1 | 139.7 |
| push | 399 | 0.59 | 81.1 | 235.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11869 |
| Documents processed | 26257 |
| Process ratio | 221.2% (target ≥90.0%) |
| Rows published (traces) | 1924 |
| Sessions observed | 304 |
| Avg session duration (s) | 1057.273 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13758.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
