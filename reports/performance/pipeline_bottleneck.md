# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T04:04:21+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 388 | 1.51 | 70.9 | 586.9 |
| source_discovery | 388 | 4.39 | 186.3 | 1704.0 |
| connector | 388 | 90143.45 | 97806.1 | 34975657.9 |
| document_discovery | 388 | 90143.64 | 97806.2 | 34975731.0 |
| document_download | 388 | 237911.2 | 1509355.9 | 92309545.8 |
| extraction | 388 | 98.46 | 274.0 | 38201.2 |
| candidate_validation | 388 | 15.24 | 149.0 | 5912.7 |
| publish_queue | 388 | 15.3 | 149.1 | 5938.1 |
| append_dataset | 388 | 38.76 | 119.7 | 15038.4 |
| export | 388 | 0.35 | 2.7 | 136.7 |
| git_commit | 388 | 0.35 | 15.1 | 136.0 |
| push | 388 | 0.6 | 81.1 | 232.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11528 |
| Documents processed | 25597 |
| Process ratio | 222.0% (target ≥90.0%) |
| Rows published (traces) | 1869 |
| Sessions observed | 306 |
| Avg session duration (s) | 1062.33 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13943.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
