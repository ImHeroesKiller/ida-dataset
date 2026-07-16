# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T09:34:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 75 | 1.03 | 6.5 | 77.6 |
| source_discovery | 75 | 2.74 | 3.3 | 205.5 |
| connector | 75 | 74028.05 | 97806.1 | 5552103.4 |
| document_discovery | 75 | 74028.18 | 97806.2 | 5552113.8 |
| document_download | 75 | 272411.29 | 1509355.9 | 20430846.7 |
| extraction | 75 | 82.31 | 274.0 | 6172.9 |
| candidate_validation | 75 | 6.79 | 18.7 | 509.1 |
| publish_queue | 75 | 7.05 | 34.7 | 528.5 |
| append_dataset | 75 | 50.78 | 119.7 | 3808.5 |
| export | 75 | 0.34 | 0.6 | 25.3 |
| git_commit | 75 | 0.33 | 2.1 | 24.4 |
| push | 75 | 0.32 | 0.8 | 23.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1956 |
| Documents processed | 7422 |
| Process ratio | 379.4% (target ≥90.0%) |
| Rows published (traces) | 307 |
| Sessions observed | 103 |
| Avg session duration (s) | 763.602 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.5 |
| Avg connector latency (ms) | 13942.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **379.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
