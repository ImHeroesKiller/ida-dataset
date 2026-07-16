# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T08:41:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 74 | 1.03 | 6.5 | 76.5 |
| source_discovery | 74 | 2.74 | 3.3 | 202.6 |
| connector | 74 | 73760.87 | 97806.1 | 5458304.4 |
| document_discovery | 74 | 73761.01 | 97806.2 | 5458314.7 |
| document_download | 74 | 273917.26 | 1509355.9 | 20269877.6 |
| extraction | 74 | 82.22 | 274.0 | 6084.0 |
| candidate_validation | 74 | 6.75 | 18.7 | 499.4 |
| publish_queue | 74 | 7.01 | 34.7 | 518.8 |
| append_dataset | 74 | 50.99 | 119.7 | 3772.9 |
| export | 74 | 0.34 | 0.6 | 24.9 |
| git_commit | 74 | 0.33 | 2.1 | 24.1 |
| push | 74 | 0.32 | 0.8 | 23.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1925 |
| Documents processed | 7371 |
| Process ratio | 382.9% (target ≥90.0%) |
| Rows published (traces) | 302 |
| Sessions observed | 102 |
| Avg session duration (s) | 761.265 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.493 |
| Avg connector latency (ms) | 13804.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **382.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
