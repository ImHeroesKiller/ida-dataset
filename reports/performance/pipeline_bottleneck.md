# Pipeline Bottleneck Analysis

**Generated:** 2026-08-03T16:46:38+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 280 | 1.38 | 70.9 | 387.7 |
| source_discovery | 280 | 4.15 | 186.3 | 1162.7 |
| connector | 280 | 88660.17 | 97806.1 | 24824847.3 |
| document_discovery | 280 | 88660.38 | 97806.2 | 24824906.1 |
| document_download | 280 | 235914.82 | 1509355.9 | 66056149.6 |
| extraction | 280 | 93.55 | 274.0 | 26194.1 |
| candidate_validation | 280 | 12.45 | 102.5 | 3485.3 |
| publish_queue | 280 | 12.53 | 102.7 | 3507.7 |
| append_dataset | 280 | 40.68 | 119.7 | 11389.3 |
| export | 280 | 0.35 | 2.1 | 97.8 |
| git_commit | 280 | 0.36 | 15.1 | 101.9 |
| push | 280 | 0.6 | 81.1 | 168.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8230 |
| Documents processed | 19694 |
| Process ratio | 239.3% (target ≥90.0%) |
| Rows published (traces) | 1329 |
| Sessions observed | 308 |
| Avg session duration (s) | 958.299 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.864 |
| Avg connector latency (ms) | 13753.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **239.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
