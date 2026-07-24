# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T17:07:01+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 172 | 0.99 | 6.5 | 169.8 |
| source_discovery | 172 | 3.1 | 39.8 | 533.5 |
| connector | 172 | 85299.77 | 97806.1 | 14671559.6 |
| document_discovery | 172 | 85299.92 | 97806.2 | 14671585.5 |
| document_download | 172 | 252391.27 | 1509355.9 | 43411298.6 |
| extraction | 172 | 87.33 | 274.0 | 15020.4 |
| candidate_validation | 172 | 9.39 | 30.0 | 1614.6 |
| publish_queue | 172 | 9.53 | 34.7 | 1638.6 |
| append_dataset | 172 | 43.43 | 119.7 | 7470.1 |
| export | 172 | 0.35 | 1.9 | 60.4 |
| git_commit | 172 | 0.31 | 2.1 | 53.9 |
| push | 172 | 0.31 | 0.8 | 54.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4913 |
| Documents processed | 13569 |
| Process ratio | 276.2% (target ≥90.0%) |
| Rows published (traces) | 792 |
| Sessions observed | 200 |
| Avg session duration (s) | 913.385 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.794 |
| Avg connector latency (ms) | 15155.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **276.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
