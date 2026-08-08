# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T14:51:44+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 340 | 1.59 | 70.9 | 540.7 |
| source_discovery | 340 | 4.61 | 186.3 | 1568.9 |
| connector | 340 | 89601.41 | 97806.1 | 30464480.5 |
| document_discovery | 340 | 89601.61 | 97806.2 | 30464546.5 |
| document_download | 340 | 231550.57 | 1509355.9 | 78727192.6 |
| extraction | 340 | 96.66 | 274.0 | 32864.8 |
| candidate_validation | 340 | 13.98 | 136.9 | 4754.1 |
| publish_queue | 340 | 14.05 | 136.9 | 4777.9 |
| append_dataset | 340 | 39.4 | 119.7 | 13397.0 |
| export | 340 | 0.35 | 2.1 | 118.1 |
| git_commit | 340 | 0.36 | 15.1 | 120.8 |
| push | 340 | 0.64 | 81.1 | 218.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10070 |
| Documents processed | 22915 |
| Process ratio | 227.6% (target ≥90.0%) |
| Rows published (traces) | 1629 |
| Sessions observed | 315 |
| Avg session duration (s) | 1066.616 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.965 |
| Avg connector latency (ms) | 13793.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **227.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
