# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T13:15:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 246 | 1.28 | 70.9 | 314.7 |
| source_discovery | 246 | 3.78 | 186.3 | 930.1 |
| connector | 246 | 87921.3 | 97806.1 | 21628639.8 |
| document_discovery | 246 | 87921.52 | 97806.2 | 21628693.9 |
| document_download | 246 | 241840.5 | 1509355.9 | 59492763.0 |
| extraction | 246 | 92.46 | 274.0 | 22744.5 |
| candidate_validation | 246 | 11.69 | 102.5 | 2875.4 |
| publish_queue | 246 | 11.78 | 102.7 | 2896.7 |
| append_dataset | 246 | 41.6 | 119.7 | 10233.2 |
| export | 246 | 0.35 | 2.1 | 86.8 |
| git_commit | 246 | 0.37 | 15.1 | 91.5 |
| push | 246 | 0.64 | 81.1 | 158.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7187 |
| Documents processed | 17844 |
| Process ratio | 248.3% (target ≥90.0%) |
| Rows published (traces) | 1159 |
| Sessions observed | 274 |
| Avg session duration (s) | 953.146 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.845 |
| Avg connector latency (ms) | 13751.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **248.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
