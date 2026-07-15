# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T18:29:58+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 68 | 1.05 | 6.5 | 71.1 |
| source_discovery | 68 | 2.73 | 3.3 | 185.9 |
| connector | 68 | 71969.58 | 97806.1 | 4893931.5 |
| document_discovery | 68 | 71969.72 | 97806.2 | 4893941.1 |
| document_download | 68 | 268511.25 | 1509355.9 | 18258765.1 |
| extraction | 68 | 81.15 | 274.0 | 5518.2 |
| candidate_validation | 68 | 6.41 | 9.5 | 435.7 |
| publish_queue | 68 | 6.45 | 9.5 | 438.7 |
| append_dataset | 68 | 50.13 | 119.7 | 3409.1 |
| export | 68 | 0.34 | 0.6 | 22.9 |
| git_commit | 68 | 0.33 | 2.1 | 22.2 |
| push | 68 | 0.32 | 0.8 | 21.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1739 |
| Documents processed | 6680 |
| Process ratio | 384.1% (target ≥90.0%) |
| Rows published (traces) | 272 |
| Sessions observed | 96 |
| Avg session duration (s) | 734.208 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.443 |
| Avg connector latency (ms) | 13791.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **384.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
