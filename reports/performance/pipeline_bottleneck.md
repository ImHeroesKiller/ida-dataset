# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T16:54:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 46 | 1.09 | 6.5 | 50.3 |
| source_discovery | 46 | 2.71 | 3.3 | 124.8 |
| connector | 46 | 61444.76 | 97806.1 | 2826458.8 |
| document_discovery | 46 | 61444.9 | 97806.2 | 2826465.3 |
| document_download | 46 | 216860.16 | 1509355.9 | 9975567.3 |
| extraction | 46 | 69.36 | 109.5 | 3190.7 |
| candidate_validation | 46 | 5.67 | 8.7 | 261.0 |
| publish_queue | 46 | 5.73 | 8.8 | 263.6 |
| append_dataset | 46 | 45.58 | 119.7 | 2096.5 |
| export | 46 | 0.34 | 0.6 | 15.7 |
| git_commit | 46 | 0.34 | 2.1 | 15.5 |
| push | 46 | 0.33 | 0.8 | 15.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1077 |
| Documents processed | 4062 |
| Process ratio | 377.2% (target ≥90.0%) |
| Rows published (traces) | 166 |
| Sessions observed | 74 |
| Avg session duration (s) | 585.851 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.231 |
| Avg connector latency (ms) | 14426.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **377.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
