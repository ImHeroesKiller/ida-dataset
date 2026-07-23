# Pipeline Bottleneck Analysis

**Generated:** 2026-07-23T18:31:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 162 | 0.99 | 6.5 | 160.1 |
| source_discovery | 162 | 3.11 | 39.8 | 504.5 |
| connector | 162 | 84763.61 | 97806.1 | 13731705.5 |
| document_discovery | 162 | 84763.77 | 97806.2 | 13731730.1 |
| document_download | 162 | 252389.16 | 1509355.9 | 40887043.4 |
| extraction | 162 | 86.73 | 274.0 | 14050.3 |
| candidate_validation | 162 | 9.15 | 30.0 | 1482.6 |
| publish_queue | 162 | 9.3 | 34.7 | 1506.3 |
| append_dataset | 162 | 43.77 | 119.7 | 7090.0 |
| export | 162 | 0.35 | 1.9 | 57.0 |
| git_commit | 162 | 0.31 | 2.1 | 50.9 |
| push | 162 | 0.31 | 0.8 | 50.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4603 |
| Documents processed | 12969 |
| Process ratio | 281.8% (target ≥90.0%) |
| Rows published (traces) | 742 |
| Sessions observed | 190 |
| Avg session duration (s) | 904.042 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.781 |
| Avg connector latency (ms) | 13702.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **281.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
