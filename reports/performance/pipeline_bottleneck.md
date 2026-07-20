# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T18:22:38+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 130 | 1.0 | 6.5 | 130.3 |
| source_discovery | 130 | 3.18 | 39.8 | 413.3 |
| connector | 130 | 82482.65 | 97806.1 | 10722745.0 |
| document_discovery | 130 | 82482.79 | 97806.2 | 10722763.0 |
| document_download | 130 | 260251.58 | 1509355.9 | 33832704.9 |
| extraction | 130 | 84.16 | 274.0 | 10941.3 |
| candidate_validation | 130 | 8.25 | 30.0 | 1073.1 |
| publish_queue | 130 | 8.43 | 34.7 | 1095.5 |
| append_dataset | 130 | 44.61 | 119.7 | 5799.2 |
| export | 130 | 0.35 | 1.9 | 45.6 |
| git_commit | 130 | 0.32 | 2.1 | 41.3 |
| push | 130 | 0.31 | 0.8 | 40.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3631 |
| Documents processed | 10828 |
| Process ratio | 298.2% (target ≥90.0%) |
| Rows published (traces) | 582 |
| Sessions observed | 158 |
| Avg session duration (s) | 872.658 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.724 |
| Avg connector latency (ms) | 13782.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **298.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
