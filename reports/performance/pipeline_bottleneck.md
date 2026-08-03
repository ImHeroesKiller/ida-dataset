# Pipeline Bottleneck Analysis

**Generated:** 2026-08-03T13:56:18+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 279 | 1.39 | 70.9 | 386.7 |
| source_discovery | 279 | 4.16 | 186.3 | 1159.7 |
| connector | 279 | 88641.75 | 97806.1 | 24731047.1 |
| document_discovery | 279 | 88641.96 | 97806.2 | 24731105.8 |
| document_download | 279 | 236287.72 | 1509355.9 | 65924272.6 |
| extraction | 279 | 93.51 | 274.0 | 26089.1 |
| candidate_validation | 279 | 12.42 | 102.5 | 3465.9 |
| publish_queue | 279 | 12.5 | 102.7 | 3488.3 |
| append_dataset | 279 | 40.73 | 119.7 | 11363.1 |
| export | 279 | 0.35 | 2.1 | 97.5 |
| git_commit | 279 | 0.36 | 15.1 | 101.6 |
| push | 279 | 0.6 | 81.1 | 168.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8199 |
| Documents processed | 19663 |
| Process ratio | 239.8% (target ≥90.0%) |
| Rows published (traces) | 1324 |
| Sessions observed | 307 |
| Avg session duration (s) | 958.847 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.864 |
| Avg connector latency (ms) | 13910.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **239.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
