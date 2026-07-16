# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T17:32:58+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 79 | 1.03 | 6.5 | 81.2 |
| source_discovery | 79 | 2.74 | 3.3 | 216.2 |
| connector | 79 | 75040.21 | 97806.1 | 5928176.6 |
| document_discovery | 79 | 75040.35 | 97806.2 | 5928187.7 |
| document_download | 79 | 266966.3 | 1509355.9 | 21090337.8 |
| extraction | 79 | 82.49 | 274.0 | 6516.8 |
| candidate_validation | 79 | 6.86 | 18.7 | 542.0 |
| publish_queue | 79 | 7.11 | 34.7 | 561.7 |
| append_dataset | 79 | 49.89 | 119.7 | 3941.0 |
| export | 79 | 0.34 | 0.6 | 26.5 |
| git_commit | 79 | 0.32 | 2.1 | 25.6 |
| push | 79 | 0.32 | 0.8 | 25.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2080 |
| Documents processed | 7649 |
| Process ratio | 367.7% (target ≥90.0%) |
| Rows published (traces) | 327 |
| Sessions observed | 107 |
| Avg session duration (s) | 772.327 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.528 |
| Avg connector latency (ms) | 13771.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **367.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
