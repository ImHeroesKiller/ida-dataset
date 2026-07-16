# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T23:14:44+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 82 | 1.03 | 6.5 | 84.3 |
| source_discovery | 82 | 2.75 | 3.3 | 225.1 |
| connector | 82 | 75738.64 | 97806.1 | 6210568.4 |
| document_discovery | 82 | 75738.79 | 97806.2 | 6210580.8 |
| document_download | 82 | 266019.36 | 1509355.9 | 21813587.6 |
| extraction | 82 | 82.73 | 274.0 | 6784.2 |
| candidate_validation | 82 | 6.95 | 18.7 | 569.9 |
| publish_queue | 82 | 7.19 | 34.7 | 589.6 |
| append_dataset | 82 | 49.33 | 119.7 | 4044.8 |
| export | 82 | 0.34 | 0.6 | 27.5 |
| git_commit | 82 | 0.32 | 2.1 | 26.5 |
| push | 82 | 0.32 | 0.8 | 26.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2173 |
| Documents processed | 7805 |
| Process ratio | 359.2% (target ≥90.0%) |
| Rows published (traces) | 342 |
| Sessions observed | 110 |
| Avg session duration (s) | 779.1 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.547 |
| Avg connector latency (ms) | 13755.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **359.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
