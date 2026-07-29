# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T09:55:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 223 | 1.31 | 70.9 | 291.3 |
| source_discovery | 223 | 3.88 | 186.3 | 864.3 |
| connector | 223 | 87293.02 | 97806.1 | 19466342.4 |
| document_discovery | 223 | 87293.16 | 97806.2 | 19466374.8 |
| document_download | 223 | 247329.29 | 1509355.9 | 55154431.8 |
| extraction | 223 | 91.12 | 274.0 | 20319.3 |
| candidate_validation | 223 | 10.78 | 37.2 | 2403.1 |
| publish_queue | 223 | 10.87 | 37.4 | 2423.6 |
| append_dataset | 223 | 41.97 | 119.7 | 9358.6 |
| export | 223 | 0.35 | 1.9 | 77.4 |
| git_commit | 223 | 0.31 | 2.1 | 69.5 |
| push | 223 | 0.31 | 0.8 | 70.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6474 |
| Documents processed | 16508 |
| Process ratio | 255.0% (target ≥90.0%) |
| Rows published (traces) | 1044 |
| Sessions observed | 251 |
| Avg session duration (s) | 945.554 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.829 |
| Avg connector latency (ms) | 15164.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **255.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
