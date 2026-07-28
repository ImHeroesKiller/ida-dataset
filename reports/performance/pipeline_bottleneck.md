# Pipeline Bottleneck Analysis

**Generated:** 2026-07-28T08:52:42+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 212 | 1.32 | 70.9 | 280.6 |
| source_discovery | 212 | 3.93 | 186.3 | 833.5 |
| connector | 212 | 86944.74 | 97806.1 | 18432285.5 |
| document_discovery | 212 | 86944.89 | 97806.2 | 18432316.3 |
| document_download | 212 | 251644.93 | 1509355.9 | 53348725.7 |
| extraction | 212 | 90.17 | 274.0 | 19116.5 |
| candidate_validation | 212 | 10.45 | 37.2 | 2215.6 |
| publish_queue | 212 | 10.57 | 37.4 | 2240.7 |
| append_dataset | 212 | 42.4 | 119.7 | 8989.3 |
| export | 212 | 0.35 | 1.9 | 73.7 |
| git_commit | 212 | 0.31 | 2.1 | 66.1 |
| push | 212 | 0.32 | 0.8 | 66.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6143 |
| Documents processed | 15929 |
| Process ratio | 259.3% (target ≥90.0%) |
| Rows published (traces) | 989 |
| Sessions observed | 240 |
| Avg session duration (s) | 942.467 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.82 |
| Avg connector latency (ms) | 14115.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **259.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
