# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T13:43:46+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 45 | 1.1 | 6.5 | 49.4 |
| source_discovery | 45 | 2.71 | 3.3 | 121.9 |
| connector | 45 | 60724.08 | 97806.1 | 2732583.5 |
| document_discovery | 45 | 60724.22 | 97806.2 | 2732589.9 |
| document_download | 45 | 216910.41 | 1509355.9 | 9760968.4 |
| extraction | 45 | 68.51 | 109.5 | 3083.1 |
| candidate_validation | 45 | 5.63 | 8.7 | 253.2 |
| publish_queue | 45 | 5.68 | 8.8 | 255.8 |
| append_dataset | 45 | 45.02 | 119.7 | 2025.7 |
| export | 45 | 0.34 | 0.6 | 15.4 |
| git_commit | 45 | 0.34 | 2.1 | 15.2 |
| push | 45 | 0.33 | 0.8 | 14.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1046 |
| Documents processed | 3923 |
| Process ratio | 375.0% (target ≥90.0%) |
| Rows published (traces) | 161 |
| Sessions observed | 73 |
| Avg session duration (s) | 579.041 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.211 |
| Avg connector latency (ms) | 13687.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **375.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
