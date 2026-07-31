# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T23:20:30+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 251 | 1.27 | 70.9 | 319.0 |
| source_discovery | 251 | 3.76 | 186.3 | 944.1 |
| connector | 251 | 88042.84 | 97806.1 | 22098753.2 |
| document_discovery | 251 | 88043.06 | 97806.2 | 22098807.8 |
| document_download | 251 | 239581.1 | 1509355.9 | 60134855.4 |
| extraction | 251 | 92.61 | 274.0 | 23244.2 |
| candidate_validation | 251 | 11.86 | 102.5 | 2977.5 |
| publish_queue | 251 | 11.95 | 102.7 | 2999.2 |
| append_dataset | 251 | 41.44 | 119.7 | 10402.3 |
| export | 251 | 0.35 | 2.1 | 88.3 |
| git_commit | 251 | 0.37 | 15.1 | 92.9 |
| push | 251 | 0.64 | 81.1 | 159.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7342 |
| Documents processed | 18132 |
| Process ratio | 247.0% (target ≥90.0%) |
| Rows published (traces) | 1184 |
| Sessions observed | 279 |
| Avg session duration (s) | 953.086 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.848 |
| Avg connector latency (ms) | 14184.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **247.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
