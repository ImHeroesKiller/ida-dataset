# Pipeline Bottleneck Analysis

**Generated:** 2026-07-23T03:10:44+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 156 | 0.99 | 6.5 | 154.4 |
| source_discovery | 156 | 3.12 | 39.8 | 487.4 |
| connector | 156 | 84409.43 | 97806.1 | 13167871.0 |
| document_discovery | 156 | 84409.58 | 97806.2 | 13167894.9 |
| document_download | 156 | 252426.57 | 1509355.9 | 39378545.4 |
| extraction | 156 | 86.26 | 274.0 | 13456.7 |
| candidate_validation | 156 | 8.99 | 30.0 | 1401.9 |
| publish_queue | 156 | 9.14 | 34.7 | 1425.7 |
| append_dataset | 156 | 43.8 | 119.7 | 6832.1 |
| export | 156 | 0.35 | 1.9 | 54.9 |
| git_commit | 156 | 0.31 | 2.1 | 49.1 |
| push | 156 | 0.31 | 0.8 | 49.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4417 |
| Documents processed | 12548 |
| Process ratio | 284.1% (target ≥90.0%) |
| Rows published (traces) | 712 |
| Sessions observed | 184 |
| Avg session duration (s) | 897.978 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.772 |
| Avg connector latency (ms) | 13697.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **284.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
