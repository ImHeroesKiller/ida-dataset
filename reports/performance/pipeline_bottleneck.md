# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T23:20:19+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 188 | 0.99 | 6.5 | 186.2 |
| source_discovery | 188 | 3.08 | 39.8 | 579.2 |
| connector | 188 | 86036.26 | 97806.1 | 16174816.3 |
| document_discovery | 188 | 86036.4 | 97806.2 | 16174844.0 |
| document_download | 188 | 254360.14 | 1509355.9 | 47819706.4 |
| extraction | 188 | 88.33 | 274.0 | 16606.9 |
| candidate_validation | 188 | 9.77 | 30.0 | 1837.5 |
| publish_queue | 188 | 9.9 | 34.7 | 1861.8 |
| append_dataset | 188 | 43.01 | 119.7 | 8085.9 |
| export | 188 | 0.35 | 1.9 | 66.0 |
| git_commit | 188 | 0.31 | 2.1 | 58.6 |
| push | 188 | 0.32 | 0.8 | 59.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5409 |
| Documents processed | 14528 |
| Process ratio | 268.6% (target ≥90.0%) |
| Rows published (traces) | 872 |
| Sessions observed | 216 |
| Avg session duration (s) | 928.481 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.812 |
| Avg connector latency (ms) | 13733.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **268.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
