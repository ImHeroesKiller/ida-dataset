# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T11:26:24+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 376 | 1.53 | 70.9 | 574.6 |
| source_discovery | 376 | 4.44 | 186.3 | 1668.5 |
| connector | 376 | 90022.2 | 97806.1 | 33848348.5 |
| document_discovery | 376 | 90022.39 | 97806.2 | 33848419.9 |
| document_download | 376 | 237670.2 | 1509355.9 | 89363994.8 |
| extraction | 376 | 97.94 | 274.0 | 36825.1 |
| candidate_validation | 376 | 14.97 | 149.0 | 5626.9 |
| publish_queue | 376 | 15.03 | 149.1 | 5652.0 |
| append_dataset | 376 | 38.79 | 119.7 | 14585.1 |
| export | 376 | 0.35 | 2.1 | 130.3 |
| git_commit | 376 | 0.35 | 15.1 | 131.9 |
| push | 376 | 0.61 | 81.1 | 228.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11166 |
| Documents processed | 24911 |
| Process ratio | 223.1% (target ≥90.0%) |
| Rows published (traces) | 1809 |
| Sessions observed | 306 |
| Avg session duration (s) | 1060.683 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13772.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
