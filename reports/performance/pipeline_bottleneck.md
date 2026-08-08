# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T11:47:57+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 337 | 1.6 | 70.9 | 537.6 |
| source_discovery | 337 | 4.63 | 186.3 | 1560.3 |
| connector | 337 | 89562.02 | 97806.1 | 30182401.2 |
| document_discovery | 337 | 89562.22 | 97806.2 | 30182466.9 |
| document_download | 337 | 232535.85 | 1509355.9 | 78364582.2 |
| extraction | 337 | 96.52 | 274.0 | 32527.0 |
| candidate_validation | 337 | 13.92 | 136.9 | 4690.3 |
| publish_queue | 337 | 13.99 | 136.9 | 4714.0 |
| append_dataset | 337 | 39.42 | 119.7 | 13285.1 |
| export | 337 | 0.34 | 2.1 | 115.9 |
| git_commit | 337 | 0.36 | 15.1 | 119.9 |
| push | 337 | 0.64 | 81.1 | 217.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9977 |
| Documents processed | 22745 |
| Process ratio | 228.0% (target ≥90.0%) |
| Rows published (traces) | 1614 |
| Sessions observed | 312 |
| Avg session duration (s) | 1067.298 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.965 |
| Avg connector latency (ms) | 13665.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **228.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
