# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T18:09:31+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 380 | 1.52 | 70.9 | 578.9 |
| source_discovery | 380 | 4.42 | 186.3 | 1680.2 |
| connector | 380 | 90064.22 | 97806.1 | 34224405.4 |
| document_discovery | 380 | 90064.41 | 97806.2 | 34224477.4 |
| document_download | 380 | 237288.58 | 1509355.9 | 90169660.8 |
| extraction | 380 | 98.12 | 274.0 | 37284.5 |
| candidate_validation | 380 | 15.05 | 149.0 | 5718.8 |
| publish_queue | 380 | 15.12 | 149.1 | 5743.9 |
| append_dataset | 380 | 38.79 | 119.7 | 14739.6 |
| export | 380 | 0.35 | 2.7 | 134.0 |
| git_commit | 380 | 0.35 | 15.1 | 133.5 |
| push | 380 | 0.61 | 81.1 | 229.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11290 |
| Documents processed | 25148 |
| Process ratio | 222.7% (target ≥90.0%) |
| Rows published (traces) | 1829 |
| Sessions observed | 310 |
| Avg session duration (s) | 1060.465 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13689.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
