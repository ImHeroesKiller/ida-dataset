# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T04:21:34+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 372 | 1.54 | 70.9 | 571.2 |
| source_discovery | 372 | 4.46 | 186.3 | 1658.1 |
| connector | 372 | 89979.11 | 97806.1 | 33472227.9 |
| document_discovery | 372 | 89979.3 | 97806.2 | 33472298.9 |
| document_download | 372 | 236370.47 | 1509355.9 | 87929814.9 |
| extraction | 372 | 97.63 | 274.0 | 36317.9 |
| candidate_validation | 372 | 14.55 | 136.9 | 5410.8 |
| publish_queue | 372 | 14.61 | 136.9 | 5435.7 |
| append_dataset | 372 | 38.89 | 119.7 | 14466.0 |
| export | 372 | 0.35 | 2.1 | 129.2 |
| git_commit | 372 | 0.35 | 15.1 | 130.9 |
| push | 372 | 0.61 | 81.1 | 227.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11052 |
| Documents processed | 24706 |
| Process ratio | 223.5% (target ≥90.0%) |
| Rows published (traces) | 1789 |
| Sessions observed | 302 |
| Avg session duration (s) | 1058.831 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13701.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
