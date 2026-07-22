# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T00:19:48+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 145 | 1.0 | 6.5 | 144.4 |
| source_discovery | 145 | 3.14 | 39.8 | 455.8 |
| connector | 145 | 83676.59 | 97806.1 | 12133105.6 |
| document_discovery | 145 | 83676.74 | 97806.2 | 12133127.7 |
| document_download | 145 | 254742.62 | 1509355.9 | 36937679.7 |
| extraction | 145 | 85.4 | 274.0 | 12383.4 |
| candidate_validation | 145 | 8.7 | 30.0 | 1260.9 |
| publish_queue | 145 | 8.86 | 34.7 | 1284.3 |
| append_dataset | 145 | 43.93 | 119.7 | 6370.3 |
| export | 145 | 0.35 | 1.9 | 50.2 |
| git_commit | 145 | 0.32 | 2.1 | 45.7 |
| push | 145 | 0.31 | 0.8 | 45.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4086 |
| Documents processed | 11790 |
| Process ratio | 288.5% (target ≥90.0%) |
| Rows published (traces) | 657 |
| Sessions observed | 173 |
| Avg session duration (s) | 887.636 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.754 |
| Avg connector latency (ms) | 13696.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **288.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
