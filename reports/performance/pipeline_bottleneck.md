# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T18:15:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 118 | 1.0 | 6.5 | 118.3 |
| source_discovery | 118 | 3.08 | 39.8 | 363.3 |
| connector | 118 | 81315.15 | 97806.1 | 9595187.8 |
| document_discovery | 118 | 81315.29 | 97806.2 | 9595204.2 |
| document_download | 118 | 269004.76 | 1509355.9 | 31742561.8 |
| extraction | 118 | 82.2 | 274.0 | 9699.4 |
| candidate_validation | 118 | 7.96 | 30.0 | 939.5 |
| publish_queue | 118 | 8.15 | 34.7 | 961.5 |
| append_dataset | 118 | 45.25 | 119.7 | 5340.0 |
| export | 118 | 0.34 | 0.7 | 40.2 |
| git_commit | 118 | 0.32 | 2.1 | 37.3 |
| push | 118 | 0.31 | 0.8 | 36.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3269 |
| Documents processed | 10065 |
| Process ratio | 307.9% (target ≥90.0%) |
| Rows published (traces) | 522 |
| Sessions observed | 146 |
| Avg session duration (s) | 861.226 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.694 |
| Avg connector latency (ms) | 13687.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **307.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
