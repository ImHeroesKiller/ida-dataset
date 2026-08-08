# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T02:01:32+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 328 | 1.61 | 70.9 | 528.9 |
| source_discovery | 328 | 4.68 | 186.3 | 1535.2 |
| connector | 328 | 89441.16 | 97806.1 | 29336700.4 |
| document_discovery | 328 | 89441.36 | 97806.2 | 29336764.8 |
| document_download | 328 | 231255.67 | 1509355.9 | 75851859.9 |
| extraction | 328 | 96.24 | 274.0 | 31567.5 |
| candidate_validation | 328 | 13.75 | 136.9 | 4509.7 |
| publish_queue | 328 | 13.82 | 136.9 | 4533.2 |
| append_dataset | 328 | 39.58 | 119.7 | 12980.7 |
| export | 328 | 0.35 | 2.1 | 113.2 |
| git_commit | 328 | 0.35 | 15.1 | 116.4 |
| push | 328 | 0.65 | 81.1 | 214.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9708 |
| Documents processed | 22250 |
| Process ratio | 229.2% (target ≥90.0%) |
| Rows published (traces) | 1569 |
| Sessions observed | 303 |
| Avg session duration (s) | 1065.528 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.963 |
| Avg connector latency (ms) | 13709.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **229.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
