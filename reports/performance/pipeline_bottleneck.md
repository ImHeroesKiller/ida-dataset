# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T03:52:26+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 72 | 1.04 | 6.5 | 74.6 |
| source_discovery | 72 | 2.74 | 3.3 | 197.0 |
| connector | 72 | 73194.07 | 97806.1 | 5269973.4 |
| document_discovery | 72 | 73194.21 | 97806.2 | 5269983.4 |
| document_download | 72 | 272373.49 | 1509355.9 | 19610891.3 |
| extraction | 72 | 81.93 | 274.0 | 5898.9 |
| candidate_validation | 72 | 6.68 | 18.7 | 481.1 |
| publish_queue | 72 | 6.95 | 34.7 | 500.3 |
| append_dataset | 72 | 50.65 | 119.7 | 3646.6 |
| export | 72 | 0.34 | 0.6 | 24.3 |
| git_commit | 72 | 0.32 | 2.1 | 23.3 |
| push | 72 | 0.32 | 0.8 | 22.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1863 |
| Documents processed | 7155 |
| Process ratio | 384.1% (target ≥90.0%) |
| Rows published (traces) | 292 |
| Sessions observed | 100 |
| Avg session duration (s) | 753.01 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.477 |
| Avg connector latency (ms) | 13733.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **384.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
