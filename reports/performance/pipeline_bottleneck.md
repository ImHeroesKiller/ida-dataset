# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T22:53:21+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 348 | 1.58 | 70.9 | 549.1 |
| source_discovery | 348 | 4.58 | 186.3 | 1592.5 |
| connector | 348 | 89703.91 | 97806.1 | 31216959.3 |
| document_discovery | 348 | 89704.1 | 97806.2 | 31217026.6 |
| document_download | 348 | 231776.5 | 1509355.9 | 80658223.7 |
| extraction | 348 | 96.94 | 274.0 | 33735.0 |
| candidate_validation | 348 | 14.13 | 136.9 | 4917.5 |
| publish_queue | 348 | 14.2 | 136.9 | 4941.4 |
| append_dataset | 348 | 39.19 | 119.7 | 13639.0 |
| export | 348 | 0.35 | 2.1 | 120.9 |
| git_commit | 348 | 0.35 | 15.1 | 123.4 |
| push | 348 | 0.63 | 81.1 | 220.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10308 |
| Documents processed | 23303 |
| Process ratio | 226.1% (target ≥90.0%) |
| Rows published (traces) | 1669 |
| Sessions observed | 308 |
| Avg session duration (s) | 1067.166 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.977 |
| Avg connector latency (ms) | 13809.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **226.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
