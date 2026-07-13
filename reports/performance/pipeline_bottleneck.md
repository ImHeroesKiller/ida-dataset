# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T07:14:42+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 42 | 1.11 | 6.5 | 46.5 |
| source_discovery | 42 | 2.7 | 3.3 | 113.2 |
| connector | 42 | 58344.31 | 97806.1 | 2450460.9 |
| document_discovery | 42 | 58344.45 | 97806.2 | 2450466.9 |
| document_download | 42 | 213671.99 | 1509355.9 | 8974223.5 |
| extraction | 42 | 66.41 | 109.5 | 2789.1 |
| candidate_validation | 42 | 5.47 | 8.7 | 229.6 |
| publish_queue | 42 | 5.53 | 8.8 | 232.2 |
| append_dataset | 42 | 43.42 | 119.7 | 1823.8 |
| export | 42 | 0.34 | 0.6 | 14.1 |
| git_commit | 42 | 0.34 | 2.1 | 14.3 |
| push | 42 | 0.32 | 0.8 | 13.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 953 |
| Documents processed | 3565 |
| Process ratio | 374.1% (target ≥90.0%) |
| Rows published (traces) | 146 |
| Sessions observed | 70 |
| Avg session duration (s) | 556.286 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.143 |
| Avg connector latency (ms) | 13702.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **374.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
