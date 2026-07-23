# Pipeline Bottleneck Analysis

**Generated:** 2026-07-23T14:25:11+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 160 | 0.99 | 6.5 | 158.3 |
| source_discovery | 160 | 3.12 | 39.8 | 498.7 |
| connector | 160 | 84648.02 | 97806.1 | 13543683.6 |
| document_discovery | 160 | 84648.18 | 97806.2 | 13543708.0 |
| document_download | 160 | 251089.04 | 1509355.9 | 40174246.7 |
| extraction | 160 | 86.58 | 274.0 | 13852.0 |
| candidate_validation | 160 | 9.1 | 30.0 | 1456.1 |
| publish_queue | 160 | 9.25 | 34.7 | 1479.9 |
| append_dataset | 160 | 43.83 | 119.7 | 7013.2 |
| export | 160 | 0.35 | 1.9 | 56.3 |
| git_commit | 160 | 0.31 | 2.1 | 50.3 |
| push | 160 | 0.31 | 0.8 | 50.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4541 |
| Documents processed | 12844 |
| Process ratio | 282.8% (target ≥90.0%) |
| Rows published (traces) | 732 |
| Sessions observed | 188 |
| Avg session duration (s) | 900.894 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.778 |
| Avg connector latency (ms) | 13715.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **282.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
