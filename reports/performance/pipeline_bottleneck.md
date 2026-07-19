# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T06:15:05+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 111 | 1.01 | 6.5 | 111.9 |
| source_discovery | 111 | 3.1 | 39.8 | 344.2 |
| connector | 111 | 80518.48 | 97806.1 | 8937551.4 |
| document_discovery | 111 | 80518.62 | 97806.2 | 8937567.0 |
| document_download | 111 | 267381.67 | 1509355.9 | 29679365.3 |
| extraction | 111 | 82.18 | 274.0 | 9121.9 |
| candidate_validation | 111 | 7.65 | 18.7 | 849.1 |
| publish_queue | 111 | 7.85 | 34.7 | 871.1 |
| append_dataset | 111 | 45.78 | 119.7 | 5082.1 |
| export | 111 | 0.34 | 0.7 | 37.4 |
| git_commit | 111 | 0.32 | 2.1 | 35.5 |
| push | 111 | 0.31 | 0.8 | 34.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3052 |
| Documents processed | 9601 |
| Process ratio | 314.6% (target ≥90.0%) |
| Rows published (traces) | 487 |
| Sessions observed | 139 |
| Avg session duration (s) | 847.662 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.673 |
| Avg connector latency (ms) | 13771.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **314.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
