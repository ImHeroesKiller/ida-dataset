# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T23:24:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 60 | 1.06 | 6.5 | 63.8 |
| source_discovery | 60 | 2.73 | 3.3 | 163.9 |
| connector | 60 | 69040.56 | 97806.1 | 4142433.6 |
| document_discovery | 60 | 69040.7 | 97806.2 | 4142442.2 |
| document_download | 60 | 247172.12 | 1509355.9 | 14830326.9 |
| extraction | 60 | 79.05 | 274.0 | 4743.3 |
| candidate_validation | 60 | 6.16 | 9.5 | 369.7 |
| publish_queue | 60 | 6.21 | 9.5 | 372.4 |
| append_dataset | 60 | 48.67 | 119.7 | 2920.4 |
| export | 60 | 0.34 | 0.6 | 20.4 |
| git_commit | 60 | 0.33 | 2.1 | 19.7 |
| push | 60 | 0.32 | 0.8 | 19.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1491 |
| Documents processed | 5718 |
| Process ratio | 383.5% (target ≥90.0%) |
| Rows published (traces) | 232 |
| Sessions observed | 88 |
| Avg session duration (s) | 683.057 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.358 |
| Avg connector latency (ms) | 13698.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **383.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
