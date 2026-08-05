# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T10:54:48+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 298 | 1.36 | 70.9 | 404.8 |
| source_discovery | 298 | 4.32 | 186.3 | 1288.4 |
| connector | 298 | 88982.57 | 97806.1 | 26516805.2 |
| document_discovery | 298 | 88982.77 | 97806.2 | 26516866.1 |
| document_download | 298 | 234474.76 | 1509355.9 | 69873477.7 |
| extraction | 298 | 94.39 | 274.0 | 28128.5 |
| candidate_validation | 298 | 12.78 | 102.5 | 3809.2 |
| publish_queue | 298 | 12.86 | 102.7 | 3831.6 |
| append_dataset | 298 | 40.2 | 119.7 | 11979.3 |
| export | 298 | 0.35 | 2.1 | 103.5 |
| git_commit | 298 | 0.36 | 15.1 | 107.5 |
| push | 298 | 0.69 | 81.1 | 205.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8788 |
| Documents processed | 20626 |
| Process ratio | 234.7% (target ≥90.0%) |
| Rows published (traces) | 1419 |
| Sessions observed | 326 |
| Avg session duration (s) | 962.442 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.873 |
| Avg connector latency (ms) | 13938.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **234.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
