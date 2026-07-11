# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T21:09:09+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 22 | 0.91 | 1.3 | 20.0 |
| source_discovery | 22 | 2.54 | 3.2 | 55.8 |
| connector | 22 | 29950.15 | 97806.1 | 658903.2 |
| document_discovery | 22 | 29950.3 | 97806.2 | 658906.7 |
| document_download | 22 | 192123.76 | 1509355.9 | 4226722.8 |
| extraction | 22 | 41.1 | 108.9 | 904.1 |
| candidate_validation | 22 | 4.15 | 6.9 | 91.2 |
| publish_queue | 22 | 4.25 | 8.8 | 93.5 |
| append_dataset | 22 | 22.38 | 119.7 | 492.3 |
| export | 22 | 0.32 | 0.6 | 7.1 |
| git_commit | 22 | 0.3 | 0.4 | 6.5 |
| push | 22 | 0.3 | 0.5 | 6.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 363 |
| Documents processed | 976 |
| Process ratio | 268.9% (target ≥90.0%) |
| Rows published (traces) | 55 |
| Sessions observed | 50 |
| Avg session duration (s) | 346.78 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.375 |
| Avg connector latency (ms) | 13666.1 |
| Worker utilization (est) | 0.932 |
| Idle fraction (est) | 0.068 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **268.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
