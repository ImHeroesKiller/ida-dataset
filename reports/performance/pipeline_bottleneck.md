# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T10:48:13+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 44 | 1.1 | 6.5 | 48.4 |
| source_discovery | 44 | 2.71 | 3.3 | 119.1 |
| connector | 44 | 59965.8 | 97806.1 | 2638495.2 |
| document_discovery | 44 | 59965.94 | 97806.2 | 2638501.5 |
| document_download | 44 | 216140.7 | 1509355.9 | 9510190.9 |
| extraction | 44 | 67.83 | 109.5 | 2984.4 |
| candidate_validation | 44 | 5.58 | 8.7 | 245.6 |
| publish_queue | 44 | 5.64 | 8.8 | 248.2 |
| append_dataset | 44 | 44.62 | 119.7 | 1963.3 |
| export | 44 | 0.34 | 0.6 | 14.8 |
| git_commit | 44 | 0.34 | 2.1 | 14.9 |
| push | 44 | 0.33 | 0.8 | 14.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1015 |
| Documents processed | 3809 |
| Process ratio | 375.3% (target ≥90.0%) |
| Rows published (traces) | 156 |
| Sessions observed | 72 |
| Avg session duration (s) | 571.361 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.189 |
| Avg connector latency (ms) | 14002.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **375.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
