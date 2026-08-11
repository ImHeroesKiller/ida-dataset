# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T18:17:07+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 397 | 1.5 | 70.9 | 595.5 |
| source_discovery | 397 | 4.35 | 186.3 | 1728.8 |
| connector | 397 | 90233.08 | 97806.1 | 35822531.5 |
| document_discovery | 397 | 90233.26 | 97806.2 | 35822605.6 |
| document_download | 397 | 236062.16 | 1509355.9 | 93716677.0 |
| extraction | 397 | 98.82 | 274.0 | 39233.4 |
| candidate_validation | 397 | 15.39 | 149.0 | 6110.6 |
| publish_queue | 397 | 15.46 | 149.1 | 6136.5 |
| append_dataset | 397 | 38.69 | 119.7 | 15361.4 |
| export | 397 | 0.35 | 2.7 | 139.4 |
| git_commit | 397 | 0.35 | 15.1 | 139.0 |
| push | 397 | 0.59 | 81.1 | 235.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11807 |
| Documents processed | 26144 |
| Process ratio | 221.4% (target ≥90.0%) |
| Rows published (traces) | 1914 |
| Sessions observed | 302 |
| Avg session duration (s) | 1057.01 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13710.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
