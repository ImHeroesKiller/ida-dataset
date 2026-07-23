# Pipeline Bottleneck Analysis

**Generated:** 2026-07-23T20:35:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 163 | 0.99 | 6.5 | 161.1 |
| source_discovery | 163 | 3.11 | 39.8 | 507.4 |
| connector | 163 | 84817.65 | 97806.1 | 13825276.3 |
| document_discovery | 163 | 84817.8 | 97806.2 | 13825301.0 |
| document_download | 163 | 252017.63 | 1509355.9 | 41078874.3 |
| extraction | 163 | 86.8 | 274.0 | 14148.4 |
| candidate_validation | 163 | 9.18 | 30.0 | 1495.6 |
| publish_queue | 163 | 9.32 | 34.7 | 1519.3 |
| append_dataset | 163 | 43.76 | 119.7 | 7132.6 |
| export | 163 | 0.35 | 1.9 | 57.4 |
| git_commit | 163 | 0.31 | 2.1 | 51.2 |
| push | 163 | 0.31 | 0.8 | 51.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4634 |
| Documents processed | 13043 |
| Process ratio | 281.5% (target ≥90.0%) |
| Rows published (traces) | 747 |
| Sessions observed | 191 |
| Avg session duration (s) | 904.759 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.782 |
| Avg connector latency (ms) | 13650.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **281.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
