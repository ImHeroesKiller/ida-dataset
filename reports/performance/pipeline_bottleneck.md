# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T13:08:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 338 | 1.59 | 70.9 | 538.6 |
| source_discovery | 338 | 4.62 | 186.3 | 1563.1 |
| connector | 338 | 89575.61 | 97806.1 | 30276557.4 |
| document_discovery | 338 | 89575.81 | 97806.2 | 30276623.2 |
| document_download | 338 | 232294.86 | 1509355.9 | 78515662.6 |
| extraction | 338 | 96.57 | 274.0 | 32639.4 |
| candidate_validation | 338 | 13.94 | 136.9 | 4712.2 |
| publish_queue | 338 | 14.01 | 136.9 | 4735.9 |
| append_dataset | 338 | 39.42 | 119.7 | 13324.5 |
| export | 338 | 0.34 | 2.1 | 116.2 |
| git_commit | 338 | 0.36 | 15.1 | 120.2 |
| push | 338 | 0.64 | 81.1 | 217.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10008 |
| Documents processed | 22807 |
| Process ratio | 227.9% (target ≥90.0%) |
| Rows published (traces) | 1619 |
| Sessions observed | 313 |
| Avg session duration (s) | 1067.163 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.965 |
| Avg connector latency (ms) | 13718.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **227.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
