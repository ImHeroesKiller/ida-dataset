# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T09:30:46+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 192 | 0.99 | 6.5 | 190.3 |
| source_discovery | 192 | 3.08 | 39.8 | 590.7 |
| connector | 192 | 86201.96 | 97806.1 | 16550775.9 |
| document_discovery | 192 | 86202.1 | 97806.2 | 16550804.0 |
| document_download | 192 | 254366.57 | 1509355.9 | 48838381.6 |
| extraction | 192 | 88.61 | 274.0 | 17013.4 |
| candidate_validation | 192 | 9.99 | 37.2 | 1918.8 |
| publish_queue | 192 | 10.12 | 37.4 | 1943.2 |
| append_dataset | 192 | 42.89 | 119.7 | 8234.6 |
| export | 192 | 0.35 | 1.9 | 67.2 |
| git_commit | 192 | 0.31 | 2.1 | 59.9 |
| push | 192 | 0.32 | 0.8 | 60.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5533 |
| Documents processed | 14765 |
| Process ratio | 266.9% (target ≥90.0%) |
| Rows published (traces) | 892 |
| Sessions observed | 220 |
| Avg session duration (s) | 931.441 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.816 |
| Avg connector latency (ms) | 13704.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **266.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
