# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T19:53:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 366 | 1.55 | 70.9 | 565.7 |
| source_discovery | 366 | 4.49 | 186.3 | 1641.7 |
| connector | 366 | 89914.57 | 97806.1 | 32908731.3 |
| document_discovery | 366 | 89914.76 | 97806.2 | 32908801.6 |
| document_download | 366 | 233328.08 | 1509355.9 | 85398075.6 |
| extraction | 366 | 97.31 | 274.0 | 35615.8 |
| candidate_validation | 366 | 14.44 | 136.9 | 5286.6 |
| publish_queue | 366 | 14.51 | 136.9 | 5311.0 |
| append_dataset | 366 | 38.95 | 119.7 | 14257.0 |
| export | 366 | 0.35 | 2.1 | 126.5 |
| git_commit | 366 | 0.35 | 15.1 | 128.5 |
| push | 366 | 0.62 | 81.1 | 225.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10866 |
| Documents processed | 24356 |
| Process ratio | 224.1% (target ≥90.0%) |
| Rows published (traces) | 1759 |
| Sessions observed | 306 |
| Avg session duration (s) | 1062.542 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13807.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **224.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
