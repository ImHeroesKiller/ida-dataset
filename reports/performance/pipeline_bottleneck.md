# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T08:51:42+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 168 | 0.99 | 6.5 | 166.0 |
| source_discovery | 168 | 3.11 | 39.8 | 521.8 |
| connector | 168 | 85093.35 | 97806.1 | 14295682.3 |
| document_discovery | 168 | 85093.5 | 97806.2 | 14295707.6 |
| document_download | 168 | 250096.19 | 1509355.9 | 42016159.9 |
| extraction | 168 | 87.12 | 274.0 | 14636.8 |
| candidate_validation | 168 | 9.3 | 30.0 | 1562.3 |
| publish_queue | 168 | 9.44 | 34.7 | 1586.1 |
| append_dataset | 168 | 43.63 | 119.7 | 7330.2 |
| export | 168 | 0.35 | 1.9 | 59.1 |
| git_commit | 168 | 0.31 | 2.1 | 52.8 |
| push | 168 | 0.31 | 0.8 | 52.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4789 |
| Documents processed | 13332 |
| Process ratio | 278.4% (target ≥90.0%) |
| Rows published (traces) | 772 |
| Sessions observed | 196 |
| Avg session duration (s) | 907.821 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.789 |
| Avg connector latency (ms) | 13810.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **278.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
