# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T11:03:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 288 | 1.37 | 70.9 | 395.7 |
| source_discovery | 288 | 4.38 | 186.3 | 1260.8 |
| connector | 288 | 88810.36 | 97806.1 | 25577383.8 |
| document_discovery | 288 | 88810.57 | 97806.2 | 25577443.6 |
| document_download | 288 | 234755.32 | 1509355.9 | 67609533.3 |
| extraction | 288 | 93.95 | 274.0 | 27058.8 |
| candidate_validation | 288 | 12.6 | 102.5 | 3629.0 |
| publish_queue | 288 | 12.68 | 102.7 | 3651.6 |
| append_dataset | 288 | 40.44 | 119.7 | 11647.9 |
| export | 288 | 0.35 | 2.1 | 100.4 |
| git_commit | 288 | 0.36 | 15.1 | 104.4 |
| push | 288 | 0.7 | 81.1 | 202.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8478 |
| Documents processed | 20075 |
| Process ratio | 236.8% (target ≥90.0%) |
| Rows published (traces) | 1369 |
| Sessions observed | 316 |
| Avg session duration (s) | 959.323 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.868 |
| Avg connector latency (ms) | 14364.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **236.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
