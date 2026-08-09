# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T09:07:47+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 355 | 1.57 | 70.9 | 555.8 |
| source_discovery | 355 | 4.54 | 186.3 | 1611.9 |
| connector | 355 | 89789.02 | 97806.1 | 31875103.4 |
| document_discovery | 355 | 89789.22 | 97806.2 | 31875171.8 |
| document_download | 355 | 231533.31 | 1509355.9 | 82194323.5 |
| extraction | 355 | 97.19 | 274.0 | 34501.6 |
| candidate_validation | 355 | 14.26 | 136.9 | 5061.0 |
| publish_queue | 355 | 14.32 | 136.9 | 5085.2 |
| append_dataset | 355 | 39.11 | 119.7 | 13882.7 |
| export | 355 | 0.35 | 2.1 | 123.3 |
| git_commit | 355 | 0.35 | 15.1 | 125.4 |
| push | 355 | 0.63 | 81.1 | 222.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10525 |
| Documents processed | 23718 |
| Process ratio | 225.3% (target ≥90.0%) |
| Rows published (traces) | 1704 |
| Sessions observed | 306 |
| Avg session duration (s) | 1065.582 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13744.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
