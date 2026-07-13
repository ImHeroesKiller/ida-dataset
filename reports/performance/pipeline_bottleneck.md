# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T19:05:12+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 47 | 1.1 | 6.5 | 51.5 |
| source_discovery | 47 | 2.71 | 3.3 | 127.6 |
| connector | 47 | 62137.77 | 97806.1 | 2920475.4 |
| document_discovery | 47 | 62137.92 | 97806.2 | 2920482.1 |
| document_download | 47 | 216806.26 | 1509355.9 | 10189894.2 |
| extraction | 47 | 69.81 | 109.5 | 3280.9 |
| candidate_validation | 47 | 5.64 | 8.7 | 265.3 |
| publish_queue | 47 | 5.7 | 8.8 | 267.9 |
| append_dataset | 47 | 45.76 | 119.7 | 2150.8 |
| export | 47 | 0.34 | 0.6 | 16.0 |
| git_commit | 47 | 0.34 | 2.1 | 15.8 |
| push | 47 | 0.33 | 0.8 | 15.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1108 |
| Documents processed | 4157 |
| Process ratio | 375.2% (target ≥90.0%) |
| Rows published (traces) | 167 |
| Sessions observed | 75 |
| Avg session duration (s) | 592.413 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.15 |
| Avg connector latency (ms) | 13654.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **375.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
