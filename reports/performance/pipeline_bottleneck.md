# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T10:06:22+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 180 | 0.99 | 6.5 | 178.0 |
| source_discovery | 180 | 3.09 | 39.8 | 556.1 |
| connector | 180 | 85685.91 | 97806.1 | 15423463.2 |
| document_discovery | 180 | 85686.06 | 97806.2 | 15423490.1 |
| document_download | 180 | 253651.98 | 1509355.9 | 45657357.0 |
| extraction | 180 | 87.68 | 274.0 | 15782.4 |
| candidate_validation | 180 | 9.57 | 30.0 | 1722.9 |
| publish_queue | 180 | 9.7 | 34.7 | 1746.9 |
| append_dataset | 180 | 43.14 | 119.7 | 7765.2 |
| export | 180 | 0.35 | 1.9 | 63.3 |
| git_commit | 180 | 0.31 | 2.1 | 56.2 |
| push | 180 | 0.31 | 0.8 | 56.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5161 |
| Documents processed | 14032 |
| Process ratio | 271.9% (target ≥90.0%) |
| Rows published (traces) | 832 |
| Sessions observed | 208 |
| Avg session duration (s) | 921.462 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.803 |
| Avg connector latency (ms) | 13802.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **271.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
