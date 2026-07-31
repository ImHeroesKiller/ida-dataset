# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T15:41:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 247 | 1.28 | 70.9 | 315.6 |
| source_discovery | 247 | 3.78 | 186.3 | 933.0 |
| connector | 247 | 87946.0 | 97806.1 | 21722661.6 |
| document_discovery | 247 | 87946.22 | 97806.2 | 21722715.8 |
| document_download | 247 | 241470.55 | 1509355.9 | 59643225.2 |
| extraction | 247 | 92.51 | 274.0 | 22849.9 |
| candidate_validation | 247 | 11.71 | 102.5 | 2892.4 |
| publish_queue | 247 | 11.8 | 102.7 | 2913.7 |
| append_dataset | 247 | 41.59 | 119.7 | 10271.9 |
| export | 247 | 0.35 | 2.1 | 87.1 |
| git_commit | 247 | 0.37 | 15.1 | 91.8 |
| push | 247 | 0.64 | 81.1 | 158.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7218 |
| Documents processed | 17906 |
| Process ratio | 248.1% (target ≥90.0%) |
| Rows published (traces) | 1164 |
| Sessions observed | 275 |
| Avg session duration (s) | 953.444 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.846 |
| Avg connector latency (ms) | 13835.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **248.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
