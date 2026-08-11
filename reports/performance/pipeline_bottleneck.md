# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T02:10:13+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 387 | 1.51 | 70.9 | 585.9 |
| source_discovery | 387 | 4.39 | 186.3 | 1700.8 |
| connector | 387 | 90134.16 | 97806.1 | 34881921.7 |
| document_discovery | 387 | 90134.35 | 97806.2 | 34881994.7 |
| document_download | 387 | 237830.68 | 1509355.9 | 92040474.6 |
| extraction | 387 | 98.41 | 274.0 | 38086.2 |
| candidate_validation | 387 | 15.22 | 149.0 | 5889.3 |
| publish_queue | 387 | 15.28 | 149.1 | 5914.6 |
| append_dataset | 387 | 38.77 | 119.7 | 15004.2 |
| export | 387 | 0.35 | 2.7 | 136.4 |
| git_commit | 387 | 0.35 | 15.1 | 135.7 |
| push | 387 | 0.6 | 81.1 | 232.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11497 |
| Documents processed | 25546 |
| Process ratio | 222.2% (target ≥90.0%) |
| Rows published (traces) | 1864 |
| Sessions observed | 305 |
| Avg session duration (s) | 1062.177 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13834.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
