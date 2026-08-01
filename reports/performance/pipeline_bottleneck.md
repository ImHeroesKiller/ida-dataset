# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T14:44:44+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 257 | 1.26 | 70.9 | 324.6 |
| source_discovery | 257 | 3.74 | 186.3 | 961.2 |
| connector | 257 | 88180.29 | 97806.1 | 22662334.1 |
| document_discovery | 257 | 88180.5 | 97806.2 | 22662389.5 |
| document_download | 257 | 239854.97 | 1509355.9 | 61642726.7 |
| extraction | 257 | 92.76 | 274.0 | 23838.9 |
| candidate_validation | 257 | 11.98 | 102.5 | 3078.3 |
| publish_queue | 257 | 12.06 | 102.7 | 3100.2 |
| append_dataset | 257 | 41.25 | 119.7 | 10600.9 |
| export | 257 | 0.35 | 2.1 | 90.4 |
| git_commit | 257 | 0.37 | 15.1 | 94.8 |
| push | 257 | 0.63 | 81.1 | 161.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7517 |
| Documents processed | 18455 |
| Process ratio | 245.5% (target ≥90.0%) |
| Rows published (traces) | 1214 |
| Sessions observed | 285 |
| Avg session duration (s) | 954.505 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.852 |
| Avg connector latency (ms) | 13758.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **245.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
