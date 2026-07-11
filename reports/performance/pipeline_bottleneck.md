# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T14:47:54+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 17 | 0.89 | 1.3 | 15.1 |
| source_discovery | 17 | 2.42 | 2.9 | 41.2 |
| connector | 17 | 21220.08 | 94176.1 | 360741.3 |
| document_discovery | 17 | 21220.25 | 94176.2 | 360744.2 |
| document_download | 17 | 106499.27 | 1263152.2 | 1810487.6 |
| extraction | 17 | 27.98 | 63.4 | 475.7 |
| candidate_validation | 17 | 4.16 | 6.9 | 70.8 |
| publish_queue | 17 | 4.17 | 6.9 | 70.9 |
| append_dataset | 17 | 16.18 | 119.7 | 275.1 |
| export | 17 | 0.33 | 0.6 | 5.6 |
| git_commit | 17 | 0.3 | 0.4 | 5.1 |
| push | 17 | 0.29 | 0.3 | 4.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 241 |
| Documents processed | 544 |
| Process ratio | 225.7% (target ≥90.0%) |
| Rows published (traces) | 43 |
| Sessions observed | 44 |
| Avg session duration (s) | 257.955 |
| Max session duration (s) | 2163.0 |
| Rows / session (productive) | 3.231 |
| Avg connector latency (ms) | 2448.5 |
| Worker utilization (est) | 0.437 |
| Idle fraction (est) | 0.563 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
