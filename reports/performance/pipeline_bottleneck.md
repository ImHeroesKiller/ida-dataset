# Pipeline Bottleneck Analysis

**Generated:** 2026-08-06T08:51:54+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 307 | 1.52 | 70.9 | 467.5 |
| source_discovery | 307 | 4.28 | 186.3 | 1313.7 |
| connector | 307 | 89131.33 | 97806.1 | 27363317.0 |
| document_discovery | 307 | 89131.53 | 97806.2 | 27363378.9 |
| document_download | 307 | 234080.93 | 1509355.9 | 71862845.8 |
| extraction | 307 | 95.14 | 274.0 | 29207.6 |
| candidate_validation | 307 | 12.97 | 102.5 | 3981.4 |
| publish_queue | 307 | 13.04 | 102.7 | 4004.2 |
| append_dataset | 307 | 39.99 | 119.7 | 12278.4 |
| export | 307 | 0.35 | 2.1 | 106.5 |
| git_commit | 307 | 0.36 | 15.1 | 110.3 |
| push | 307 | 0.68 | 81.1 | 208.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9057 |
| Documents processed | 21079 |
| Process ratio | 232.7% (target ≥90.0%) |
| Rows published (traces) | 1464 |
| Sessions observed | 303 |
| Avg session duration (s) | 1058.614 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.929 |
| Avg connector latency (ms) | 13903.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **232.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
