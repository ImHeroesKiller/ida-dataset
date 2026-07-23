# Pipeline Bottleneck Analysis

**Generated:** 2026-07-23T22:21:40+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 164 | 0.99 | 6.5 | 162.1 |
| source_discovery | 164 | 3.11 | 39.8 | 510.2 |
| connector | 164 | 84874.14 | 97806.1 | 13919358.6 |
| document_discovery | 164 | 84874.29 | 97806.2 | 13919383.4 |
| document_download | 164 | 253110.55 | 1509355.9 | 41510130.7 |
| extraction | 164 | 86.8 | 274.0 | 14235.2 |
| candidate_validation | 164 | 9.2 | 30.0 | 1508.9 |
| publish_queue | 164 | 9.35 | 34.7 | 1532.6 |
| append_dataset | 164 | 43.7 | 119.7 | 7167.4 |
| export | 164 | 0.35 | 1.9 | 57.8 |
| git_commit | 164 | 0.31 | 2.1 | 51.5 |
| push | 164 | 0.31 | 0.8 | 51.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4665 |
| Documents processed | 13094 |
| Process ratio | 280.7% (target ≥90.0%) |
| Rows published (traces) | 752 |
| Sessions observed | 192 |
| Avg session duration (s) | 906.615 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.783 |
| Avg connector latency (ms) | 13731.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **280.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
