# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T08:54:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 148 | 0.99 | 6.5 | 147.1 |
| source_discovery | 148 | 3.14 | 39.8 | 464.5 |
| connector | 148 | 83884.41 | 97806.1 | 12414893.1 |
| document_discovery | 148 | 83884.57 | 97806.2 | 12414915.7 |
| document_download | 148 | 253628.16 | 1509355.9 | 37536967.8 |
| extraction | 148 | 85.67 | 274.0 | 12679.5 |
| candidate_validation | 148 | 8.77 | 30.0 | 1298.1 |
| publish_queue | 148 | 8.93 | 34.7 | 1321.5 |
| append_dataset | 148 | 43.93 | 119.7 | 6501.4 |
| export | 148 | 0.35 | 1.9 | 51.3 |
| git_commit | 148 | 0.31 | 2.1 | 46.6 |
| push | 148 | 0.31 | 0.8 | 46.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4179 |
| Documents processed | 12012 |
| Process ratio | 287.4% (target ≥90.0%) |
| Rows published (traces) | 672 |
| Sessions observed | 176 |
| Avg session duration (s) | 890.324 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.759 |
| Avg connector latency (ms) | 14671.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **287.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
