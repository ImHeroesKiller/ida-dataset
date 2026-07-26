# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T17:20:19+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 196 | 0.99 | 6.5 | 194.1 |
| source_discovery | 196 | 3.07 | 39.8 | 602.3 |
| connector | 196 | 86361.48 | 97806.1 | 16926849.4 |
| document_discovery | 196 | 86361.62 | 97806.2 | 16926878.1 |
| document_download | 196 | 254184.42 | 1509355.9 | 49820147.1 |
| extraction | 196 | 88.94 | 274.0 | 17431.6 |
| candidate_validation | 196 | 10.09 | 37.2 | 1977.8 |
| publish_queue | 196 | 10.22 | 37.4 | 2002.2 |
| append_dataset | 196 | 42.74 | 119.7 | 8377.7 |
| export | 196 | 0.35 | 1.9 | 68.6 |
| git_commit | 196 | 0.31 | 2.1 | 61.1 |
| push | 196 | 0.32 | 0.8 | 61.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5647 |
| Documents processed | 14981 |
| Process ratio | 265.3% (target ≥90.0%) |
| Rows published (traces) | 912 |
| Sessions observed | 224 |
| Avg session duration (s) | 934.089 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.82 |
| Avg connector latency (ms) | 16180.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **265.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
