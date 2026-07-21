# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T23:18:05+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 144 | 1.0 | 6.5 | 143.7 |
| source_discovery | 144 | 3.15 | 39.8 | 453.3 |
| connector | 144 | 83603.95 | 97806.1 | 12038969.3 |
| document_discovery | 144 | 83604.09 | 97806.2 | 12038989.5 |
| document_download | 144 | 254712.69 | 1509355.9 | 36678626.8 |
| extraction | 144 | 85.36 | 274.0 | 12291.6 |
| candidate_validation | 144 | 8.69 | 30.0 | 1251.7 |
| publish_queue | 144 | 8.85 | 34.7 | 1275.1 |
| append_dataset | 144 | 44.03 | 119.7 | 6340.3 |
| export | 144 | 0.35 | 1.9 | 49.9 |
| git_commit | 144 | 0.32 | 2.1 | 45.4 |
| push | 144 | 0.31 | 0.8 | 45.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4055 |
| Documents processed | 11716 |
| Process ratio | 288.9% (target ≥90.0%) |
| Rows published (traces) | 652 |
| Sessions observed | 172 |
| Avg session duration (s) | 886.372 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.752 |
| Avg connector latency (ms) | 15334.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **288.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
