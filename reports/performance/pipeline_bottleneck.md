# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T19:16:04+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 322 | 1.62 | 70.9 | 522.7 |
| source_discovery | 322 | 4.71 | 186.3 | 1517.2 |
| connector | 322 | 89356.65 | 97806.1 | 28772842.7 |
| document_discovery | 322 | 89356.85 | 97806.2 | 28772906.3 |
| document_download | 322 | 232234.86 | 1509355.9 | 74779625.2 |
| extraction | 322 | 95.92 | 274.0 | 30885.3 |
| candidate_validation | 322 | 13.62 | 136.9 | 4386.5 |
| publish_queue | 322 | 13.69 | 136.9 | 4409.6 |
| append_dataset | 322 | 39.63 | 119.7 | 12759.6 |
| export | 322 | 0.34 | 2.1 | 111.0 |
| git_commit | 322 | 0.36 | 15.1 | 114.4 |
| push | 322 | 0.66 | 81.1 | 212.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9522 |
| Documents processed | 21889 |
| Process ratio | 229.9% (target ≥90.0%) |
| Rows published (traces) | 1539 |
| Sessions observed | 318 |
| Avg session duration (s) | 1056.903 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.932 |
| Avg connector latency (ms) | 13671.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **229.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
