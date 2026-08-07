# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T04:07:24+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 311 | 1.52 | 70.9 | 471.4 |
| source_discovery | 311 | 4.26 | 186.3 | 1325.4 |
| connector | 311 | 89194.22 | 97806.1 | 27739403.0 |
| document_discovery | 311 | 89194.42 | 97806.2 | 27739465.4 |
| document_download | 311 | 233941.77 | 1509355.9 | 72755891.6 |
| extraction | 311 | 95.35 | 274.0 | 29653.6 |
| candidate_validation | 311 | 13.06 | 102.5 | 4062.1 |
| publish_queue | 311 | 13.14 | 102.7 | 4085.0 |
| append_dataset | 311 | 39.95 | 119.7 | 12425.4 |
| export | 311 | 0.35 | 2.1 | 107.7 |
| git_commit | 311 | 0.36 | 15.1 | 111.5 |
| push | 311 | 0.67 | 81.1 | 209.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9181 |
| Documents processed | 21305 |
| Process ratio | 232.1% (target ≥90.0%) |
| Rows published (traces) | 1484 |
| Sessions observed | 307 |
| Avg session duration (s) | 1058.107 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.93 |
| Avg connector latency (ms) | 13664.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **232.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
