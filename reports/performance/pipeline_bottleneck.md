# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T19:32:37+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 197 | 0.99 | 6.5 | 195.0 |
| source_discovery | 197 | 3.07 | 39.8 | 605.2 |
| connector | 197 | 86400.92 | 97806.1 | 17020980.9 |
| document_discovery | 197 | 86401.06 | 97806.2 | 17021009.7 |
| document_download | 197 | 253627.57 | 1509355.9 | 49964631.0 |
| extraction | 197 | 89.03 | 274.0 | 17539.6 |
| candidate_validation | 197 | 10.11 | 37.2 | 1992.6 |
| publish_queue | 197 | 10.24 | 37.4 | 2016.9 |
| append_dataset | 197 | 42.72 | 119.7 | 8416.1 |
| export | 197 | 0.35 | 1.9 | 68.9 |
| git_commit | 197 | 0.31 | 2.1 | 61.4 |
| push | 197 | 0.32 | 0.8 | 62.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5678 |
| Documents processed | 15043 |
| Process ratio | 264.9% (target ≥90.0%) |
| Rows published (traces) | 917 |
| Sessions observed | 225 |
| Avg session duration (s) | 934.342 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.821 |
| Avg connector latency (ms) | 13721.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **264.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
