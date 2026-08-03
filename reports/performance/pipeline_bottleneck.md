# Pipeline Bottleneck Analysis

**Generated:** 2026-08-03T10:57:20+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 278 | 1.39 | 70.9 | 385.8 |
| source_discovery | 278 | 4.16 | 186.3 | 1156.8 |
| connector | 278 | 88621.84 | 97806.1 | 24636870.5 |
| document_discovery | 278 | 88622.05 | 97806.2 | 24636929.0 |
| document_download | 278 | 236731.84 | 1509355.9 | 65811451.6 |
| extraction | 278 | 93.48 | 274.0 | 25986.5 |
| candidate_validation | 278 | 12.4 | 102.5 | 3446.9 |
| publish_queue | 278 | 12.48 | 102.7 | 3469.3 |
| append_dataset | 278 | 40.78 | 119.7 | 11337.2 |
| export | 278 | 0.35 | 2.1 | 97.2 |
| git_commit | 278 | 0.36 | 15.1 | 101.3 |
| push | 278 | 0.61 | 81.1 | 168.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8168 |
| Documents processed | 19632 |
| Process ratio | 240.4% (target ≥90.0%) |
| Rows published (traces) | 1319 |
| Sessions observed | 306 |
| Avg session duration (s) | 959.464 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.863 |
| Avg connector latency (ms) | 13973.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **240.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
