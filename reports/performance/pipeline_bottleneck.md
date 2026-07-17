# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T12:13:47+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 88 | 1.03 | 6.5 | 90.6 |
| source_discovery | 88 | 2.75 | 3.3 | 242.2 |
| connector | 88 | 76984.59 | 97806.1 | 6774643.6 |
| document_discovery | 88 | 76984.74 | 97806.2 | 6774656.8 |
| document_download | 88 | 262249.88 | 1509355.9 | 23077989.1 |
| extraction | 88 | 82.96 | 274.0 | 7300.3 |
| candidate_validation | 88 | 7.11 | 18.7 | 626.0 |
| publish_queue | 88 | 7.34 | 34.7 | 645.7 |
| append_dataset | 88 | 48.26 | 119.7 | 4247.1 |
| export | 88 | 0.34 | 0.6 | 29.6 |
| git_commit | 88 | 0.32 | 2.1 | 28.3 |
| push | 88 | 0.32 | 0.8 | 27.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2359 |
| Documents processed | 8135 |
| Process ratio | 344.8% (target ≥90.0%) |
| Rows published (traces) | 372 |
| Sessions observed | 116 |
| Avg session duration (s) | 793.448 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.58 |
| Avg connector latency (ms) | 13669.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **344.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
