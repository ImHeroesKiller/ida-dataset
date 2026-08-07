# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T20:59:39+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 324 | 1.62 | 70.9 | 524.5 |
| source_discovery | 324 | 4.7 | 186.3 | 1522.6 |
| connector | 324 | 89385.95 | 97806.1 | 28961048.3 |
| document_discovery | 324 | 89386.15 | 97806.2 | 28961112.1 |
| document_download | 324 | 231615.9 | 1509355.9 | 75043550.6 |
| extraction | 324 | 96.04 | 274.0 | 31115.5 |
| candidate_validation | 324 | 13.66 | 136.9 | 4425.4 |
| publish_queue | 324 | 13.73 | 136.9 | 4448.5 |
| append_dataset | 324 | 39.59 | 119.7 | 12827.4 |
| export | 324 | 0.35 | 2.1 | 111.9 |
| git_commit | 324 | 0.36 | 15.1 | 115.1 |
| push | 324 | 0.66 | 81.1 | 213.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9584 |
| Documents processed | 22013 |
| Process ratio | 229.7% (target ≥90.0%) |
| Rows published (traces) | 1549 |
| Sessions observed | 320 |
| Avg session duration (s) | 1056.091 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.932 |
| Avg connector latency (ms) | 13666.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **229.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
