# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T23:08:47+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 24 | 0.94 | 1.3 | 22.5 |
| source_discovery | 24 | 2.58 | 3.3 | 62.0 |
| connector | 24 | 35277.9 | 97806.1 | 846669.7 |
| document_discovery | 24 | 35278.06 | 97806.2 | 846673.4 |
| document_download | 24 | 203881.35 | 1509355.9 | 4893152.5 |
| extraction | 24 | 46.28 | 109.5 | 1110.7 |
| candidate_validation | 24 | 4.39 | 7.3 | 105.3 |
| publish_queue | 24 | 4.48 | 8.8 | 107.6 |
| append_dataset | 24 | 26.78 | 119.7 | 642.7 |
| export | 24 | 0.32 | 0.6 | 7.7 |
| git_commit | 24 | 0.3 | 0.4 | 7.1 |
| push | 24 | 0.3 | 0.5 | 7.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 425 |
| Documents processed | 1255 |
| Process ratio | 295.3% (target ≥90.0%) |
| Rows published (traces) | 65 |
| Sessions observed | 52 |
| Avg session duration (s) | 379.096 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.556 |
| Avg connector latency (ms) | 13644.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **295.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
