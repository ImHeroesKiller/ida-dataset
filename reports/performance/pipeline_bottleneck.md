# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T21:57:08+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 325 | 1.62 | 70.9 | 525.4 |
| source_discovery | 325 | 4.69 | 186.3 | 1525.5 |
| connector | 325 | 89400.09 | 97806.1 | 29055028.6 |
| document_discovery | 325 | 89400.28 | 97806.2 | 29055092.5 |
| document_download | 325 | 231257.75 | 1509355.9 | 75158768.5 |
| extraction | 325 | 96.08 | 274.0 | 31227.2 |
| candidate_validation | 325 | 13.68 | 136.9 | 4446.7 |
| publish_queue | 325 | 13.75 | 136.9 | 4470.1 |
| append_dataset | 325 | 39.57 | 119.7 | 12861.3 |
| export | 325 | 0.35 | 2.1 | 112.3 |
| git_commit | 325 | 0.36 | 15.1 | 115.4 |
| push | 325 | 0.66 | 81.1 | 213.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9615 |
| Documents processed | 22064 |
| Process ratio | 229.5% (target ≥90.0%) |
| Rows published (traces) | 1554 |
| Sessions observed | 321 |
| Avg session duration (s) | 1055.798 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.933 |
| Avg connector latency (ms) | 13716.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **229.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
