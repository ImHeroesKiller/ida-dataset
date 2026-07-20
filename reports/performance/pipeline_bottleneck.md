# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T10:31:35+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 127 | 1.0 | 6.5 | 127.4 |
| source_discovery | 127 | 3.07 | 39.8 | 389.5 |
| connector | 127 | 82210.78 | 97806.1 | 10440768.8 |
| document_discovery | 127 | 82210.92 | 97806.2 | 10440786.4 |
| document_download | 127 | 261393.03 | 1509355.9 | 33196915.1 |
| extraction | 127 | 83.02 | 274.0 | 10543.1 |
| candidate_validation | 127 | 8.21 | 30.0 | 1042.1 |
| publish_queue | 127 | 8.38 | 34.7 | 1064.3 |
| append_dataset | 127 | 44.84 | 119.7 | 5694.6 |
| export | 127 | 0.35 | 1.9 | 44.5 |
| git_commit | 127 | 0.32 | 2.1 | 40.5 |
| push | 127 | 0.31 | 0.8 | 39.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3538 |
| Documents processed | 10629 |
| Process ratio | 300.4% (target ≥90.0%) |
| Rows published (traces) | 567 |
| Sessions observed | 155 |
| Avg session duration (s) | 869.032 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.717 |
| Avg connector latency (ms) | 13847.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **300.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
