# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T19:26:26+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 381 | 1.52 | 70.9 | 579.8 |
| source_discovery | 381 | 4.42 | 186.3 | 1683.1 |
| connector | 381 | 90073.91 | 97806.1 | 34318158.9 |
| document_discovery | 381 | 90074.1 | 97806.2 | 34318231.0 |
| document_download | 381 | 237021.83 | 1509355.9 | 90305318.8 |
| extraction | 381 | 98.17 | 274.0 | 37404.2 |
| candidate_validation | 381 | 15.07 | 149.0 | 5742.7 |
| publish_queue | 381 | 15.14 | 149.1 | 5767.8 |
| append_dataset | 381 | 38.79 | 119.7 | 14778.0 |
| export | 381 | 0.35 | 2.7 | 134.3 |
| git_commit | 381 | 0.35 | 15.1 | 133.8 |
| push | 381 | 0.6 | 81.1 | 230.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11321 |
| Documents processed | 25210 |
| Process ratio | 222.7% (target ≥90.0%) |
| Rows published (traces) | 1834 |
| Sessions observed | 311 |
| Avg session duration (s) | 1060.145 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13803.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
