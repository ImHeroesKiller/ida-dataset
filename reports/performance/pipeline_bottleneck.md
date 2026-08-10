# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T02:14:47+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 371 | 1.54 | 70.9 | 570.3 |
| source_discovery | 371 | 4.46 | 186.3 | 1655.3 |
| connector | 371 | 89969.15 | 97806.1 | 33378555.2 |
| document_discovery | 371 | 89969.34 | 97806.2 | 33378626.1 |
| document_download | 371 | 236205.89 | 1509355.9 | 87632383.9 |
| extraction | 371 | 97.58 | 274.0 | 36201.9 |
| candidate_validation | 371 | 14.52 | 136.9 | 5388.2 |
| publish_queue | 371 | 14.59 | 136.9 | 5413.1 |
| append_dataset | 371 | 38.89 | 119.7 | 14426.8 |
| export | 371 | 0.35 | 2.1 | 128.8 |
| git_commit | 371 | 0.35 | 15.1 | 130.5 |
| push | 371 | 0.61 | 81.1 | 227.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11021 |
| Documents processed | 24644 |
| Process ratio | 223.6% (target ≥90.0%) |
| Rows published (traces) | 1784 |
| Sessions observed | 301 |
| Avg session duration (s) | 1058.601 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13596.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
