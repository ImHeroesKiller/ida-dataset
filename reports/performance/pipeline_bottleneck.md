# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T07:52:08+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 147 | 0.99 | 6.5 | 146.1 |
| source_discovery | 147 | 3.14 | 39.8 | 461.6 |
| connector | 147 | 83815.63 | 97806.1 | 12320897.7 |
| document_discovery | 147 | 83815.78 | 97806.2 | 12320920.1 |
| document_download | 147 | 254162.9 | 1509355.9 | 37361946.2 |
| extraction | 147 | 85.56 | 274.0 | 12577.4 |
| candidate_validation | 147 | 8.74 | 30.0 | 1285.5 |
| publish_queue | 147 | 8.9 | 34.7 | 1308.9 |
| append_dataset | 147 | 43.93 | 119.7 | 6457.7 |
| export | 147 | 0.35 | 1.9 | 51.0 |
| git_commit | 147 | 0.31 | 2.1 | 46.3 |
| push | 147 | 0.31 | 0.8 | 46.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4148 |
| Documents processed | 11938 |
| Process ratio | 287.8% (target ≥90.0%) |
| Rows published (traces) | 667 |
| Sessions observed | 175 |
| Avg session duration (s) | 889.663 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.757 |
| Avg connector latency (ms) | 13748.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **287.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
