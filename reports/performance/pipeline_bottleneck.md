# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T04:15:32+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 231 | 1.3 | 70.9 | 299.3 |
| source_discovery | 231 | 3.84 | 186.3 | 887.0 |
| connector | 231 | 87526.42 | 97806.1 | 20218602.5 |
| document_discovery | 231 | 87526.57 | 97806.2 | 20218637.0 |
| document_download | 231 | 244711.22 | 1509355.9 | 56528290.8 |
| extraction | 231 | 91.72 | 274.0 | 21186.8 |
| candidate_validation | 231 | 10.97 | 37.2 | 2533.3 |
| publish_queue | 231 | 11.06 | 37.4 | 2554.0 |
| append_dataset | 231 | 41.87 | 119.7 | 9671.3 |
| export | 231 | 0.35 | 1.9 | 79.8 |
| git_commit | 231 | 0.31 | 2.1 | 72.0 |
| push | 231 | 0.31 | 0.8 | 72.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6722 |
| Documents processed | 16993 |
| Process ratio | 252.8% (target ≥90.0%) |
| Rows published (traces) | 1084 |
| Sessions observed | 259 |
| Avg session duration (s) | 947.514 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.835 |
| Avg connector latency (ms) | 13867.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **252.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
