# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T07:06:02+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 125 | 1.0 | 6.5 | 125.5 |
| source_discovery | 125 | 3.07 | 39.8 | 383.8 |
| connector | 125 | 82025.67 | 97806.1 | 10253209.3 |
| document_discovery | 125 | 82025.81 | 97806.2 | 10253226.5 |
| document_download | 125 | 262694.87 | 1509355.9 | 32836858.3 |
| extraction | 125 | 82.76 | 274.0 | 10345.2 |
| candidate_validation | 125 | 8.15 | 30.0 | 1019.2 |
| publish_queue | 125 | 8.33 | 34.7 | 1041.4 |
| append_dataset | 125 | 44.85 | 119.7 | 5606.6 |
| export | 125 | 0.35 | 1.9 | 43.9 |
| git_commit | 125 | 0.32 | 2.1 | 39.9 |
| push | 125 | 0.31 | 0.8 | 39.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3476 |
| Documents processed | 10481 |
| Process ratio | 301.5% (target ≥90.0%) |
| Rows published (traces) | 557 |
| Sessions observed | 153 |
| Avg session duration (s) | 867.118 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.712 |
| Avg connector latency (ms) | 13713.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **301.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
