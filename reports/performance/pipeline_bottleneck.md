# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T07:58:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 296 | 1.36 | 70.9 | 402.8 |
| source_discovery | 296 | 4.33 | 186.3 | 1282.4 |
| connector | 296 | 88948.56 | 97806.1 | 26328772.8 |
| document_discovery | 296 | 88948.76 | 97806.2 | 26328833.5 |
| document_download | 296 | 235175.78 | 1509355.9 | 69612031.2 |
| extraction | 296 | 94.28 | 274.0 | 27907.0 |
| candidate_validation | 296 | 12.74 | 102.5 | 3769.7 |
| publish_queue | 296 | 12.81 | 102.7 | 3792.1 |
| append_dataset | 296 | 40.25 | 119.7 | 11913.8 |
| export | 296 | 0.35 | 2.1 | 102.9 |
| git_commit | 296 | 0.36 | 15.1 | 106.9 |
| push | 296 | 0.69 | 81.1 | 205.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8726 |
| Documents processed | 20530 |
| Process ratio | 235.3% (target ≥90.0%) |
| Rows published (traces) | 1409 |
| Sessions observed | 324 |
| Avg session duration (s) | 962.59 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.872 |
| Avg connector latency (ms) | 13767.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **235.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
