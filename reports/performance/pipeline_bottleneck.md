# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T08:37:28+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 86 | 1.03 | 6.5 | 88.6 |
| source_discovery | 86 | 2.75 | 3.3 | 236.6 |
| connector | 86 | 76588.87 | 97806.1 | 6586642.4 |
| document_discovery | 86 | 76589.02 | 97806.2 | 6586655.3 |
| document_download | 86 | 264049.04 | 1509355.9 | 22708217.4 |
| extraction | 86 | 82.9 | 274.0 | 7129.1 |
| candidate_validation | 86 | 7.05 | 18.7 | 606.0 |
| publish_queue | 86 | 7.27 | 34.7 | 625.6 |
| append_dataset | 86 | 48.58 | 119.7 | 4178.3 |
| export | 86 | 0.33 | 0.6 | 28.8 |
| git_commit | 86 | 0.32 | 2.1 | 27.7 |
| push | 86 | 0.32 | 0.8 | 27.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2297 |
| Documents processed | 8031 |
| Process ratio | 349.6% (target ≥90.0%) |
| Rows published (traces) | 362 |
| Sessions observed | 114 |
| Avg session duration (s) | 789.298 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.57 |
| Avg connector latency (ms) | 13792.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **349.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
