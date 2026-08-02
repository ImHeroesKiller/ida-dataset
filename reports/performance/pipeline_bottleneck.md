# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T22:16:53+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 273 | 1.39 | 70.9 | 380.2 |
| source_discovery | 273 | 4.18 | 186.3 | 1141.6 |
| connector | 273 | 88522.15 | 97806.1 | 24166548.3 |
| document_discovery | 273 | 88522.37 | 97806.2 | 24166606.1 |
| document_download | 273 | 238688.71 | 1509355.9 | 65162016.6 |
| extraction | 273 | 93.23 | 274.0 | 25452.6 |
| candidate_validation | 273 | 12.28 | 102.5 | 3351.2 |
| publish_queue | 273 | 12.36 | 102.7 | 3373.5 |
| append_dataset | 273 | 40.83 | 119.7 | 11147.9 |
| export | 273 | 0.35 | 2.1 | 95.5 |
| git_commit | 273 | 0.37 | 15.1 | 99.7 |
| push | 273 | 0.61 | 81.1 | 166.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8013 |
| Documents processed | 19352 |
| Process ratio | 241.5% (target ≥90.0%) |
| Rows published (traces) | 1294 |
| Sessions observed | 301 |
| Avg session duration (s) | 959.116 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.861 |
| Avg connector latency (ms) | 13689.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **241.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
