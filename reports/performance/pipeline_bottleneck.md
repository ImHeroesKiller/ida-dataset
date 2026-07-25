# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T11:35:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 181 | 0.99 | 6.5 | 179.0 |
| source_discovery | 181 | 3.09 | 39.8 | 559.0 |
| connector | 181 | 85731.24 | 97806.1 | 15517354.1 |
| document_discovery | 181 | 85731.39 | 97806.2 | 15517381.1 |
| document_download | 181 | 253051.19 | 1509355.9 | 45802265.2 |
| extraction | 181 | 87.78 | 274.0 | 15888.7 |
| candidate_validation | 181 | 9.6 | 30.0 | 1737.2 |
| publish_queue | 181 | 9.73 | 34.7 | 1761.2 |
| append_dataset | 181 | 43.13 | 119.7 | 7805.8 |
| export | 181 | 0.35 | 1.9 | 63.7 |
| git_commit | 181 | 0.31 | 2.1 | 56.5 |
| push | 181 | 0.31 | 0.8 | 56.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5192 |
| Documents processed | 14094 |
| Process ratio | 271.5% (target ≥90.0%) |
| Rows published (traces) | 837 |
| Sessions observed | 209 |
| Avg session duration (s) | 921.746 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.805 |
| Avg connector latency (ms) | 13785.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **271.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
