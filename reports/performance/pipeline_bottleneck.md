# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T21:15:37+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 93 | 1.02 | 6.5 | 94.9 |
| source_discovery | 93 | 2.75 | 3.3 | 255.9 |
| connector | 93 | 77905.03 | 97806.1 | 7245168.2 |
| document_discovery | 93 | 77905.18 | 97806.2 | 7245181.8 |
| document_download | 93 | 271960.23 | 1509355.9 | 25292301.4 |
| extraction | 93 | 83.06 | 274.0 | 7724.6 |
| candidate_validation | 93 | 7.23 | 18.7 | 672.1 |
| publish_queue | 93 | 7.44 | 34.7 | 692.0 |
| append_dataset | 93 | 47.7 | 119.7 | 4436.3 |
| export | 93 | 0.34 | 0.6 | 31.3 |
| git_commit | 93 | 0.32 | 2.1 | 29.7 |
| push | 93 | 0.31 | 0.8 | 29.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2504 |
| Documents processed | 8491 |
| Process ratio | 339.1% (target ≥90.0%) |
| Rows published (traces) | 397 |
| Sessions observed | 121 |
| Avg session duration (s) | 813.355 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.605 |
| Avg connector latency (ms) | 13686.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **339.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
