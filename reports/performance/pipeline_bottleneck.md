# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T10:03:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 356 | 1.56 | 70.9 | 556.8 |
| source_discovery | 356 | 4.54 | 186.3 | 1614.9 |
| connector | 356 | 89801.5 | 97806.1 | 31969333.0 |
| document_discovery | 356 | 89801.69 | 97806.2 | 31969401.5 |
| document_download | 356 | 231324.28 | 1509355.9 | 82351444.0 |
| extraction | 356 | 97.25 | 274.0 | 34619.7 |
| candidate_validation | 356 | 14.28 | 136.9 | 5083.6 |
| publish_queue | 356 | 14.35 | 136.9 | 5107.8 |
| append_dataset | 356 | 39.1 | 119.7 | 13921.0 |
| export | 356 | 0.35 | 2.1 | 123.6 |
| git_commit | 356 | 0.35 | 15.1 | 125.7 |
| push | 356 | 0.63 | 81.1 | 222.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10556 |
| Documents processed | 23780 |
| Process ratio | 225.3% (target ≥90.0%) |
| Rows published (traces) | 1709 |
| Sessions observed | 307 |
| Avg session duration (s) | 1065.326 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13749.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
