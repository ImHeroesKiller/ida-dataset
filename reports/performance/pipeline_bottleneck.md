# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T09:56:44+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 43 | 1.1 | 6.5 | 47.5 |
| source_discovery | 43 | 2.7 | 3.3 | 116.1 |
| connector | 43 | 59173.66 | 97806.1 | 2544467.4 |
| document_discovery | 43 | 59173.8 | 97806.2 | 2544473.6 |
| document_download | 43 | 216819.06 | 1509355.9 | 9323219.7 |
| extraction | 43 | 67.1 | 109.5 | 2885.4 |
| candidate_validation | 43 | 5.53 | 8.7 | 237.7 |
| publish_queue | 43 | 5.59 | 8.8 | 240.3 |
| append_dataset | 43 | 44.12 | 119.7 | 1897.3 |
| export | 43 | 0.34 | 0.6 | 14.5 |
| git_commit | 43 | 0.34 | 2.1 | 14.6 |
| push | 43 | 0.32 | 0.8 | 13.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 984 |
| Documents processed | 3688 |
| Process ratio | 374.8% (target ≥90.0%) |
| Rows published (traces) | 151 |
| Sessions observed | 71 |
| Avg session duration (s) | 564.789 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.167 |
| Avg connector latency (ms) | 13772.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **374.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
