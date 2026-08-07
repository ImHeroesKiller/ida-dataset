# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T22:59:30+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 326 | 1.62 | 70.9 | 526.6 |
| source_discovery | 326 | 4.69 | 186.3 | 1528.8 |
| connector | 326 | 89413.53 | 97806.1 | 29148810.7 |
| document_discovery | 326 | 89413.73 | 97806.2 | 29148874.8 |
| document_download | 326 | 230940.74 | 1509355.9 | 75286682.6 |
| extraction | 326 | 96.14 | 274.0 | 31341.0 |
| candidate_validation | 326 | 13.7 | 136.9 | 4467.8 |
| publish_queue | 326 | 13.78 | 136.9 | 4491.3 |
| append_dataset | 326 | 39.58 | 119.7 | 12902.3 |
| export | 326 | 0.35 | 2.1 | 112.6 |
| git_commit | 326 | 0.35 | 15.1 | 115.7 |
| push | 326 | 0.66 | 81.1 | 213.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9646 |
| Documents processed | 22126 |
| Process ratio | 229.4% (target ≥90.0%) |
| Rows published (traces) | 1559 |
| Sessions observed | 301 |
| Avg session duration (s) | 1065.169 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.963 |
| Avg connector latency (ms) | 13684.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **229.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
