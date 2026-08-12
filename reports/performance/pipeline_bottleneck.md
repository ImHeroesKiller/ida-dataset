# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T15:15:28+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 411 | 1.48 | 70.9 | 610.3 |
| source_discovery | 411 | 4.31 | 186.3 | 1770.2 |
| connector | 411 | 90361.52 | 97806.1 | 37138586.6 |
| document_discovery | 411 | 90361.71 | 97806.2 | 37138662.4 |
| document_download | 411 | 236400.05 | 1509355.9 | 97160422.2 |
| extraction | 411 | 99.37 | 274.0 | 40839.5 |
| candidate_validation | 411 | 15.74 | 149.0 | 6468.0 |
| publish_queue | 411 | 15.8 | 149.1 | 6494.6 |
| append_dataset | 411 | 38.63 | 119.7 | 15878.3 |
| export | 411 | 0.35 | 2.7 | 144.0 |
| git_commit | 411 | 0.35 | 15.1 | 143.7 |
| push | 411 | 0.64 | 81.1 | 262.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12231 |
| Documents processed | 26936 |
| Process ratio | 220.2% (target ≥90.0%) |
| Rows published (traces) | 1984 |
| Sessions observed | 302 |
| Avg session duration (s) | 1057.566 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 14004.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
