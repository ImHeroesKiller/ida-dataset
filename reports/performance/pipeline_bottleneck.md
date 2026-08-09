# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T14:14:07+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 360 | 1.56 | 70.9 | 560.6 |
| source_discovery | 360 | 4.52 | 186.3 | 1626.0 |
| connector | 360 | 89847.46 | 97806.1 | 32345083.9 |
| document_discovery | 360 | 89847.65 | 97806.2 | 32345152.9 |
| document_download | 360 | 231389.36 | 1509355.9 | 83300168.0 |
| extraction | 360 | 97.35 | 274.0 | 35046.7 |
| candidate_validation | 360 | 14.36 | 136.9 | 5167.8 |
| publish_queue | 360 | 14.42 | 136.9 | 5192.1 |
| append_dataset | 360 | 39.05 | 119.7 | 14058.0 |
| export | 360 | 0.35 | 2.1 | 124.7 |
| git_commit | 360 | 0.35 | 15.1 | 126.8 |
| push | 360 | 0.62 | 81.1 | 223.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10680 |
| Documents processed | 24006 |
| Process ratio | 224.8% (target ≥90.0%) |
| Rows published (traces) | 1729 |
| Sessions observed | 311 |
| Avg session duration (s) | 1065.424 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13706.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **224.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
