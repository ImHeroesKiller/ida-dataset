# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T17:29:44+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 104 | 1.02 | 6.5 | 105.7 |
| source_discovery | 104 | 2.77 | 3.5 | 288.3 |
| connector | 104 | 79607.77 | 97806.1 | 8279207.7 |
| document_discovery | 104 | 79607.91 | 97806.2 | 8279222.4 |
| document_download | 104 | 264886.5 | 1509355.9 | 27548196.2 |
| extraction | 104 | 83.44 | 274.0 | 8677.7 |
| candidate_validation | 104 | 7.54 | 18.7 | 784.0 |
| publish_queue | 104 | 7.75 | 34.7 | 805.9 |
| append_dataset | 104 | 46.67 | 119.7 | 4854.1 |
| export | 104 | 0.34 | 0.7 | 35.3 |
| git_commit | 104 | 0.32 | 2.1 | 33.4 |
| push | 104 | 0.31 | 0.8 | 32.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2845 |
| Documents processed | 9182 |
| Process ratio | 322.7% (target ≥90.0%) |
| Rows published (traces) | 452 |
| Sessions observed | 132 |
| Avg session duration (s) | 832.205 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.649 |
| Avg connector latency (ms) | 13739.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **322.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
