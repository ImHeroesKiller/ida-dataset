# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T00:12:13+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 109 | 1.01 | 6.5 | 110.3 |
| source_discovery | 109 | 2.77 | 3.5 | 301.6 |
| connector | 109 | 80269.51 | 97806.1 | 8749376.9 |
| document_discovery | 109 | 80269.65 | 97806.2 | 8749392.3 |
| document_download | 109 | 269086.51 | 1509355.9 | 29330429.8 |
| extraction | 109 | 82.54 | 274.0 | 8997.1 |
| candidate_validation | 109 | 7.64 | 18.7 | 832.4 |
| publish_queue | 109 | 7.84 | 34.7 | 854.3 |
| append_dataset | 109 | 46.15 | 119.7 | 5030.4 |
| export | 109 | 0.34 | 0.7 | 36.8 |
| git_commit | 109 | 0.32 | 2.1 | 34.9 |
| push | 109 | 0.31 | 0.8 | 34.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2990 |
| Documents processed | 9503 |
| Process ratio | 317.8% (target ≥90.0%) |
| Rows published (traces) | 477 |
| Sessions observed | 137 |
| Avg session duration (s) | 845.285 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.667 |
| Avg connector latency (ms) | 15952.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **317.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
