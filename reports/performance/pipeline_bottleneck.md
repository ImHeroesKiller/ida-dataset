# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T15:22:16+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 378 | 1.53 | 70.9 | 576.8 |
| source_discovery | 378 | 4.43 | 186.3 | 1674.3 |
| connector | 378 | 90042.71 | 97806.1 | 34036143.5 |
| document_discovery | 378 | 90042.9 | 97806.2 | 34036215.1 |
| document_download | 378 | 236996.76 | 1509355.9 | 89584776.5 |
| extraction | 378 | 98.03 | 274.0 | 37055.0 |
| candidate_validation | 378 | 15.01 | 149.0 | 5672.4 |
| publish_queue | 378 | 15.07 | 149.1 | 5697.5 |
| append_dataset | 378 | 38.79 | 119.7 | 14661.5 |
| export | 378 | 0.35 | 2.7 | 133.3 |
| git_commit | 378 | 0.35 | 15.1 | 132.5 |
| push | 378 | 0.61 | 81.1 | 229.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11228 |
| Documents processed | 25024 |
| Process ratio | 222.9% (target ≥90.0%) |
| Rows published (traces) | 1819 |
| Sessions observed | 308 |
| Avg session duration (s) | 1059.948 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13880.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
