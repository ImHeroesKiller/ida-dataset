# Pipeline Bottleneck Analysis

**Generated:** 2026-07-28T11:36:01+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 213 | 1.32 | 70.9 | 281.7 |
| source_discovery | 213 | 3.93 | 186.3 | 836.9 |
| connector | 213 | 86977.76 | 97806.1 | 18526263.5 |
| document_discovery | 213 | 86977.91 | 97806.2 | 18526294.4 |
| document_download | 213 | 250948.14 | 1509355.9 | 53451953.4 |
| extraction | 213 | 90.2 | 274.0 | 19212.6 |
| candidate_validation | 213 | 10.47 | 37.2 | 2231.0 |
| publish_queue | 213 | 10.59 | 37.4 | 2256.3 |
| append_dataset | 213 | 42.37 | 119.7 | 9024.0 |
| export | 213 | 0.35 | 1.9 | 74.1 |
| git_commit | 213 | 0.31 | 2.1 | 66.4 |
| push | 213 | 0.32 | 0.8 | 67.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6164 |
| Documents processed | 15981 |
| Process ratio | 259.3% (target ≥90.0%) |
| Rows published (traces) | 994 |
| Sessions observed | 241 |
| Avg session duration (s) | 942.452 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.82 |
| Avg connector latency (ms) | 13804.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **259.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
