# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T11:38:11+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 193 | 0.99 | 6.5 | 191.2 |
| source_discovery | 193 | 3.08 | 39.8 | 593.6 |
| connector | 193 | 86242.58 | 97806.1 | 16644818.4 |
| document_discovery | 193 | 86242.73 | 97806.2 | 16644846.7 |
| document_download | 193 | 253951.03 | 1509355.9 | 49012549.1 |
| extraction | 193 | 88.72 | 274.0 | 17122.7 |
| candidate_validation | 193 | 10.02 | 37.2 | 1933.0 |
| publish_queue | 193 | 10.14 | 37.4 | 1957.4 |
| append_dataset | 193 | 42.86 | 119.7 | 8272.9 |
| export | 193 | 0.35 | 1.9 | 67.5 |
| git_commit | 193 | 0.31 | 2.1 | 60.2 |
| push | 193 | 0.32 | 0.8 | 60.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5564 |
| Documents processed | 14827 |
| Process ratio | 266.5% (target ≥90.0%) |
| Rows published (traces) | 897 |
| Sessions observed | 221 |
| Avg session duration (s) | 931.81 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.817 |
| Avg connector latency (ms) | 14146.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **266.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
