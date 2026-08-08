# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T17:50:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 343 | 1.59 | 70.9 | 543.8 |
| source_discovery | 343 | 4.6 | 186.3 | 1577.4 |
| connector | 343 | 89640.67 | 97806.1 | 30746748.2 |
| document_discovery | 343 | 89640.86 | 97806.2 | 30746814.7 |
| document_download | 343 | 231598.1 | 1509355.9 | 79438149.9 |
| extraction | 343 | 96.72 | 274.0 | 33174.5 |
| candidate_validation | 343 | 14.03 | 136.9 | 4811.8 |
| publish_queue | 343 | 14.1 | 136.9 | 4835.4 |
| append_dataset | 343 | 39.28 | 119.7 | 13472.9 |
| export | 343 | 0.35 | 2.1 | 119.2 |
| git_commit | 343 | 0.35 | 15.1 | 121.6 |
| push | 343 | 0.64 | 81.1 | 218.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10153 |
| Documents processed | 23040 |
| Process ratio | 226.9% (target ≥90.0%) |
| Rows published (traces) | 1644 |
| Sessions observed | 303 |
| Avg session duration (s) | 1066.561 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.977 |
| Avg connector latency (ms) | 13834.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **226.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
