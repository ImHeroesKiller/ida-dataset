# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T09:00:18+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 297 | 1.36 | 70.9 | 403.9 |
| source_discovery | 297 | 4.33 | 186.3 | 1285.4 |
| connector | 297 | 88965.73 | 97806.1 | 26422822.1 |
| document_discovery | 297 | 88965.94 | 97806.2 | 26422882.9 |
| document_download | 297 | 234890.5 | 1509355.9 | 69762479.4 |
| extraction | 297 | 94.34 | 274.0 | 28018.2 |
| candidate_validation | 297 | 12.76 | 102.5 | 3789.8 |
| publish_queue | 297 | 12.84 | 102.7 | 3812.2 |
| append_dataset | 297 | 40.24 | 119.7 | 11951.9 |
| export | 297 | 0.35 | 2.1 | 103.2 |
| git_commit | 297 | 0.36 | 15.1 | 107.2 |
| push | 297 | 0.69 | 81.1 | 205.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8757 |
| Documents processed | 20592 |
| Process ratio | 235.1% (target ≥90.0%) |
| Rows published (traces) | 1414 |
| Sessions observed | 325 |
| Avg session duration (s) | 962.742 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.872 |
| Avg connector latency (ms) | 13749.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **235.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
