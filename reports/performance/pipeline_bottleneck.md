# Pipeline Bottleneck Analysis

**Generated:** 2026-08-06T14:33:08+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 309 | 1.52 | 70.9 | 469.4 |
| source_discovery | 309 | 4.27 | 186.3 | 1319.5 |
| connector | 309 | 89162.75 | 97806.1 | 27551288.5 |
| document_discovery | 309 | 89162.95 | 97806.2 | 27551350.7 |
| document_download | 309 | 234002.58 | 1509355.9 | 72306798.4 |
| extraction | 309 | 95.23 | 274.0 | 29427.3 |
| candidate_validation | 309 | 13.01 | 102.5 | 4021.2 |
| publish_queue | 309 | 13.09 | 102.7 | 4044.1 |
| append_dataset | 309 | 39.97 | 119.7 | 12351.5 |
| export | 309 | 0.35 | 2.1 | 107.1 |
| git_commit | 309 | 0.36 | 15.1 | 110.9 |
| push | 309 | 0.68 | 81.1 | 209.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9119 |
| Documents processed | 21192 |
| Process ratio | 232.4% (target ≥90.0%) |
| Rows published (traces) | 1474 |
| Sessions observed | 305 |
| Avg session duration (s) | 1058.003 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.929 |
| Avg connector latency (ms) | 13711.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **232.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
