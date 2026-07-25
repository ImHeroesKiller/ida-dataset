# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T17:20:43+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 184 | 0.99 | 6.5 | 182.0 |
| source_discovery | 184 | 3.09 | 39.8 | 567.7 |
| connector | 184 | 85866.87 | 97806.1 | 15799504.4 |
| document_discovery | 184 | 85867.02 | 97806.2 | 15799531.7 |
| document_download | 184 | 253243.3 | 1509355.9 | 46596767.4 |
| extraction | 184 | 88.05 | 274.0 | 16201.9 |
| candidate_validation | 184 | 9.67 | 30.0 | 1779.5 |
| publish_queue | 184 | 9.8 | 34.7 | 1803.7 |
| append_dataset | 184 | 43.07 | 119.7 | 7924.1 |
| export | 184 | 0.35 | 1.9 | 64.7 |
| git_commit | 184 | 0.31 | 2.1 | 57.4 |
| push | 184 | 0.32 | 0.8 | 58.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5285 |
| Documents processed | 14280 |
| Process ratio | 270.2% (target ≥90.0%) |
| Rows published (traces) | 852 |
| Sessions observed | 212 |
| Avg session duration (s) | 924.377 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.808 |
| Avg connector latency (ms) | 13736.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **270.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
