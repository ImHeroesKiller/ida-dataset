# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T13:44:18+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 194 | 0.99 | 6.5 | 192.1 |
| source_discovery | 194 | 3.07 | 39.8 | 596.5 |
| connector | 194 | 86283.35 | 97806.1 | 16738969.0 |
| document_discovery | 194 | 86283.49 | 97806.2 | 16738997.5 |
| document_download | 194 | 253611.8 | 1509355.9 | 49200689.1 |
| extraction | 194 | 88.74 | 274.0 | 17215.7 |
| candidate_validation | 194 | 10.04 | 37.2 | 1947.6 |
| publish_queue | 194 | 10.16 | 37.4 | 1972.0 |
| append_dataset | 194 | 42.82 | 119.7 | 8307.6 |
| export | 194 | 0.35 | 1.9 | 68.0 |
| git_commit | 194 | 0.31 | 2.1 | 60.5 |
| push | 194 | 0.32 | 0.8 | 61.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5585 |
| Documents processed | 14879 |
| Process ratio | 266.4% (target ≥90.0%) |
| Rows published (traces) | 902 |
| Sessions observed | 222 |
| Avg session duration (s) | 932.194 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.818 |
| Avg connector latency (ms) | 13699.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **266.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
