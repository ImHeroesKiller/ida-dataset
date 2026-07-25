# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T00:27:24+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 176 | 0.99 | 6.5 | 174.0 |
| source_discovery | 176 | 3.1 | 39.8 | 544.8 |
| connector | 176 | 85496.39 | 97806.1 | 15047364.3 |
| document_discovery | 176 | 85496.54 | 97806.2 | 15047390.6 |
| document_download | 176 | 252927.06 | 1509355.9 | 44515162.1 |
| extraction | 176 | 87.39 | 274.0 | 15381.4 |
| candidate_validation | 176 | 9.47 | 30.0 | 1667.2 |
| publish_queue | 176 | 9.61 | 34.7 | 1691.2 |
| append_dataset | 176 | 43.27 | 119.7 | 7615.3 |
| export | 176 | 0.35 | 1.9 | 61.9 |
| git_commit | 176 | 0.31 | 2.1 | 55.0 |
| push | 176 | 0.31 | 0.8 | 55.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5037 |
| Documents processed | 13806 |
| Process ratio | 274.1% (target ≥90.0%) |
| Rows published (traces) | 812 |
| Sessions observed | 204 |
| Avg session duration (s) | 917.402 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.799 |
| Avg connector latency (ms) | 13735.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **274.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
