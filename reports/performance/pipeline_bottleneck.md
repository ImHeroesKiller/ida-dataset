# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T11:21:34+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 100 | 1.02 | 6.5 | 102.0 |
| source_discovery | 100 | 2.77 | 3.5 | 276.5 |
| connector | 100 | 79030.11 | 97806.1 | 7903011.4 |
| document_discovery | 100 | 79030.26 | 97806.2 | 7903025.7 |
| document_download | 100 | 265792.72 | 1509355.9 | 26579272.4 |
| extraction | 100 | 83.26 | 274.0 | 8325.6 |
| candidate_validation | 100 | 7.43 | 18.7 | 742.9 |
| publish_queue | 100 | 7.65 | 34.7 | 764.6 |
| append_dataset | 100 | 46.96 | 119.7 | 4695.9 |
| export | 100 | 0.34 | 0.6 | 33.7 |
| git_commit | 100 | 0.32 | 2.1 | 32.2 |
| push | 100 | 0.31 | 0.8 | 31.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2721 |
| Documents processed | 8911 |
| Process ratio | 327.5% (target ≥90.0%) |
| Rows published (traces) | 432 |
| Sessions observed | 128 |
| Avg session duration (s) | 824.461 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.634 |
| Avg connector latency (ms) | 13702.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **327.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
