# Pipeline Bottleneck Analysis

**Generated:** 2026-07-28T20:35:17+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 217 | 1.32 | 70.9 | 285.7 |
| source_discovery | 217 | 3.91 | 186.3 | 848.3 |
| connector | 217 | 87107.7 | 97806.1 | 18902370.9 |
| document_discovery | 217 | 87107.85 | 97806.2 | 18902402.4 |
| document_download | 217 | 249195.19 | 1509355.9 | 54075356.3 |
| extraction | 217 | 90.54 | 274.0 | 19646.5 |
| candidate_validation | 217 | 10.57 | 37.2 | 2293.6 |
| publish_queue | 217 | 10.69 | 37.4 | 2319.0 |
| append_dataset | 217 | 42.29 | 119.7 | 9178.0 |
| export | 217 | 0.35 | 1.9 | 75.5 |
| git_commit | 217 | 0.31 | 2.1 | 67.7 |
| push | 217 | 0.32 | 0.8 | 68.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6288 |
| Documents processed | 16218 |
| Process ratio | 257.9% (target ≥90.0%) |
| Rows published (traces) | 1014 |
| Sessions observed | 245 |
| Avg session duration (s) | 943.396 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.824 |
| Avg connector latency (ms) | 13907.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **257.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
