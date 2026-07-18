# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T16:20:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 103 | 1.02 | 6.5 | 104.8 |
| source_discovery | 103 | 2.77 | 3.5 | 285.5 |
| connector | 103 | 79467.98 | 97806.1 | 8185201.6 |
| document_discovery | 103 | 79468.12 | 97806.2 | 8185216.2 |
| document_download | 103 | 263626.54 | 1509355.9 | 27153534.1 |
| extraction | 103 | 83.57 | 274.0 | 8607.4 |
| candidate_validation | 103 | 7.51 | 18.7 | 773.5 |
| publish_queue | 103 | 7.72 | 34.7 | 795.4 |
| append_dataset | 103 | 46.75 | 119.7 | 4815.4 |
| export | 103 | 0.34 | 0.7 | 35.0 |
| git_commit | 103 | 0.32 | 2.1 | 33.1 |
| push | 103 | 0.31 | 0.8 | 32.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2814 |
| Documents processed | 9110 |
| Process ratio | 323.7% (target ≥90.0%) |
| Rows published (traces) | 447 |
| Sessions observed | 131 |
| Avg session duration (s) | 829.145 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.646 |
| Avg connector latency (ms) | 13749.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **323.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
