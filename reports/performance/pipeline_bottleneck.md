# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T06:53:27+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 27 | 0.97 | 1.4 | 26.1 |
| source_discovery | 27 | 2.62 | 3.3 | 70.7 |
| connector | 27 | 41810.66 | 97806.1 | 1128887.7 |
| document_discovery | 27 | 41810.81 | 97806.2 | 1128891.9 |
| document_download | 27 | 202234.22 | 1509355.9 | 5460323.9 |
| extraction | 27 | 52.29 | 109.5 | 1411.8 |
| candidate_validation | 27 | 4.72 | 7.8 | 127.5 |
| publish_queue | 27 | 4.81 | 8.8 | 129.8 |
| append_dataset | 27 | 32.31 | 119.7 | 872.3 |
| export | 27 | 0.32 | 0.6 | 8.7 |
| git_commit | 27 | 0.3 | 0.4 | 8.1 |
| push | 27 | 0.31 | 0.5 | 8.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 518 |
| Documents processed | 1691 |
| Process ratio | 326.4% (target ≥90.0%) |
| Rows published (traces) | 80 |
| Sessions observed | 55 |
| Avg session duration (s) | 415.873 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.762 |
| Avg connector latency (ms) | 13649.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **326.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
