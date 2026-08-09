# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T22:52:33+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 369 | 1.54 | 70.9 | 568.4 |
| source_discovery | 369 | 4.47 | 186.3 | 1649.5 |
| connector | 369 | 89947.61 | 97806.1 | 33190666.9 |
| document_discovery | 369 | 89947.8 | 97806.2 | 33190737.6 |
| document_download | 369 | 235221.32 | 1509355.9 | 86796666.4 |
| extraction | 369 | 97.54 | 274.0 | 35991.7 |
| candidate_validation | 369 | 14.48 | 136.9 | 5343.1 |
| publish_queue | 369 | 14.55 | 136.9 | 5367.8 |
| append_dataset | 369 | 38.9 | 119.7 | 14352.8 |
| export | 369 | 0.35 | 2.1 | 127.5 |
| git_commit | 369 | 0.35 | 15.1 | 129.7 |
| push | 369 | 0.61 | 81.1 | 226.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10959 |
| Documents processed | 24531 |
| Process ratio | 223.8% (target ≥90.0%) |
| Rows published (traces) | 1774 |
| Sessions observed | 309 |
| Avg session duration (s) | 1064.835 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13754.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
