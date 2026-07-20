# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T16:10:20+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 129 | 1.0 | 6.5 | 129.2 |
| source_discovery | 129 | 3.18 | 39.8 | 410.0 |
| connector | 129 | 82392.73 | 97806.1 | 10628662.1 |
| document_discovery | 129 | 82392.87 | 97806.2 | 10628680.1 |
| document_download | 129 | 260486.0 | 1509355.9 | 33602694.6 |
| extraction | 129 | 84.05 | 274.0 | 10842.4 |
| candidate_validation | 129 | 8.22 | 30.0 | 1061.0 |
| publish_queue | 129 | 8.4 | 34.7 | 1083.4 |
| append_dataset | 129 | 44.69 | 119.7 | 5764.5 |
| export | 129 | 0.35 | 1.9 | 45.1 |
| git_commit | 129 | 0.32 | 2.1 | 41.0 |
| push | 129 | 0.31 | 0.8 | 40.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3600 |
| Documents processed | 10777 |
| Process ratio | 299.4% (target ≥90.0%) |
| Rows published (traces) | 577 |
| Sessions observed | 157 |
| Avg session duration (s) | 871.363 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.721 |
| Avg connector latency (ms) | 13751.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **299.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
