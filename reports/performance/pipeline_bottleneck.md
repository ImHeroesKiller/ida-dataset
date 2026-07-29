# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T17:35:27+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 226 | 1.3 | 70.9 | 294.2 |
| source_discovery | 226 | 3.86 | 186.3 | 872.6 |
| connector | 226 | 87384.22 | 97806.1 | 19748833.2 |
| document_discovery | 226 | 87384.36 | 97806.2 | 19748866.0 |
| document_download | 226 | 246383.25 | 1509355.9 | 55682615.5 |
| extraction | 226 | 91.37 | 274.0 | 20648.8 |
| candidate_validation | 226 | 10.85 | 37.2 | 2452.1 |
| publish_queue | 226 | 10.94 | 37.4 | 2472.8 |
| append_dataset | 226 | 41.93 | 119.7 | 9477.3 |
| export | 226 | 0.35 | 1.9 | 78.3 |
| git_commit | 226 | 0.31 | 2.1 | 70.4 |
| push | 226 | 0.31 | 0.8 | 70.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6567 |
| Documents processed | 16694 |
| Process ratio | 254.2% (target ≥90.0%) |
| Rows published (traces) | 1059 |
| Sessions observed | 254 |
| Avg session duration (s) | 946.346 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.831 |
| Avg connector latency (ms) | 13835.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **254.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
