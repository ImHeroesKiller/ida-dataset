# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T15:57:13+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 78 | 1.04 | 6.5 | 80.8 |
| source_discovery | 78 | 2.75 | 3.3 | 214.2 |
| connector | 78 | 74797.83 | 97806.1 | 5834230.5 |
| document_discovery | 78 | 74797.97 | 97806.2 | 5834241.5 |
| document_download | 78 | 268571.69 | 1509355.9 | 20948591.5 |
| extraction | 78 | 82.74 | 274.0 | 6453.4 |
| candidate_validation | 78 | 6.89 | 18.7 | 537.3 |
| publish_queue | 78 | 7.14 | 34.7 | 556.9 |
| append_dataset | 78 | 50.31 | 119.7 | 3924.0 |
| export | 78 | 0.34 | 0.6 | 26.3 |
| git_commit | 78 | 0.33 | 2.1 | 25.4 |
| push | 78 | 0.32 | 0.8 | 24.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2049 |
| Documents processed | 7598 |
| Process ratio | 370.8% (target ≥90.0%) |
| Rows published (traces) | 322 |
| Sessions observed | 106 |
| Avg session duration (s) | 770.396 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.521 |
| Avg connector latency (ms) | 13920.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **370.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
