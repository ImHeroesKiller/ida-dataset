# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T07:14:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 332 | 1.6 | 70.9 | 532.7 |
| source_discovery | 332 | 4.66 | 186.3 | 1546.4 |
| connector | 332 | 89494.05 | 97806.1 | 29712023.7 |
| document_discovery | 332 | 89494.24 | 97806.2 | 29712088.7 |
| document_download | 332 | 231709.23 | 1509355.9 | 76927465.2 |
| extraction | 332 | 96.4 | 274.0 | 32004.3 |
| candidate_validation | 332 | 13.82 | 136.9 | 4588.5 |
| publish_queue | 332 | 13.89 | 136.9 | 4612.1 |
| append_dataset | 332 | 39.51 | 119.7 | 13118.6 |
| export | 332 | 0.34 | 2.1 | 114.4 |
| git_commit | 332 | 0.35 | 15.1 | 117.6 |
| push | 332 | 0.65 | 81.1 | 215.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9832 |
| Documents processed | 22487 |
| Process ratio | 228.7% (target ≥90.0%) |
| Rows published (traces) | 1589 |
| Sessions observed | 307 |
| Avg session duration (s) | 1066.003 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.964 |
| Avg connector latency (ms) | 13755.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **228.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
