# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T13:41:28+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 32 | 1.15 | 6.5 | 36.7 |
| source_discovery | 32 | 2.66 | 3.3 | 85.2 |
| connector | 32 | 47212.92 | 97806.1 | 1510813.5 |
| document_discovery | 32 | 47213.07 | 97806.2 | 1510818.1 |
| document_download | 32 | 203356.18 | 1509355.9 | 6507397.7 |
| extraction | 32 | 58.24 | 109.5 | 1863.8 |
| candidate_validation | 32 | 4.96 | 8.7 | 158.7 |
| publish_queue | 32 | 5.03 | 8.8 | 161.1 |
| append_dataset | 32 | 37.14 | 119.7 | 1188.6 |
| export | 32 | 0.33 | 0.6 | 10.4 |
| git_commit | 32 | 0.3 | 0.4 | 9.5 |
| push | 32 | 0.31 | 0.5 | 9.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 663 |
| Documents processed | 2315 |
| Process ratio | 349.2% (target ≥90.0%) |
| Rows published (traces) | 100 |
| Sessions observed | 60 |
| Avg session duration (s) | 464.3 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.96 |
| Avg connector latency (ms) | 13745.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **349.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
