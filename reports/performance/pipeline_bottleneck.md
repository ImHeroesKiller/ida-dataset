# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T19:26:52+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 21 | 0.9 | 1.3 | 18.9 |
| source_discovery | 21 | 2.52 | 3.2 | 52.9 |
| connector | 21 | 26903.56 | 97806.1 | 564974.8 |
| document_discovery | 21 | 26903.73 | 97806.2 | 564978.3 |
| document_download | 21 | 188787.4 | 1509355.9 | 3964535.4 |
| extraction | 21 | 37.87 | 93.4 | 795.2 |
| candidate_validation | 21 | 4.02 | 6.9 | 84.5 |
| publish_queue | 21 | 4.03 | 6.9 | 84.7 |
| append_dataset | 21 | 20.87 | 119.7 | 438.3 |
| export | 21 | 0.32 | 0.6 | 6.7 |
| git_commit | 21 | 0.3 | 0.4 | 6.2 |
| push | 21 | 0.29 | 0.3 | 6.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 332 |
| Documents processed | 884 |
| Process ratio | 266.3% (target ≥90.0%) |
| Rows published (traces) | 50 |
| Sessions observed | 49 |
| Avg session duration (s) | 331.0 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.267 |
| Avg connector latency (ms) | 13645.0 |
| Worker utilization (est) | 0.79 |
| Idle fraction (est) | 0.21 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **266.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
