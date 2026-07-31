# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T00:21:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 241 | 1.28 | 70.9 | 309.5 |
| source_discovery | 241 | 3.8 | 186.3 | 915.7 |
| connector | 241 | 87794.99 | 97806.1 | 21158592.4 |
| document_discovery | 241 | 87795.21 | 97806.2 | 21158645.8 |
| document_download | 241 | 244198.71 | 1509355.9 | 58851888.8 |
| extraction | 241 | 92.21 | 274.0 | 22223.3 |
| candidate_validation | 241 | 11.57 | 102.5 | 2789.3 |
| publish_queue | 241 | 11.66 | 102.7 | 2810.4 |
| append_dataset | 241 | 41.71 | 119.7 | 10052.1 |
| export | 241 | 0.35 | 1.9 | 83.4 |
| git_commit | 241 | 0.37 | 15.1 | 90.0 |
| push | 241 | 0.65 | 81.1 | 156.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7032 |
| Documents processed | 17575 |
| Process ratio | 249.9% (target ≥90.0%) |
| Rows published (traces) | 1134 |
| Sessions observed | 269 |
| Avg session duration (s) | 952.405 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.842 |
| Avg connector latency (ms) | 13886.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **249.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
