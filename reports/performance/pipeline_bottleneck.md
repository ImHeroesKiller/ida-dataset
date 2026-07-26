# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T06:26:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 190 | 0.99 | 6.5 | 188.2 |
| source_discovery | 190 | 3.08 | 39.8 | 585.3 |
| connector | 190 | 86119.51 | 97806.1 | 16362706.1 |
| document_discovery | 190 | 86119.65 | 97806.2 | 16362734.1 |
| document_download | 190 | 255343.01 | 1509355.9 | 48515171.6 |
| extraction | 190 | 88.53 | 274.0 | 16820.5 |
| candidate_validation | 190 | 9.82 | 30.0 | 1866.3 |
| publish_queue | 190 | 9.95 | 34.7 | 1890.5 |
| append_dataset | 190 | 42.98 | 119.7 | 8165.9 |
| export | 190 | 0.35 | 1.9 | 66.6 |
| git_commit | 190 | 0.31 | 2.1 | 59.2 |
| push | 190 | 0.32 | 0.8 | 60.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5471 |
| Documents processed | 14652 |
| Process ratio | 267.8% (target ≥90.0%) |
| Rows published (traces) | 882 |
| Sessions observed | 218 |
| Avg session duration (s) | 930.853 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.814 |
| Avg connector latency (ms) | 13711.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **267.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
