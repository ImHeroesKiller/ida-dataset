# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T08:56:14+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 136 | 1.0 | 6.5 | 136.2 |
| source_discovery | 136 | 3.17 | 39.8 | 430.6 |
| connector | 136 | 82990.78 | 97806.1 | 11286746.2 |
| document_discovery | 136 | 82990.92 | 97806.2 | 11286765.1 |
| document_download | 136 | 255998.27 | 1509355.9 | 34815764.7 |
| extraction | 136 | 84.69 | 274.0 | 11518.4 |
| candidate_validation | 136 | 8.42 | 30.0 | 1145.0 |
| publish_queue | 136 | 8.59 | 34.7 | 1167.7 |
| append_dataset | 136 | 44.41 | 119.7 | 6040.4 |
| export | 136 | 0.35 | 1.9 | 47.6 |
| git_commit | 136 | 0.32 | 2.1 | 43.1 |
| push | 136 | 0.31 | 0.8 | 42.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3807 |
| Documents processed | 11216 |
| Process ratio | 294.6% (target ≥90.0%) |
| Rows published (traces) | 612 |
| Sessions observed | 164 |
| Avg session duration (s) | 877.317 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.736 |
| Avg connector latency (ms) | 13776.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **294.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
