# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T08:32:14+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 11 | 0.81 | 1.1 | 8.9 |
| source_discovery | 11 | 2.23 | 2.8 | 24.5 |
| connector | 11 | 5455.03 | 7301.3 | 60005.3 |
| document_discovery | 11 | 5455.23 | 7301.7 | 60007.5 |
| document_download | 11 | 29335.95 | 49397.5 | 322695.5 |
| extraction | 11 | 19.01 | 31.4 | 209.1 |
| candidate_validation | 11 | 3.85 | 6.6 | 42.3 |
| publish_queue | 11 | 3.85 | 6.5 | 42.4 |
| append_dataset | 11 | 4.33 | 7.4 | 47.6 |
| export | 11 | 0.3 | 0.4 | 3.3 |
| git_commit | 11 | 0.28 | 0.3 | 3.1 |
| push | 11 | 0.28 | 0.3 | 3.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 95 |
| Documents processed | 57 |
| Process ratio | 60.0% (target ≥90.0%) |
| Rows published (traces) | 26 |
| Sessions observed | 37 |
| Avg session duration (s) | 132.459 |
| Max session duration (s) | 604.0 |
| Rows / session (productive) | 2.778 |
| Avg connector latency (ms) | 2443.4 |
| Worker utilization (est) | 0.049 |
| Idle fraction (est) | 0.951 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **60.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
