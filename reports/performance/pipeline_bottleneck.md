# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T19:28:26+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 105 | 1.02 | 6.5 | 106.7 |
| source_discovery | 105 | 2.77 | 3.5 | 291.3 |
| connector | 105 | 79746.16 | 97806.1 | 8373346.7 |
| document_discovery | 105 | 79746.3 | 97806.2 | 8373361.5 |
| document_download | 105 | 266916.25 | 1509355.9 | 28026205.9 |
| extraction | 105 | 83.24 | 274.0 | 8740.1 |
| candidate_validation | 105 | 7.57 | 18.7 | 794.5 |
| publish_queue | 105 | 7.78 | 34.7 | 816.5 |
| append_dataset | 105 | 46.58 | 119.7 | 4891.1 |
| export | 105 | 0.34 | 0.7 | 35.6 |
| git_commit | 105 | 0.32 | 2.1 | 33.7 |
| push | 105 | 0.31 | 0.8 | 33.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2876 |
| Documents processed | 9253 |
| Process ratio | 321.7% (target ≥90.0%) |
| Rows published (traces) | 457 |
| Sessions observed | 133 |
| Avg session duration (s) | 835.835 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.653 |
| Avg connector latency (ms) | 13773.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **321.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
