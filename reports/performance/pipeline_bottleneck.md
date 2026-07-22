# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T21:29:35+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 154 | 0.99 | 6.5 | 152.5 |
| source_discovery | 154 | 3.13 | 39.8 | 481.6 |
| connector | 154 | 84283.18 | 97806.1 | 12979609.5 |
| document_discovery | 154 | 84283.33 | 97806.2 | 12979633.1 |
| document_download | 154 | 252769.96 | 1509355.9 | 38926574.4 |
| extraction | 154 | 86.08 | 274.0 | 13256.7 |
| candidate_validation | 154 | 8.93 | 30.0 | 1375.6 |
| publish_queue | 154 | 9.09 | 34.7 | 1399.2 |
| append_dataset | 154 | 43.79 | 119.7 | 6743.4 |
| export | 154 | 0.35 | 1.9 | 54.2 |
| git_commit | 154 | 0.31 | 2.1 | 48.5 |
| push | 154 | 0.31 | 0.8 | 48.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4355 |
| Documents processed | 12400 |
| Process ratio | 284.7% (target ≥90.0%) |
| Rows published (traces) | 702 |
| Sessions observed | 182 |
| Avg session duration (s) | 896.165 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.769 |
| Avg connector latency (ms) | 13824.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **284.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
