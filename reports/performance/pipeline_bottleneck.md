# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T20:42:58+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 174 | 0.99 | 6.5 | 171.7 |
| source_discovery | 174 | 3.1 | 39.8 | 539.0 |
| connector | 174 | 85398.58 | 97806.1 | 14859353.0 |
| document_discovery | 174 | 85398.73 | 97806.2 | 14859379.1 |
| document_download | 174 | 252608.26 | 1509355.9 | 43953837.8 |
| extraction | 174 | 87.29 | 274.0 | 15188.7 |
| candidate_validation | 174 | 9.42 | 30.0 | 1639.8 |
| publish_queue | 174 | 9.56 | 34.7 | 1663.7 |
| append_dataset | 174 | 43.31 | 119.7 | 7536.3 |
| export | 174 | 0.35 | 1.9 | 61.2 |
| git_commit | 174 | 0.31 | 2.1 | 54.4 |
| push | 174 | 0.31 | 0.8 | 54.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4975 |
| Documents processed | 13682 |
| Process ratio | 275.0% (target ≥90.0%) |
| Rows published (traces) | 802 |
| Sessions observed | 202 |
| Avg session duration (s) | 915.45 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.796 |
| Avg connector latency (ms) | 13738.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **275.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
