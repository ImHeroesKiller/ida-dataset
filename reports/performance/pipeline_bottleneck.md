# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T18:54:30+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 20 | 0.89 | 1.3 | 17.8 |
| source_discovery | 20 | 2.49 | 3.0 | 49.7 |
| connector | 20 | 27941.88 | 97806.1 | 558837.6 |
| document_discovery | 20 | 27942.05 | 97806.2 | 558841.0 |
| document_download | 20 | 190155.58 | 1509355.9 | 3803111.7 |
| extraction | 20 | 36.33 | 93.4 | 726.6 |
| candidate_validation | 20 | 4.15 | 6.9 | 83.0 |
| publish_queue | 20 | 4.16 | 6.9 | 83.2 |
| append_dataset | 20 | 19.99 | 119.7 | 399.7 |
| export | 20 | 0.32 | 0.6 | 6.4 |
| git_commit | 20 | 0.29 | 0.4 | 5.9 |
| push | 20 | 0.29 | 0.3 | 5.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 311 |
| Documents processed | 811 |
| Process ratio | 260.8% (target ≥90.0%) |
| Rows published (traces) | 50 |
| Sessions observed | 48 |
| Avg session duration (s) | 324.271 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.267 |
| Avg connector latency (ms) | 2522.2 |
| Worker utilization (est) | 0.621 |
| Idle fraction (est) | 0.379 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **260.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
