# Pipeline Bottleneck Analysis

**Generated:** 2026-07-13T00:18:50+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 40 | 1.11 | 6.5 | 44.3 |
| source_discovery | 40 | 2.68 | 3.3 | 107.2 |
| connector | 40 | 56561.65 | 97806.1 | 2262466.1 |
| document_discovery | 40 | 56561.8 | 97806.2 | 2262471.9 |
| document_download | 40 | 209045.68 | 1509355.9 | 8361827.4 |
| extraction | 40 | 64.71 | 109.5 | 2588.5 |
| candidate_validation | 40 | 5.36 | 8.7 | 214.4 |
| publish_queue | 40 | 5.42 | 8.8 | 216.9 |
| append_dataset | 40 | 42.16 | 119.7 | 1686.5 |
| export | 40 | 0.33 | 0.6 | 13.2 |
| git_commit | 40 | 0.34 | 2.1 | 13.7 |
| push | 40 | 0.32 | 0.8 | 12.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 891 |
| Documents processed | 3302 |
| Process ratio | 370.6% (target ≥90.0%) |
| Rows published (traces) | 136 |
| Sessions observed | 68 |
| Avg session duration (s) | 538.221 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.091 |
| Avg connector latency (ms) | 13610.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **370.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
