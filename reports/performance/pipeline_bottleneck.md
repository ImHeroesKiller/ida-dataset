# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T08:01:48+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 286 | 1.38 | 70.9 | 393.9 |
| source_discovery | 286 | 4.13 | 186.3 | 1180.7 |
| connector | 286 | 88772.81 | 97806.1 | 25389024.1 |
| document_discovery | 286 | 88773.02 | 97806.2 | 25389083.7 |
| document_download | 286 | 234512.35 | 1509355.9 | 67070531.2 |
| extraction | 286 | 93.84 | 274.0 | 26837.5 |
| candidate_validation | 286 | 12.58 | 102.5 | 3597.1 |
| publish_queue | 286 | 12.66 | 102.7 | 3619.8 |
| append_dataset | 286 | 40.53 | 119.7 | 11590.3 |
| export | 286 | 0.35 | 2.1 | 99.7 |
| git_commit | 286 | 0.36 | 15.1 | 103.8 |
| push | 286 | 0.6 | 81.1 | 170.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8416 |
| Documents processed | 19982 |
| Process ratio | 237.4% (target ≥90.0%) |
| Rows published (traces) | 1359 |
| Sessions observed | 314 |
| Avg session duration (s) | 958.815 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.867 |
| Avg connector latency (ms) | 13939.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **237.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
