# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T09:21:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 30 | 0.97 | 1.4 | 29.1 |
| source_discovery | 30 | 2.63 | 3.3 | 79.0 |
| connector | 30 | 44096.87 | 97806.1 | 1322906.2 |
| document_discovery | 30 | 44097.02 | 97806.2 | 1322910.6 |
| document_download | 30 | 203042.03 | 1509355.9 | 6091261.0 |
| extraction | 30 | 55.49 | 109.5 | 1664.7 |
| candidate_validation | 30 | 4.77 | 7.8 | 143.0 |
| publish_queue | 30 | 4.84 | 8.8 | 145.3 |
| append_dataset | 30 | 35.21 | 119.7 | 1056.2 |
| export | 30 | 0.32 | 0.6 | 9.7 |
| git_commit | 30 | 0.3 | 0.4 | 8.9 |
| push | 30 | 0.31 | 0.5 | 9.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 601 |
| Documents processed | 2067 |
| Process ratio | 343.9% (target ≥90.0%) |
| Rows published (traces) | 90 |
| Sessions observed | 58 |
| Avg session duration (s) | 443.466 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.87 |
| Avg connector latency (ms) | 13665.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **343.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
