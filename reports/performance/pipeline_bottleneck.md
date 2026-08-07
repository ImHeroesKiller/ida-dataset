# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T18:12:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 321 | 1.63 | 70.9 | 522.1 |
| source_discovery | 321 | 4.72 | 186.3 | 1515.1 |
| connector | 321 | 89342.19 | 97806.1 | 28678842.3 |
| document_discovery | 321 | 89342.39 | 97806.2 | 28678905.8 |
| document_download | 321 | 232503.9 | 1509355.9 | 74633751.6 |
| extraction | 321 | 95.81 | 274.0 | 30754.8 |
| candidate_validation | 321 | 13.62 | 136.9 | 4371.6 |
| publish_queue | 321 | 13.69 | 136.9 | 4394.7 |
| append_dataset | 321 | 39.68 | 119.7 | 12735.9 |
| export | 321 | 0.34 | 2.1 | 110.7 |
| git_commit | 321 | 0.36 | 15.1 | 114.2 |
| push | 321 | 0.66 | 81.1 | 212.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9491 |
| Documents processed | 21827 |
| Process ratio | 230.0% (target ≥90.0%) |
| Rows published (traces) | 1534 |
| Sessions observed | 317 |
| Avg session duration (s) | 1057.107 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.932 |
| Avg connector latency (ms) | 13811.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **230.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
