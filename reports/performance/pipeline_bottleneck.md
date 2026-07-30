# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T14:22:25+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 236 | 1.29 | 70.9 | 304.8 |
| source_discovery | 236 | 3.82 | 186.3 | 901.6 |
| connector | 236 | 87662.99 | 97806.1 | 20688466.4 |
| document_discovery | 236 | 87663.14 | 97806.2 | 20688501.6 |
| document_download | 236 | 245179.36 | 1509355.9 | 57862329.8 |
| extraction | 236 | 92.02 | 274.0 | 21717.8 |
| candidate_validation | 236 | 11.09 | 37.2 | 2617.2 |
| publish_queue | 236 | 11.18 | 37.4 | 2638.1 |
| append_dataset | 236 | 41.87 | 119.7 | 9882.2 |
| export | 236 | 0.35 | 1.9 | 81.8 |
| git_commit | 236 | 0.31 | 2.1 | 73.8 |
| push | 236 | 0.31 | 0.8 | 74.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6877 |
| Documents processed | 17292 |
| Process ratio | 251.4% (target ≥90.0%) |
| Rows published (traces) | 1109 |
| Sessions observed | 264 |
| Avg session duration (s) | 950.53 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.838 |
| Avg connector latency (ms) | 13797.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **251.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
