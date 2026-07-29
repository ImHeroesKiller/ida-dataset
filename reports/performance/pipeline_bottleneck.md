# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T00:15:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 219 | 1.31 | 70.9 | 287.5 |
| source_discovery | 219 | 3.9 | 186.3 | 853.2 |
| connector | 219 | 87171.89 | 97806.1 | 19090645.0 |
| document_discovery | 219 | 87172.04 | 97806.2 | 19090676.8 |
| document_download | 219 | 248719.73 | 1509355.9 | 54469621.0 |
| extraction | 219 | 90.92 | 274.0 | 19911.3 |
| candidate_validation | 219 | 10.67 | 37.2 | 2337.5 |
| publish_queue | 219 | 10.79 | 37.4 | 2362.9 |
| append_dataset | 219 | 42.14 | 119.7 | 9229.3 |
| export | 219 | 0.35 | 1.9 | 76.3 |
| git_commit | 219 | 0.31 | 2.1 | 68.2 |
| push | 219 | 0.31 | 0.8 | 68.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6350 |
| Documents processed | 16322 |
| Process ratio | 257.0% (target ≥90.0%) |
| Rows published (traces) | 1024 |
| Sessions observed | 247 |
| Avg session duration (s) | 944.368 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.825 |
| Avg connector latency (ms) | 13798.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **257.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
