# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T14:13:44+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 77 | 1.04 | 6.5 | 79.9 |
| source_discovery | 77 | 2.75 | 3.3 | 211.4 |
| connector | 77 | 74547.58 | 97806.1 | 5740163.6 |
| document_discovery | 77 | 74547.72 | 97806.2 | 5740174.4 |
| document_download | 77 | 269230.04 | 1509355.9 | 20730713.2 |
| extraction | 77 | 82.64 | 274.0 | 6363.0 |
| candidate_validation | 77 | 6.86 | 18.7 | 528.2 |
| publish_queue | 77 | 7.11 | 34.7 | 547.7 |
| append_dataset | 77 | 50.51 | 119.7 | 3889.2 |
| export | 77 | 0.34 | 0.6 | 26.0 |
| git_commit | 77 | 0.32 | 2.1 | 25.0 |
| push | 77 | 0.32 | 0.8 | 24.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2018 |
| Documents processed | 7547 |
| Process ratio | 374.0% (target ≥90.0%) |
| Rows published (traces) | 317 |
| Sessions observed | 105 |
| Avg session duration (s) | 767.743 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.514 |
| Avg connector latency (ms) | 13721.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **374.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
