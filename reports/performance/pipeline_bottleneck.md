# Pipeline Bottleneck Analysis

**Generated:** 2026-07-28T18:32:20+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 216 | 1.32 | 70.9 | 284.7 |
| source_discovery | 216 | 3.91 | 186.3 | 845.6 |
| connector | 216 | 87075.8 | 97806.1 | 18808373.5 |
| document_discovery | 216 | 87075.95 | 97806.2 | 18808404.8 |
| document_download | 216 | 249780.87 | 1509355.9 | 53952668.3 |
| extraction | 216 | 90.46 | 274.0 | 19539.1 |
| candidate_validation | 216 | 10.55 | 37.2 | 2278.0 |
| publish_queue | 216 | 10.66 | 37.4 | 2303.4 |
| append_dataset | 216 | 42.31 | 119.7 | 9138.0 |
| export | 216 | 0.35 | 1.9 | 75.2 |
| git_commit | 216 | 0.31 | 2.1 | 67.4 |
| push | 216 | 0.32 | 0.8 | 68.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6257 |
| Documents processed | 16156 |
| Process ratio | 258.2% (target ≥90.0%) |
| Rows published (traces) | 1009 |
| Sessions observed | 244 |
| Avg session duration (s) | 943.258 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.823 |
| Avg connector latency (ms) | 13764.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **258.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
