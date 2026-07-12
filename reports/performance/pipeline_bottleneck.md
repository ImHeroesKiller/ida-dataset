# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T07:32:52+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 28 | 0.97 | 1.4 | 27.2 |
| source_discovery | 28 | 2.62 | 3.3 | 73.5 |
| connector | 28 | 43670.74 | 97806.1 | 1222780.8 |
| document_discovery | 28 | 43670.9 | 97806.2 | 1222785.1 |
| document_download | 28 | 203697.34 | 1509355.9 | 5703525.6 |
| extraction | 28 | 53.89 | 109.5 | 1509.0 |
| candidate_validation | 28 | 4.81 | 7.8 | 134.8 |
| publish_queue | 28 | 4.9 | 8.8 | 137.1 |
| append_dataset | 28 | 33.94 | 119.7 | 950.4 |
| export | 28 | 0.33 | 0.6 | 9.1 |
| git_commit | 28 | 0.3 | 0.4 | 8.4 |
| push | 28 | 0.31 | 0.5 | 8.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 549 |
| Documents processed | 1839 |
| Process ratio | 335.0% (target ≥90.0%) |
| Rows published (traces) | 85 |
| Sessions observed | 56 |
| Avg session duration (s) | 428.018 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.818 |
| Avg connector latency (ms) | 2482.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **335.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
