# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T10:52:14+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 336 | 1.6 | 70.9 | 536.8 |
| source_discovery | 336 | 4.64 | 186.3 | 1558.0 |
| connector | 336 | 89548.69 | 97806.1 | 30088358.6 |
| document_discovery | 336 | 89548.88 | 97806.2 | 30088424.2 |
| document_download | 336 | 232855.41 | 1509355.9 | 78239417.7 |
| extraction | 336 | 96.54 | 274.0 | 32436.9 |
| candidate_validation | 336 | 13.91 | 136.9 | 4673.3 |
| publish_queue | 336 | 13.98 | 136.9 | 4697.0 |
| append_dataset | 336 | 39.45 | 119.7 | 13255.2 |
| export | 336 | 0.34 | 2.1 | 115.7 |
| git_commit | 336 | 0.36 | 15.1 | 119.4 |
| push | 336 | 0.65 | 81.1 | 216.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9946 |
| Documents processed | 22683 |
| Process ratio | 228.1% (target ≥90.0%) |
| Rows published (traces) | 1609 |
| Sessions observed | 311 |
| Avg session duration (s) | 1067.505 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.964 |
| Avg connector latency (ms) | 13683.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **228.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
