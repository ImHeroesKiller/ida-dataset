# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T02:08:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 350 | 1.58 | 70.9 | 551.4 |
| source_discovery | 350 | 4.57 | 186.3 | 1598.5 |
| connector | 350 | 89728.65 | 97806.1 | 31405026.2 |
| document_discovery | 350 | 89728.84 | 97806.2 | 31405093.7 |
| document_download | 350 | 232132.01 | 1509355.9 | 81246202.3 |
| extraction | 350 | 97.04 | 274.0 | 33964.6 |
| candidate_validation | 350 | 14.18 | 136.9 | 4961.5 |
| publish_queue | 350 | 14.24 | 136.9 | 4985.6 |
| append_dataset | 350 | 39.19 | 119.7 | 13718.1 |
| export | 350 | 0.35 | 2.1 | 121.6 |
| git_commit | 350 | 0.35 | 15.1 | 124.0 |
| push | 350 | 0.63 | 81.1 | 220.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10370 |
| Documents processed | 23427 |
| Process ratio | 225.9% (target ≥90.0%) |
| Rows published (traces) | 1679 |
| Sessions observed | 301 |
| Avg session duration (s) | 1066.14 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13858.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
