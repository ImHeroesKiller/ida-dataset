# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T16:04:20+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 140 | 1.0 | 6.5 | 140.0 |
| source_discovery | 140 | 3.15 | 39.8 | 441.6 |
| connector | 140 | 83307.18 | 97806.1 | 11663004.8 |
| document_discovery | 140 | 83307.32 | 97806.2 | 11663024.4 |
| document_download | 140 | 254868.22 | 1509355.9 | 35681551.3 |
| extraction | 140 | 85.06 | 274.0 | 11908.3 |
| candidate_validation | 140 | 8.57 | 30.0 | 1200.3 |
| publish_queue | 140 | 8.74 | 34.7 | 1223.2 |
| append_dataset | 140 | 44.18 | 119.7 | 6185.8 |
| export | 140 | 0.35 | 1.9 | 48.7 |
| git_commit | 140 | 0.32 | 2.1 | 44.2 |
| push | 140 | 0.31 | 0.8 | 43.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3931 |
| Documents processed | 11466 |
| Process ratio | 291.7% (target ≥90.0%) |
| Rows published (traces) | 632 |
| Sessions observed | 168 |
| Avg session duration (s) | 881.542 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.744 |
| Avg connector latency (ms) | 13685.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **291.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
