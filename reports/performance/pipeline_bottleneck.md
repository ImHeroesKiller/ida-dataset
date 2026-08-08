# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T19:50:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 345 | 1.58 | 70.9 | 545.9 |
| source_discovery | 345 | 4.59 | 186.3 | 1583.3 |
| connector | 345 | 89666.13 | 97806.1 | 30934814.1 |
| document_discovery | 345 | 89666.32 | 97806.2 | 30934880.9 |
| document_download | 345 | 231716.66 | 1509355.9 | 79942247.7 |
| extraction | 345 | 96.83 | 274.0 | 33405.1 |
| candidate_validation | 345 | 14.07 | 136.9 | 4855.3 |
| publish_queue | 345 | 14.14 | 136.9 | 4879.0 |
| append_dataset | 345 | 39.26 | 119.7 | 13544.3 |
| export | 345 | 0.35 | 2.1 | 119.8 |
| git_commit | 345 | 0.35 | 15.1 | 122.2 |
| push | 345 | 0.64 | 81.1 | 219.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10215 |
| Documents processed | 23148 |
| Process ratio | 226.6% (target ≥90.0%) |
| Rows published (traces) | 1654 |
| Sessions observed | 305 |
| Avg session duration (s) | 1066.944 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.977 |
| Avg connector latency (ms) | 13966.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **226.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
