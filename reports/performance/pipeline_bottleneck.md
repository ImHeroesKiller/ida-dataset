# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T13:12:50+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 299 | 1.54 | 70.9 | 459.1 |
| source_discovery | 299 | 4.32 | 186.3 | 1290.7 |
| connector | 299 | 88999.42 | 97806.1 | 26610827.1 |
| document_discovery | 299 | 88999.63 | 97806.2 | 26610888.1 |
| document_download | 299 | 234201.09 | 1509355.9 | 70026124.9 |
| extraction | 299 | 94.78 | 274.0 | 28339.3 |
| candidate_validation | 299 | 12.79 | 102.5 | 3824.4 |
| publish_queue | 299 | 12.87 | 102.7 | 3846.8 |
| append_dataset | 299 | 40.15 | 119.7 | 12005.5 |
| export | 299 | 0.35 | 2.1 | 103.8 |
| git_commit | 299 | 0.36 | 15.1 | 107.7 |
| push | 299 | 0.69 | 81.1 | 206.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8819 |
| Documents processed | 20677 |
| Process ratio | 234.5% (target ≥90.0%) |
| Rows published (traces) | 1424 |
| Sessions observed | 327 |
| Avg session duration (s) | 962.685 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.873 |
| Avg connector latency (ms) | 14205.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **234.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
