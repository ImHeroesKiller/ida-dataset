# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T19:33:27+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 80 | 1.03 | 6.5 | 82.3 |
| source_discovery | 80 | 2.74 | 3.3 | 219.4 |
| connector | 80 | 75281.04 | 97806.1 | 6022483.2 |
| document_discovery | 80 | 75281.18 | 97806.2 | 6022494.4 |
| document_download | 80 | 265529.16 | 1509355.9 | 21242333.1 |
| extraction | 80 | 82.59 | 274.0 | 6607.5 |
| candidate_validation | 80 | 6.89 | 18.7 | 551.0 |
| publish_queue | 80 | 7.13 | 34.7 | 570.7 |
| append_dataset | 80 | 49.58 | 119.7 | 3966.8 |
| export | 80 | 0.34 | 0.6 | 26.8 |
| git_commit | 80 | 0.32 | 2.1 | 25.9 |
| push | 80 | 0.32 | 0.8 | 25.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2111 |
| Documents processed | 7680 |
| Process ratio | 363.8% (target ≥90.0%) |
| Rows published (traces) | 332 |
| Sessions observed | 108 |
| Avg session duration (s) | 772.704 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.534 |
| Avg connector latency (ms) | 13804.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **363.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
