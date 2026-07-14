# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T20:34:35+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 58 | 1.07 | 6.5 | 61.8 |
| source_discovery | 58 | 2.72 | 3.3 | 157.9 |
| connector | 58 | 68173.61 | 97806.1 | 3954069.1 |
| document_discovery | 58 | 68173.75 | 97806.2 | 3954077.4 |
| document_download | 58 | 244578.68 | 1509355.9 | 14185563.7 |
| extraction | 58 | 78.47 | 274.0 | 4551.3 |
| candidate_validation | 58 | 6.08 | 9.5 | 352.9 |
| publish_queue | 58 | 6.13 | 9.5 | 355.6 |
| append_dataset | 58 | 48.07 | 119.7 | 2788.1 |
| export | 58 | 0.34 | 0.6 | 19.7 |
| git_commit | 58 | 0.33 | 2.1 | 19.1 |
| push | 58 | 0.32 | 0.8 | 18.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1439 |
| Documents processed | 5466 |
| Process ratio | 379.8% (target ≥90.0%) |
| Rows published (traces) | 222 |
| Sessions observed | 86 |
| Avg session duration (s) | 671.221 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.333 |
| Avg connector latency (ms) | 13689.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **379.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
