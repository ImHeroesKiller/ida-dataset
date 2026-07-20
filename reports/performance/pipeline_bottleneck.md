# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T13:26:20+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 128 | 1.0 | 6.5 | 128.2 |
| source_discovery | 128 | 3.18 | 39.8 | 406.9 |
| connector | 128 | 82301.21 | 97806.1 | 10534555.5 |
| document_discovery | 128 | 82301.35 | 97806.2 | 10534573.3 |
| document_download | 128 | 260860.63 | 1509355.9 | 33390161.0 |
| extraction | 128 | 83.92 | 274.0 | 10742.3 |
| candidate_validation | 128 | 8.2 | 30.0 | 1049.6 |
| publish_queue | 128 | 8.37 | 34.7 | 1072.0 |
| append_dataset | 128 | 44.69 | 119.7 | 5720.7 |
| export | 128 | 0.35 | 1.9 | 44.8 |
| git_commit | 128 | 0.32 | 2.1 | 40.7 |
| push | 128 | 0.31 | 0.8 | 39.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3569 |
| Documents processed | 10703 |
| Process ratio | 299.9% (target ≥90.0%) |
| Rows published (traces) | 572 |
| Sessions observed | 156 |
| Avg session duration (s) | 870.103 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.719 |
| Avg connector latency (ms) | 13762.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **299.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
