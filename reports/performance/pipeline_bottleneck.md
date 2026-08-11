# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T15:16:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 395 | 1.5 | 70.9 | 593.6 |
| source_discovery | 395 | 4.36 | 186.3 | 1723.0 |
| connector | 395 | 90212.79 | 97806.1 | 35634051.5 |
| document_discovery | 395 | 90212.98 | 97806.2 | 35634125.3 |
| document_download | 395 | 236433.34 | 1509355.9 | 93391168.5 |
| extraction | 395 | 98.72 | 274.0 | 38994.9 |
| candidate_validation | 395 | 15.35 | 149.0 | 6062.0 |
| publish_queue | 395 | 15.41 | 149.1 | 6087.8 |
| append_dataset | 395 | 38.69 | 119.7 | 15283.0 |
| export | 395 | 0.35 | 2.7 | 138.7 |
| git_commit | 395 | 0.35 | 15.1 | 138.3 |
| push | 395 | 0.59 | 81.1 | 234.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11745 |
| Documents processed | 26020 |
| Process ratio | 221.5% (target ≥90.0%) |
| Rows published (traces) | 1904 |
| Sessions observed | 313 |
| Avg session duration (s) | 1060.78 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 14166.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
