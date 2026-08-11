# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T22:09:01+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 400 | 1.5 | 70.9 | 598.3 |
| source_discovery | 400 | 4.34 | 186.3 | 1737.5 |
| connector | 400 | 90261.18 | 97806.1 | 36104471.1 |
| document_discovery | 400 | 90261.36 | 97806.2 | 36104545.7 |
| document_download | 400 | 236430.83 | 1509355.9 | 94572332.8 |
| extraction | 400 | 98.94 | 274.0 | 39574.1 |
| candidate_validation | 400 | 15.46 | 149.0 | 6185.1 |
| publish_queue | 400 | 15.53 | 149.1 | 6211.2 |
| append_dataset | 400 | 38.7 | 119.7 | 15478.3 |
| export | 400 | 0.35 | 2.7 | 140.4 |
| git_commit | 400 | 0.35 | 15.1 | 140.0 |
| push | 400 | 0.59 | 81.1 | 235.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11900 |
| Documents processed | 26319 |
| Process ratio | 221.2% (target ≥90.0%) |
| Rows published (traces) | 1929 |
| Sessions observed | 305 |
| Avg session duration (s) | 1058.187 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13850.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
