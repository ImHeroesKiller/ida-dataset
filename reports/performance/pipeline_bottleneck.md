# Pipeline Bottleneck Analysis

**Generated:** 2026-07-28T22:23:12+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 218 | 1.31 | 70.9 | 286.5 |
| source_discovery | 218 | 3.9 | 186.3 | 850.4 |
| connector | 218 | 87139.8 | 97806.1 | 18996476.4 |
| document_discovery | 218 | 87139.94 | 97806.2 | 18996508.0 |
| document_download | 218 | 249194.05 | 1509355.9 | 54324302.0 |
| extraction | 218 | 90.85 | 274.0 | 19805.6 |
| candidate_validation | 218 | 10.65 | 37.2 | 2321.8 |
| publish_queue | 218 | 10.77 | 37.4 | 2347.2 |
| append_dataset | 218 | 42.19 | 119.7 | 9198.2 |
| export | 218 | 0.35 | 1.9 | 76.0 |
| git_commit | 218 | 0.31 | 2.1 | 67.9 |
| push | 218 | 0.31 | 0.8 | 68.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6319 |
| Documents processed | 16280 |
| Process ratio | 257.6% (target ≥90.0%) |
| Rows published (traces) | 1019 |
| Sessions observed | 246 |
| Avg session duration (s) | 944.061 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.825 |
| Avg connector latency (ms) | 13845.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **257.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
