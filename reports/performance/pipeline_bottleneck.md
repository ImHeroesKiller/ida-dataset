# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T22:20:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 261 | 1.26 | 70.9 | 328.4 |
| source_discovery | 261 | 3.73 | 186.3 | 972.5 |
| connector | 261 | 88268.82 | 97806.1 | 23038162.2 |
| document_discovery | 261 | 88269.03 | 97806.2 | 23038218.0 |
| document_download | 261 | 238442.83 | 1509355.9 | 62233577.5 |
| extraction | 261 | 92.89 | 274.0 | 24245.0 |
| candidate_validation | 261 | 12.05 | 102.5 | 3145.9 |
| publish_queue | 261 | 12.14 | 102.7 | 3168.0 |
| append_dataset | 261 | 41.19 | 119.7 | 10749.7 |
| export | 261 | 0.35 | 2.1 | 91.7 |
| git_commit | 261 | 0.37 | 15.1 | 96.3 |
| push | 261 | 0.62 | 81.1 | 162.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7641 |
| Documents processed | 18703 |
| Process ratio | 244.8% (target ≥90.0%) |
| Rows published (traces) | 1234 |
| Sessions observed | 289 |
| Avg session duration (s) | 954.498 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.854 |
| Avg connector latency (ms) | 13756.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **244.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
