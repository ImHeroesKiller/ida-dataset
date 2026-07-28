# Pipeline Bottleneck Analysis

**Generated:** 2026-07-28T17:00:17+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 215 | 1.32 | 70.9 | 283.8 |
| source_discovery | 215 | 3.92 | 186.3 | 842.6 |
| connector | 215 | 87043.26 | 97806.1 | 18714299.9 |
| document_discovery | 215 | 87043.4 | 97806.2 | 18714331.0 |
| document_download | 215 | 249832.52 | 1509355.9 | 53713991.2 |
| extraction | 215 | 90.36 | 274.0 | 19427.8 |
| candidate_validation | 215 | 10.52 | 37.2 | 2262.4 |
| publish_queue | 215 | 10.64 | 37.4 | 2287.8 |
| append_dataset | 215 | 42.32 | 119.7 | 9099.2 |
| export | 215 | 0.35 | 1.9 | 74.9 |
| git_commit | 215 | 0.31 | 2.1 | 67.1 |
| push | 215 | 0.32 | 0.8 | 67.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6226 |
| Documents processed | 16094 |
| Process ratio | 258.5% (target ≥90.0%) |
| Rows published (traces) | 1004 |
| Sessions observed | 243 |
| Avg session duration (s) | 942.683 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.822 |
| Avg connector latency (ms) | 13753.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **258.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
