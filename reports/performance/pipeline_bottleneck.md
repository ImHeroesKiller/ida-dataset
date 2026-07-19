# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T14:04:35+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 115 | 1.0 | 6.5 | 115.3 |
| source_discovery | 115 | 3.09 | 39.8 | 354.9 |
| connector | 115 | 80986.73 | 97806.1 | 9313474.4 |
| document_discovery | 115 | 80986.87 | 97806.2 | 9313490.4 |
| document_download | 115 | 269320.83 | 1509355.9 | 30971894.9 |
| extraction | 115 | 81.94 | 274.0 | 9422.6 |
| candidate_validation | 115 | 7.9 | 30.0 | 909.0 |
| publish_queue | 115 | 8.1 | 34.7 | 931.0 |
| append_dataset | 115 | 45.43 | 119.7 | 5223.9 |
| export | 115 | 0.34 | 0.7 | 38.8 |
| git_commit | 115 | 0.32 | 2.1 | 36.5 |
| push | 115 | 0.31 | 0.8 | 36.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3176 |
| Documents processed | 9866 |
| Process ratio | 310.6% (target ≥90.0%) |
| Rows published (traces) | 507 |
| Sessions observed | 143 |
| Avg session duration (s) | 856.35 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.685 |
| Avg connector latency (ms) | 13759.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **310.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
