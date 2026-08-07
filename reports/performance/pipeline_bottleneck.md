# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T09:17:16+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 314 | 1.51 | 70.9 | 474.2 |
| source_discovery | 314 | 4.25 | 186.3 | 1333.5 |
| connector | 314 | 89238.92 | 97806.1 | 28021022.1 |
| document_discovery | 314 | 89239.12 | 97806.2 | 28021084.9 |
| document_download | 314 | 233020.88 | 1509355.9 | 73168556.6 |
| extraction | 314 | 95.3 | 274.0 | 29923.0 |
| candidate_validation | 314 | 13.11 | 102.5 | 4117.2 |
| publish_queue | 314 | 13.19 | 102.7 | 4140.1 |
| append_dataset | 314 | 39.87 | 119.7 | 12519.6 |
| export | 314 | 0.35 | 2.1 | 108.6 |
| git_commit | 314 | 0.36 | 15.1 | 112.3 |
| push | 314 | 0.67 | 81.1 | 210.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9274 |
| Documents processed | 21468 |
| Process ratio | 231.5% (target ≥90.0%) |
| Rows published (traces) | 1499 |
| Sessions observed | 310 |
| Avg session duration (s) | 1057.065 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.93 |
| Avg connector latency (ms) | 13833.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **231.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
