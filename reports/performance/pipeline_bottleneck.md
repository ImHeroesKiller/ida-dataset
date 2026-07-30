# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T16:45:41+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 237 | 1.29 | 70.9 | 305.7 |
| source_discovery | 237 | 3.82 | 186.3 | 904.5 |
| connector | 237 | 87689.84 | 97806.1 | 20782491.2 |
| document_discovery | 237 | 87689.99 | 97806.2 | 20782526.5 |
| document_download | 237 | 244618.49 | 1509355.9 | 57974583.0 |
| extraction | 237 | 92.11 | 274.0 | 21829.1 |
| candidate_validation | 237 | 11.11 | 37.2 | 2633.4 |
| publish_queue | 237 | 11.2 | 37.4 | 2654.3 |
| append_dataset | 237 | 41.86 | 119.7 | 9921.5 |
| export | 237 | 0.35 | 1.9 | 82.1 |
| git_commit | 237 | 0.31 | 2.1 | 74.1 |
| push | 237 | 0.31 | 0.8 | 74.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6908 |
| Documents processed | 17343 |
| Process ratio | 251.1% (target ≥90.0%) |
| Rows published (traces) | 1114 |
| Sessions observed | 265 |
| Avg session duration (s) | 950.528 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.839 |
| Avg connector latency (ms) | 13717.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **251.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
