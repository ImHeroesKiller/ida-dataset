# Pipeline Bottleneck Analysis

**Generated:** 2026-08-06T11:43:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 308 | 1.52 | 70.9 | 468.4 |
| source_discovery | 308 | 4.27 | 186.3 | 1316.6 |
| connector | 308 | 89147.46 | 97806.1 | 27457418.7 |
| document_discovery | 308 | 89147.66 | 97806.2 | 27457480.7 |
| document_download | 308 | 233751.56 | 1509355.9 | 71995479.1 |
| extraction | 308 | 95.19 | 274.0 | 29319.4 |
| candidate_validation | 308 | 12.99 | 102.5 | 4001.3 |
| publish_queue | 308 | 13.07 | 102.7 | 4024.1 |
| append_dataset | 308 | 39.97 | 119.7 | 12312.0 |
| export | 308 | 0.35 | 2.1 | 106.8 |
| git_commit | 308 | 0.36 | 15.1 | 110.6 |
| push | 308 | 0.68 | 81.1 | 208.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9088 |
| Documents processed | 21130 |
| Process ratio | 232.5% (target ≥90.0%) |
| Rows published (traces) | 1469 |
| Sessions observed | 304 |
| Avg session duration (s) | 1057.688 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.929 |
| Avg connector latency (ms) | 13895.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **232.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
