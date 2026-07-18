# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T05:45:46+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 97 | 1.02 | 6.5 | 99.1 |
| source_discovery | 97 | 2.76 | 3.5 | 268.1 |
| connector | 97 | 78570.91 | 97806.1 | 7621378.6 |
| document_discovery | 97 | 78571.06 | 97806.2 | 7621392.6 |
| document_download | 97 | 268569.03 | 1509355.9 | 26051196.1 |
| extraction | 97 | 83.36 | 274.0 | 8086.3 |
| candidate_validation | 97 | 7.34 | 18.7 | 712.4 |
| publish_queue | 97 | 7.56 | 34.7 | 733.8 |
| append_dataset | 97 | 47.34 | 119.7 | 4591.9 |
| export | 97 | 0.34 | 0.6 | 32.8 |
| git_commit | 97 | 0.32 | 2.1 | 31.0 |
| push | 97 | 0.31 | 0.8 | 30.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2628 |
| Documents processed | 8741 |
| Process ratio | 332.6% (target ≥90.0%) |
| Rows published (traces) | 417 |
| Sessions observed | 125 |
| Avg session duration (s) | 819.96 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.622 |
| Avg connector latency (ms) | 13830.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **332.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
