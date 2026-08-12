# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T12:05:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 409 | 1.49 | 70.9 | 608.5 |
| source_discovery | 409 | 4.32 | 186.3 | 1765.0 |
| connector | 409 | 90344.54 | 97806.1 | 36950918.1 |
| document_discovery | 409 | 90344.73 | 97806.2 | 36950993.7 |
| document_download | 409 | 236542.68 | 1509355.9 | 96745956.1 |
| extraction | 409 | 99.33 | 274.0 | 40626.3 |
| candidate_validation | 409 | 15.67 | 149.0 | 6409.2 |
| publish_queue | 409 | 15.73 | 149.1 | 6435.6 |
| append_dataset | 409 | 38.67 | 119.7 | 15815.6 |
| export | 409 | 0.35 | 2.7 | 143.4 |
| git_commit | 409 | 0.35 | 15.1 | 143.0 |
| push | 409 | 0.58 | 81.1 | 238.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12169 |
| Documents processed | 26834 |
| Process ratio | 220.5% (target ≥90.0%) |
| Rows published (traces) | 1974 |
| Sessions observed | 314 |
| Avg session duration (s) | 1059.178 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 14169.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
