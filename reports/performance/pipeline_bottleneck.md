# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T00:15:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 25 | 0.94 | 1.3 | 23.6 |
| source_discovery | 25 | 2.6 | 3.3 | 65.0 |
| connector | 25 | 37628.44 | 97806.1 | 940710.9 |
| document_discovery | 25 | 37628.59 | 97806.2 | 940714.8 |
| document_download | 25 | 202395.02 | 1509355.9 | 5059875.4 |
| extraction | 25 | 48.51 | 109.5 | 1212.7 |
| candidate_validation | 25 | 4.52 | 7.8 | 113.1 |
| publish_queue | 25 | 4.62 | 8.8 | 115.5 |
| append_dataset | 25 | 28.6 | 119.7 | 715.0 |
| export | 25 | 0.32 | 0.6 | 8.0 |
| git_commit | 25 | 0.3 | 0.4 | 7.4 |
| push | 25 | 0.3 | 0.5 | 7.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 456 |
| Documents processed | 1401 |
| Process ratio | 307.2% (target ≥90.0%) |
| Rows published (traces) | 70 |
| Sessions observed | 53 |
| Avg session duration (s) | 391.208 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.632 |
| Avg connector latency (ms) | 13740.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **307.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
