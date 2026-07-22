# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T04:35:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 146 | 1.0 | 6.5 | 145.3 |
| source_discovery | 146 | 3.14 | 39.8 | 458.8 |
| connector | 146 | 83747.83 | 97806.1 | 12227183.4 |
| document_discovery | 146 | 83747.98 | 97806.2 | 12227205.7 |
| document_download | 146 | 254657.12 | 1509355.9 | 37179939.9 |
| extraction | 146 | 85.47 | 274.0 | 12479.3 |
| candidate_validation | 146 | 8.72 | 30.0 | 1273.0 |
| publish_queue | 146 | 8.88 | 34.7 | 1296.4 |
| append_dataset | 146 | 43.92 | 119.7 | 6412.6 |
| export | 146 | 0.35 | 1.9 | 50.5 |
| git_commit | 146 | 0.32 | 2.1 | 46.0 |
| push | 146 | 0.31 | 0.8 | 45.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4117 |
| Documents processed | 11864 |
| Process ratio | 288.2% (target ≥90.0%) |
| Rows published (traces) | 662 |
| Sessions observed | 174 |
| Avg session duration (s) | 888.828 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.755 |
| Avg connector latency (ms) | 13814.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **288.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
