# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T07:41:43+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 178 | 0.99 | 6.5 | 176.0 |
| source_discovery | 178 | 3.09 | 39.8 | 550.3 |
| connector | 178 | 85592.26 | 97806.1 | 15235423.0 |
| document_discovery | 178 | 85592.41 | 97806.2 | 15235449.6 |
| document_download | 178 | 253333.3 | 1509355.9 | 45093327.8 |
| extraction | 178 | 87.51 | 274.0 | 15577.4 |
| candidate_validation | 178 | 9.53 | 30.0 | 1695.5 |
| publish_queue | 178 | 9.66 | 34.7 | 1719.5 |
| append_dataset | 178 | 43.2 | 119.7 | 7690.2 |
| export | 178 | 0.35 | 1.9 | 62.5 |
| git_commit | 178 | 0.31 | 2.1 | 55.6 |
| push | 178 | 0.31 | 0.8 | 56.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5099 |
| Documents processed | 13919 |
| Process ratio | 273.0% (target ≥90.0%) |
| Rows published (traces) | 822 |
| Sessions observed | 206 |
| Avg session duration (s) | 919.442 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.801 |
| Avg connector latency (ms) | 15105.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **273.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
