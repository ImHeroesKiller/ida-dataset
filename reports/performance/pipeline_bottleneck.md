# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T19:35:48+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 119 | 1.0 | 6.5 | 119.3 |
| source_discovery | 119 | 3.08 | 39.8 | 366.3 |
| connector | 119 | 81423.16 | 97806.1 | 9689355.5 |
| document_discovery | 119 | 81423.29 | 97806.2 | 9689372.0 |
| document_download | 119 | 267839.86 | 1509355.9 | 31872943.0 |
| extraction | 119 | 82.27 | 274.0 | 9789.9 |
| candidate_validation | 119 | 7.99 | 30.0 | 950.5 |
| publish_queue | 119 | 8.17 | 34.7 | 972.5 |
| append_dataset | 119 | 45.16 | 119.7 | 5374.1 |
| export | 119 | 0.34 | 0.7 | 40.5 |
| git_commit | 119 | 0.32 | 2.1 | 37.6 |
| push | 119 | 0.31 | 0.8 | 37.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3300 |
| Documents processed | 10116 |
| Process ratio | 306.5% (target ≥90.0%) |
| Rows published (traces) | 527 |
| Sessions observed | 147 |
| Avg session duration (s) | 861.884 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.696 |
| Avg connector latency (ms) | 13794.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **306.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
