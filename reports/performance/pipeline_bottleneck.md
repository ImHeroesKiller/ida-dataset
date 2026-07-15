# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T16:45:26+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 67 | 1.05 | 6.5 | 70.1 |
| source_discovery | 67 | 2.73 | 3.3 | 182.9 |
| connector | 67 | 71644.12 | 97806.1 | 4800156.2 |
| document_discovery | 67 | 71644.26 | 97806.2 | 4800165.6 |
| document_download | 67 | 266972.64 | 1509355.9 | 17887166.8 |
| extraction | 67 | 80.82 | 274.0 | 5415.0 |
| candidate_validation | 67 | 6.37 | 9.5 | 427.1 |
| publish_queue | 67 | 6.42 | 9.5 | 430.1 |
| append_dataset | 67 | 49.93 | 119.7 | 3345.2 |
| export | 67 | 0.34 | 0.6 | 22.6 |
| git_commit | 67 | 0.33 | 2.1 | 21.9 |
| push | 67 | 0.32 | 0.8 | 21.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1708 |
| Documents processed | 6555 |
| Process ratio | 383.8% (target ≥90.0%) |
| Rows published (traces) | 267 |
| Sessions observed | 95 |
| Avg session duration (s) | 728.832 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.433 |
| Avg connector latency (ms) | 13752.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **383.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
