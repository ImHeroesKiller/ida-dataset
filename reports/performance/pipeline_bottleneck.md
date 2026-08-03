# Pipeline Bottleneck Analysis

**Generated:** 2026-08-03T22:27:31+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 283 | 1.38 | 70.9 | 390.6 |
| source_discovery | 283 | 4.14 | 186.3 | 1171.3 |
| connector | 283 | 88715.97 | 97806.1 | 25106619.9 |
| document_discovery | 283 | 88716.18 | 97806.2 | 25106679.1 |
| document_download | 283 | 235633.4 | 1509355.9 | 66684251.1 |
| extraction | 283 | 93.69 | 274.0 | 26513.4 |
| candidate_validation | 283 | 12.51 | 102.5 | 3540.9 |
| publish_queue | 283 | 12.59 | 102.7 | 3563.6 |
| append_dataset | 283 | 40.63 | 119.7 | 11497.0 |
| export | 283 | 0.35 | 2.1 | 98.8 |
| git_commit | 283 | 0.36 | 15.1 | 102.8 |
| push | 283 | 0.6 | 81.1 | 169.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8323 |
| Documents processed | 19858 |
| Process ratio | 238.6% (target ≥90.0%) |
| Rows published (traces) | 1344 |
| Sessions observed | 311 |
| Avg session duration (s) | 959.318 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.866 |
| Avg connector latency (ms) | 13922.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **238.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
