# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T15:21:40+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 183 | 0.99 | 6.5 | 181.1 |
| source_discovery | 183 | 3.09 | 39.8 | 564.8 |
| connector | 183 | 85823.02 | 97806.1 | 15705613.4 |
| document_discovery | 183 | 85823.17 | 97806.2 | 15705640.6 |
| document_download | 183 | 253844.85 | 1509355.9 | 46453608.2 |
| extraction | 183 | 87.94 | 274.0 | 16092.8 |
| candidate_validation | 183 | 9.65 | 30.0 | 1765.3 |
| publish_queue | 183 | 9.78 | 34.7 | 1789.5 |
| append_dataset | 183 | 43.09 | 119.7 | 7885.6 |
| export | 183 | 0.35 | 1.9 | 64.4 |
| git_commit | 183 | 0.31 | 2.1 | 57.1 |
| push | 183 | 0.32 | 0.8 | 57.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5254 |
| Documents processed | 14218 |
| Process ratio | 270.6% (target ≥90.0%) |
| Rows published (traces) | 847 |
| Sessions observed | 211 |
| Avg session duration (s) | 924.019 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.807 |
| Avg connector latency (ms) | 13711.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **270.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
