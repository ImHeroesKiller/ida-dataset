# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T10:22:24+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 392 | 1.51 | 70.9 | 590.9 |
| source_discovery | 392 | 4.38 | 186.3 | 1715.2 |
| connector | 392 | 90181.56 | 97806.1 | 35351170.5 |
| document_discovery | 392 | 90181.74 | 97806.2 | 35351244.0 |
| document_download | 392 | 237211.32 | 1509355.9 | 92986838.4 |
| extraction | 392 | 98.56 | 274.0 | 38636.8 |
| candidate_validation | 392 | 15.31 | 149.0 | 6002.4 |
| publish_queue | 392 | 15.38 | 149.1 | 6028.1 |
| append_dataset | 392 | 38.75 | 119.7 | 15188.5 |
| export | 392 | 0.35 | 2.7 | 137.8 |
| git_commit | 392 | 0.35 | 15.1 | 137.1 |
| push | 392 | 0.6 | 81.1 | 233.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11652 |
| Documents processed | 25845 |
| Process ratio | 221.8% (target ≥90.0%) |
| Rows published (traces) | 1889 |
| Sessions observed | 310 |
| Avg session duration (s) | 1061.665 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13930.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
