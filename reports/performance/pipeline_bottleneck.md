# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T11:48:13+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 13 | 0.84 | 1.1 | 10.9 |
| source_discovery | 13 | 2.31 | 2.8 | 30.0 |
| connector | 13 | 12322.54 | 93968.9 | 160193.0 |
| document_discovery | 13 | 12322.72 | 93969.0 | 160195.4 |
| document_download | 13 | 29068.13 | 49397.5 | 377885.7 |
| extraction | 13 | 21.38 | 38.1 | 277.9 |
| candidate_validation | 13 | 4.3 | 6.9 | 55.9 |
| publish_queue | 13 | 4.31 | 6.9 | 56.0 |
| append_dataset | 13 | 5.4 | 14.9 | 70.2 |
| export | 13 | 0.32 | 0.6 | 4.2 |
| git_commit | 13 | 0.29 | 0.4 | 3.8 |
| push | 13 | 0.28 | 0.3 | 3.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 137 |
| Documents processed | 95 |
| Process ratio | 69.3% (target ≥90.0%) |
| Rows published (traces) | 36 |
| Sessions observed | 39 |
| Avg session duration (s) | 173.077 |
| Max session duration (s) | 1262.0 |
| Rows / session (productive) | 3.182 |
| Avg connector latency (ms) | 13681.8 |
| Worker utilization (est) | 0.075 |
| Idle fraction (est) | 0.925 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **69.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
