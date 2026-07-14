# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T16:42:16+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 56 | 1.06 | 6.5 | 59.6 |
| source_discovery | 56 | 2.71 | 3.3 | 151.9 |
| connector | 56 | 67254.46 | 97806.1 | 3766249.7 |
| document_discovery | 56 | 67254.6 | 97806.2 | 3766257.7 |
| document_download | 56 | 235386.46 | 1509355.9 | 13181641.6 |
| extraction | 56 | 77.61 | 274.0 | 4346.1 |
| candidate_validation | 56 | 5.99 | 9.5 | 335.7 |
| publish_queue | 56 | 6.04 | 9.5 | 338.3 |
| append_dataset | 56 | 47.37 | 119.7 | 2652.7 |
| export | 56 | 0.34 | 0.6 | 19.0 |
| git_commit | 56 | 0.33 | 2.1 | 18.5 |
| push | 56 | 0.32 | 0.8 | 18.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1377 |
| Documents processed | 5210 |
| Process ratio | 378.4% (target ≥90.0%) |
| Rows published (traces) | 212 |
| Sessions observed | 84 |
| Avg session duration (s) | 654.774 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.306 |
| Avg connector latency (ms) | 13784.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **378.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
