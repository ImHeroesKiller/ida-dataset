# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T23:10:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 49 | 1.09 | 6.5 | 53.5 |
| source_discovery | 49 | 2.72 | 3.3 | 133.3 |
| connector | 49 | 63436.28 | 97806.1 | 3108377.7 |
| document_discovery | 49 | 63436.42 | 97806.2 | 3108384.7 |
| document_download | 49 | 220534.78 | 1509355.9 | 10806204.2 |
| extraction | 49 | 71.05 | 109.5 | 3481.4 |
| candidate_validation | 49 | 5.75 | 8.7 | 281.8 |
| publish_queue | 49 | 5.8 | 8.8 | 284.4 |
| append_dataset | 49 | 46.75 | 119.7 | 2290.6 |
| export | 49 | 0.34 | 0.6 | 16.9 |
| git_commit | 49 | 0.33 | 2.1 | 16.4 |
| push | 49 | 0.33 | 0.8 | 16.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1170 |
| Documents processed | 4411 |
| Process ratio | 377.0% (target ≥90.0%) |
| Rows published (traces) | 177 |
| Sessions observed | 77 |
| Avg session duration (s) | 607.571 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.19 |
| Avg connector latency (ms) | 13890.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **377.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
