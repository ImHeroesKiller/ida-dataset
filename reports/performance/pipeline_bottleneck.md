# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T23:19:35+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 304 | 1.53 | 70.9 | 464.5 |
| source_discovery | 304 | 4.29 | 186.3 | 1305.4 |
| connector | 304 | 89079.93 | 97806.1 | 27080300.2 |
| document_discovery | 304 | 89080.14 | 97806.2 | 27080361.8 |
| document_download | 304 | 234026.1 | 1509355.9 | 71143935.6 |
| extraction | 304 | 94.97 | 274.0 | 28871.3 |
| candidate_validation | 304 | 12.9 | 102.5 | 3922.5 |
| publish_queue | 304 | 12.98 | 102.7 | 3945.2 |
| append_dataset | 304 | 40.02 | 119.7 | 12166.1 |
| export | 304 | 0.35 | 2.1 | 105.5 |
| git_commit | 304 | 0.36 | 15.1 | 109.3 |
| push | 304 | 0.68 | 81.1 | 207.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8964 |
| Documents processed | 20896 |
| Process ratio | 233.1% (target ≥90.0%) |
| Rows published (traces) | 1449 |
| Sessions observed | 332 |
| Avg session duration (s) | 963.852 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.875 |
| Avg connector latency (ms) | 13717.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **233.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
