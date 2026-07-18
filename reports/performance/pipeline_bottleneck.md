# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T22:12:38+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 107 | 1.02 | 6.5 | 108.8 |
| source_discovery | 107 | 2.78 | 3.5 | 297.0 |
| connector | 107 | 80014.34 | 97806.1 | 8561534.2 |
| document_discovery | 107 | 80014.48 | 97806.2 | 8561549.3 |
| document_download | 107 | 269374.39 | 1509355.9 | 28823059.5 |
| extraction | 107 | 83.04 | 274.0 | 8885.1 |
| candidate_validation | 107 | 7.63 | 18.7 | 816.1 |
| publish_queue | 107 | 7.83 | 34.7 | 838.0 |
| append_dataset | 107 | 46.57 | 119.7 | 4982.8 |
| export | 107 | 0.34 | 0.7 | 36.3 |
| git_commit | 107 | 0.32 | 2.1 | 34.4 |
| push | 107 | 0.31 | 0.8 | 33.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2938 |
| Documents processed | 9395 |
| Process ratio | 319.8% (target ≥90.0%) |
| Rows published (traces) | 467 |
| Sessions observed | 135 |
| Avg session duration (s) | 841.741 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.66 |
| Avg connector latency (ms) | 13868.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **319.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
