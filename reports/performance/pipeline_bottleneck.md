# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T09:43:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 126 | 1.0 | 6.5 | 126.5 |
| source_discovery | 126 | 3.07 | 39.8 | 386.6 |
| connector | 126 | 82119.0 | 97806.1 | 10346994.3 |
| document_discovery | 126 | 82119.14 | 97806.2 | 10347011.7 |
| document_download | 126 | 262092.16 | 1509355.9 | 33023611.6 |
| extraction | 126 | 82.88 | 274.0 | 10442.6 |
| candidate_validation | 126 | 8.18 | 30.0 | 1031.0 |
| publish_queue | 126 | 8.36 | 34.7 | 1053.2 |
| append_dataset | 126 | 44.86 | 119.7 | 5651.8 |
| export | 126 | 0.35 | 1.9 | 44.2 |
| git_commit | 126 | 0.32 | 2.1 | 40.2 |
| push | 126 | 0.31 | 0.8 | 39.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3507 |
| Documents processed | 10555 |
| Process ratio | 301.0% (target ≥90.0%) |
| Rows published (traces) | 562 |
| Sessions observed | 154 |
| Avg session duration (s) | 868.097 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.714 |
| Avg connector latency (ms) | 13691.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **301.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
