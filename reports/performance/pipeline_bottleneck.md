# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T07:35:31+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 85 | 1.03 | 6.5 | 87.6 |
| source_discovery | 85 | 2.75 | 3.3 | 233.6 |
| connector | 85 | 76384.02 | 97806.1 | 6492641.8 |
| document_discovery | 85 | 76384.17 | 97806.2 | 6492654.6 |
| document_download | 85 | 265273.18 | 1509355.9 | 22548220.3 |
| extraction | 85 | 82.77 | 274.0 | 7035.8 |
| candidate_validation | 85 | 7.02 | 18.7 | 596.8 |
| publish_queue | 85 | 7.25 | 34.7 | 616.4 |
| append_dataset | 85 | 48.76 | 119.7 | 4144.7 |
| export | 85 | 0.34 | 0.6 | 28.5 |
| git_commit | 85 | 0.32 | 2.1 | 27.4 |
| push | 85 | 0.32 | 0.8 | 26.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2266 |
| Documents processed | 7980 |
| Process ratio | 352.2% (target ≥90.0%) |
| Rows published (traces) | 357 |
| Sessions observed | 113 |
| Avg session duration (s) | 787.389 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.564 |
| Avg connector latency (ms) | 13864.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **352.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
