# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T15:16:01+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 33 | 1.14 | 6.5 | 37.7 |
| source_discovery | 33 | 2.67 | 3.3 | 88.1 |
| connector | 33 | 48626.66 | 97806.1 | 1604679.9 |
| document_discovery | 33 | 48626.81 | 97806.2 | 1604684.7 |
| document_download | 33 | 203153.56 | 1509355.9 | 6704067.5 |
| extraction | 33 | 59.38 | 109.5 | 1959.4 |
| candidate_validation | 33 | 5.03 | 8.7 | 166.0 |
| publish_queue | 33 | 5.1 | 8.8 | 168.4 |
| append_dataset | 33 | 37.86 | 119.7 | 1249.5 |
| export | 33 | 0.32 | 0.6 | 10.7 |
| git_commit | 33 | 0.3 | 0.4 | 9.8 |
| push | 33 | 0.32 | 0.6 | 10.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 694 |
| Documents processed | 2423 |
| Process ratio | 349.1% (target ≥90.0%) |
| Rows published (traces) | 105 |
| Sessions observed | 61 |
| Avg session duration (s) | 474.049 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.0 |
| Avg connector latency (ms) | 13702.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **349.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
