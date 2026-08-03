# Pipeline Bottleneck Analysis

**Generated:** 2026-08-03T10:13:58+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 277 | 1.39 | 70.9 | 384.6 |
| source_discovery | 277 | 4.16 | 186.3 | 1153.5 |
| connector | 277 | 88602.39 | 97806.1 | 24542862.5 |
| document_discovery | 277 | 88602.6 | 97806.2 | 24542920.8 |
| document_download | 277 | 237208.3 | 1509355.9 | 65706700.0 |
| extraction | 277 | 93.44 | 274.0 | 25884.0 |
| candidate_validation | 277 | 12.37 | 102.5 | 3427.8 |
| publish_queue | 277 | 12.46 | 102.7 | 3450.2 |
| append_dataset | 277 | 40.8 | 119.7 | 11301.0 |
| export | 277 | 0.35 | 2.1 | 96.9 |
| git_commit | 277 | 0.36 | 15.1 | 100.9 |
| push | 277 | 0.61 | 81.1 | 167.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8137 |
| Documents processed | 19581 |
| Process ratio | 240.6% (target ≥90.0%) |
| Rows published (traces) | 1314 |
| Sessions observed | 305 |
| Avg session duration (s) | 959.459 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.863 |
| Avg connector latency (ms) | 13848.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **240.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
