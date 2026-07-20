# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T22:18:19+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 132 | 1.0 | 6.5 | 132.4 |
| source_discovery | 132 | 3.18 | 39.8 | 419.2 |
| connector | 132 | 82657.72 | 97806.1 | 10910819.4 |
| document_discovery | 132 | 82657.86 | 97806.2 | 10910837.7 |
| document_download | 132 | 258876.92 | 1509355.9 | 34171753.2 |
| extraction | 132 | 84.4 | 274.0 | 11140.3 |
| candidate_validation | 132 | 8.31 | 30.0 | 1097.0 |
| publish_queue | 132 | 8.48 | 34.7 | 1119.4 |
| append_dataset | 132 | 44.61 | 119.7 | 5888.2 |
| export | 132 | 0.35 | 1.9 | 46.2 |
| git_commit | 132 | 0.32 | 2.1 | 41.9 |
| push | 132 | 0.31 | 0.8 | 41.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3693 |
| Documents processed | 10976 |
| Process ratio | 297.2% (target ≥90.0%) |
| Rows published (traces) | 592 |
| Sessions observed | 160 |
| Avg session duration (s) | 874.312 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.728 |
| Avg connector latency (ms) | 14227.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **297.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
