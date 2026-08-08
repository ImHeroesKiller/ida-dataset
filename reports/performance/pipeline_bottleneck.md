# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T20:50:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 346 | 1.58 | 70.9 | 547.0 |
| source_discovery | 346 | 4.58 | 186.3 | 1586.0 |
| connector | 346 | 89678.66 | 97806.1 | 31028816.2 |
| document_discovery | 346 | 89678.85 | 97806.2 | 31028883.3 |
| document_download | 346 | 231766.31 | 1509355.9 | 80191141.8 |
| extraction | 346 | 96.87 | 274.0 | 33515.4 |
| candidate_validation | 346 | 14.08 | 136.9 | 4872.7 |
| publish_queue | 346 | 14.15 | 136.9 | 4896.5 |
| append_dataset | 346 | 39.23 | 119.7 | 13574.7 |
| export | 346 | 0.35 | 2.1 | 120.2 |
| git_commit | 346 | 0.35 | 15.1 | 122.7 |
| push | 346 | 0.63 | 81.1 | 219.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10246 |
| Documents processed | 23210 |
| Process ratio | 226.5% (target ≥90.0%) |
| Rows published (traces) | 1659 |
| Sessions observed | 306 |
| Avg session duration (s) | 1067.056 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.977 |
| Avg connector latency (ms) | 13698.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **226.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
