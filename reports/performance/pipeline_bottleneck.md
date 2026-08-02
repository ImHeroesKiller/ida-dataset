# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T08:50:40+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 265 | 1.25 | 70.9 | 331.9 |
| source_discovery | 265 | 3.71 | 186.3 | 983.6 |
| connector | 265 | 88357.45 | 97806.1 | 23414724.1 |
| document_discovery | 265 | 88357.66 | 97806.2 | 23414780.6 |
| document_download | 265 | 238669.64 | 1509355.9 | 63247455.3 |
| extraction | 265 | 92.99 | 274.0 | 24642.2 |
| candidate_validation | 265 | 12.13 | 102.5 | 3215.6 |
| publish_queue | 265 | 12.22 | 102.7 | 3237.7 |
| append_dataset | 265 | 41.05 | 119.7 | 10877.6 |
| export | 265 | 0.35 | 2.1 | 92.8 |
| git_commit | 265 | 0.37 | 15.1 | 97.5 |
| push | 265 | 0.62 | 81.1 | 164.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7765 |
| Documents processed | 18909 |
| Process ratio | 243.5% (target ≥90.0%) |
| Rows published (traces) | 1254 |
| Sessions observed | 293 |
| Avg session duration (s) | 955.795 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.857 |
| Avg connector latency (ms) | 13800.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **243.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
