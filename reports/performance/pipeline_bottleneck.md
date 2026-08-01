# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T06:17:05+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 253 | 1.27 | 70.9 | 321.0 |
| source_discovery | 253 | 3.75 | 186.3 | 949.8 |
| connector | 253 | 88088.19 | 97806.1 | 22286313.3 |
| document_discovery | 253 | 88088.41 | 97806.2 | 22286368.2 |
| document_download | 253 | 239212.52 | 1509355.9 | 60520768.1 |
| extraction | 253 | 92.62 | 274.0 | 23432.3 |
| candidate_validation | 253 | 11.91 | 102.5 | 3012.3 |
| publish_queue | 253 | 11.99 | 102.7 | 3034.1 |
| append_dataset | 253 | 41.39 | 119.7 | 10472.4 |
| export | 253 | 0.35 | 2.1 | 89.0 |
| git_commit | 253 | 0.37 | 15.1 | 93.5 |
| push | 253 | 0.63 | 81.1 | 160.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7393 |
| Documents processed | 18245 |
| Process ratio | 246.8% (target ≥90.0%) |
| Rows published (traces) | 1194 |
| Sessions observed | 281 |
| Avg session duration (s) | 953.751 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.85 |
| Avg connector latency (ms) | 13665.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **246.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
