# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T05:52:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 4 | 0.53 | 0.9 | 2.1 |
| source_discovery | 4 | 1.38 | 2.2 | 5.5 |
| connector | 4 | 3413.82 | 7301.3 | 13655.3 |
| document_discovery | 4 | 3414.03 | 7301.7 | 13656.1 |
| document_download | 4 | 4722.73 | 6219.3 | 18890.9 |
| extraction | 4 | 17.77 | 20.6 | 71.1 |
| candidate_validation | 4 | 3.58 | 6.6 | 14.3 |
| publish_queue | 4 | 3.6 | 6.5 | 14.4 |
| append_dataset | 4 | 4.35 | 6.3 | 17.4 |
| export | 4 | 0.38 | 0.6 | 1.5 |
| git_commit | 4 | 0.35 | 0.6 | 1.4 |
| push | 4 | 0.3 | 0.4 | 1.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 42 |
| Documents processed | 12 |
| Process ratio | 28.6% (target ≥90.0%) |
| Rows published (traces) | 9 |
| Sessions observed | 28 |
| Avg session duration (s) | 5.679 |
| Max session duration (s) | 111.0 |
| Rows / session (productive) | 2.333 |
| Avg connector latency (ms) | 3.8 |
| Worker utilization (est) | 0.77 |
| Idle fraction (est) | 0.23 |
| Queue wait (doc depth) | 13 |

## Bottleneck notes

- Historical process ratio **28.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
