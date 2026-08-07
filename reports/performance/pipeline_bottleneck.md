# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T23:51:33+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 327 | 1.61 | 70.9 | 527.8 |
| source_discovery | 327 | 4.69 | 186.3 | 1532.3 |
| connector | 327 | 89427.66 | 97806.1 | 29242843.6 |
| document_discovery | 327 | 89427.85 | 97806.2 | 29242907.9 |
| document_download | 327 | 231592.15 | 1509355.9 | 75730632.5 |
| extraction | 327 | 96.18 | 274.0 | 31452.2 |
| candidate_validation | 327 | 13.73 | 136.9 | 4489.0 |
| publish_queue | 327 | 13.8 | 136.9 | 4512.5 |
| append_dataset | 327 | 39.57 | 119.7 | 12940.8 |
| export | 327 | 0.35 | 2.1 | 112.9 |
| git_commit | 327 | 0.36 | 15.1 | 116.1 |
| push | 327 | 0.65 | 81.1 | 214.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9677 |
| Documents processed | 22188 |
| Process ratio | 229.3% (target ≥90.0%) |
| Rows published (traces) | 1564 |
| Sessions observed | 302 |
| Avg session duration (s) | 1065.907 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.963 |
| Avg connector latency (ms) | 13761.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **229.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
