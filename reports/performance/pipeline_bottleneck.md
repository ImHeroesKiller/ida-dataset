# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T04:32:23+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 166 | 0.99 | 6.5 | 164.1 |
| source_discovery | 166 | 3.11 | 39.8 | 516.0 |
| connector | 166 | 84985.81 | 97806.1 | 14107645.0 |
| document_discovery | 166 | 84985.96 | 97806.2 | 14107670.0 |
| document_download | 166 | 251654.97 | 1509355.9 | 41774725.3 |
| extraction | 166 | 86.94 | 274.0 | 14432.4 |
| candidate_validation | 166 | 9.25 | 30.0 | 1535.7 |
| publish_queue | 166 | 9.39 | 34.7 | 1559.4 |
| append_dataset | 166 | 43.66 | 119.7 | 7247.7 |
| export | 166 | 0.35 | 1.9 | 58.4 |
| git_commit | 166 | 0.31 | 2.1 | 52.2 |
| push | 166 | 0.32 | 0.8 | 52.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4727 |
| Documents processed | 13219 |
| Process ratio | 279.6% (target ≥90.0%) |
| Rows published (traces) | 762 |
| Sessions observed | 194 |
| Avg session duration (s) | 907.247 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.786 |
| Avg connector latency (ms) | 13808.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **279.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
