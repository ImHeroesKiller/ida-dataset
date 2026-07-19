# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T12:23:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 114 | 1.0 | 6.5 | 114.4 |
| source_discovery | 114 | 3.09 | 39.8 | 351.9 |
| connector | 114 | 80873.08 | 97806.1 | 9219531.0 |
| document_discovery | 114 | 80873.22 | 97806.2 | 9219546.9 |
| document_download | 114 | 266948.83 | 1509355.9 | 30432167.1 |
| extraction | 114 | 81.98 | 274.0 | 9345.7 |
| candidate_validation | 114 | 7.88 | 30.0 | 898.2 |
| publish_queue | 114 | 8.07 | 34.7 | 920.2 |
| append_dataset | 114 | 45.49 | 119.7 | 5186.2 |
| export | 114 | 0.34 | 0.7 | 38.5 |
| git_commit | 114 | 0.32 | 2.1 | 36.2 |
| push | 114 | 0.31 | 0.8 | 35.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3145 |
| Documents processed | 9796 |
| Process ratio | 311.5% (target ≥90.0%) |
| Rows published (traces) | 502 |
| Sessions observed | 142 |
| Avg session duration (s) | 852.711 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.682 |
| Avg connector latency (ms) | 13681.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **311.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
