# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T15:15:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 116 | 1.0 | 6.5 | 116.3 |
| source_discovery | 116 | 3.08 | 39.8 | 357.7 |
| connector | 116 | 81099.28 | 97806.1 | 9407516.1 |
| document_discovery | 116 | 81099.42 | 97806.2 | 9407532.2 |
| document_download | 116 | 269464.65 | 1509355.9 | 31257899.7 |
| extraction | 116 | 82.02 | 274.0 | 9514.3 |
| candidate_validation | 116 | 7.93 | 30.0 | 920.1 |
| publish_queue | 116 | 8.12 | 34.7 | 942.1 |
| append_dataset | 116 | 45.41 | 119.7 | 5268.0 |
| export | 116 | 0.34 | 0.7 | 39.2 |
| git_commit | 116 | 0.32 | 2.1 | 36.8 |
| push | 116 | 0.31 | 0.8 | 36.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3207 |
| Documents processed | 9940 |
| Process ratio | 309.9% (target ≥90.0%) |
| Rows published (traces) | 512 |
| Sessions observed | 144 |
| Avg session duration (s) | 858.125 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.688 |
| Avg connector latency (ms) | 15406.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **309.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
