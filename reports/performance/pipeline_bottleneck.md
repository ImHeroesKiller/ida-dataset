# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T15:13:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 102 | 1.02 | 6.5 | 103.8 |
| source_discovery | 102 | 2.77 | 3.5 | 282.3 |
| connector | 102 | 79325.44 | 97806.1 | 8091195.2 |
| document_discovery | 102 | 79325.59 | 97806.2 | 8091209.7 |
| document_download | 102 | 264201.95 | 1509355.9 | 26948598.7 |
| extraction | 102 | 83.51 | 274.0 | 8517.9 |
| candidate_validation | 102 | 7.48 | 18.7 | 762.9 |
| publish_queue | 102 | 7.69 | 34.7 | 784.8 |
| append_dataset | 102 | 46.8 | 119.7 | 4773.6 |
| export | 102 | 0.34 | 0.7 | 34.7 |
| git_commit | 102 | 0.32 | 2.1 | 32.8 |
| push | 102 | 0.31 | 0.8 | 32.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2783 |
| Documents processed | 9036 |
| Process ratio | 324.7% (target ≥90.0%) |
| Rows published (traces) | 442 |
| Sessions observed | 130 |
| Avg session duration (s) | 827.4 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.642 |
| Avg connector latency (ms) | 13700.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **324.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
