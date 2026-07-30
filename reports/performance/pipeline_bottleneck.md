# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T12:15:42+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 235 | 1.29 | 70.9 | 303.6 |
| source_discovery | 235 | 3.82 | 186.3 | 898.5 |
| connector | 235 | 87636.97 | 97806.1 | 20594687.1 |
| document_discovery | 235 | 87637.12 | 97806.2 | 20594722.2 |
| document_download | 235 | 244177.9 | 1509355.9 | 57381805.6 |
| extraction | 235 | 91.96 | 274.0 | 21610.6 |
| candidate_validation | 235 | 11.06 | 37.2 | 2599.1 |
| publish_queue | 235 | 11.15 | 37.4 | 2620.0 |
| append_dataset | 235 | 41.89 | 119.7 | 9844.0 |
| export | 235 | 0.35 | 1.9 | 81.3 |
| git_commit | 235 | 0.31 | 2.1 | 73.3 |
| push | 235 | 0.31 | 0.8 | 73.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6846 |
| Documents processed | 17241 |
| Process ratio | 251.8% (target ≥90.0%) |
| Rows published (traces) | 1104 |
| Sessions observed | 263 |
| Avg session duration (s) | 949.118 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.838 |
| Avg connector latency (ms) | 13829.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **251.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
