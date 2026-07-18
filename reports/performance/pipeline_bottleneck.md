# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T23:09:28+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 108 | 1.02 | 6.5 | 109.9 |
| source_discovery | 108 | 2.78 | 3.5 | 299.8 |
| connector | 108 | 80142.4 | 97806.1 | 8655379.1 |
| document_discovery | 108 | 80142.54 | 97806.2 | 8655394.4 |
| document_download | 108 | 270012.01 | 1509355.9 | 29161297.2 |
| extraction | 108 | 82.99 | 274.0 | 8962.4 |
| candidate_validation | 108 | 7.66 | 18.7 | 826.9 |
| publish_queue | 108 | 7.86 | 34.7 | 848.8 |
| append_dataset | 108 | 46.42 | 119.7 | 5013.1 |
| export | 108 | 0.34 | 0.7 | 36.6 |
| git_commit | 108 | 0.32 | 2.1 | 34.7 |
| push | 108 | 0.31 | 0.8 | 33.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2969 |
| Documents processed | 9443 |
| Process ratio | 318.1% (target ≥90.0%) |
| Rows published (traces) | 472 |
| Sessions observed | 136 |
| Avg session duration (s) | 844.125 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.663 |
| Avg connector latency (ms) | 14168.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **318.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
