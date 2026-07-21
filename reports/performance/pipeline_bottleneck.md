# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T06:47:40+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 135 | 1.0 | 6.5 | 135.2 |
| source_discovery | 135 | 3.17 | 39.8 | 427.6 |
| connector | 135 | 82909.66 | 97806.1 | 11192804.7 |
| document_discovery | 135 | 82909.8 | 97806.2 | 11192823.4 |
| document_download | 135 | 256397.53 | 1509355.9 | 34613667.0 |
| extraction | 135 | 84.59 | 274.0 | 11419.5 |
| candidate_validation | 135 | 8.39 | 30.0 | 1132.9 |
| publish_queue | 135 | 8.56 | 34.7 | 1155.5 |
| append_dataset | 135 | 44.49 | 119.7 | 6006.3 |
| export | 135 | 0.35 | 1.9 | 47.3 |
| git_commit | 135 | 0.32 | 2.1 | 42.8 |
| push | 135 | 0.31 | 0.8 | 42.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3776 |
| Documents processed | 11165 |
| Process ratio | 295.7% (target ≥90.0%) |
| Rows published (traces) | 607 |
| Sessions observed | 163 |
| Avg session duration (s) | 876.264 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.734 |
| Avg connector latency (ms) | 13850.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **295.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
