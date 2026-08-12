# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T08:35:53+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 407 | 1.49 | 70.9 | 606.1 |
| source_discovery | 407 | 4.32 | 186.3 | 1758.7 |
| connector | 407 | 90326.21 | 97806.1 | 36762767.5 |
| document_discovery | 407 | 90326.4 | 97806.2 | 36762842.9 |
| document_download | 407 | 236933.63 | 1509355.9 | 96431986.1 |
| extraction | 407 | 99.28 | 274.0 | 40407.6 |
| candidate_validation | 407 | 15.63 | 149.0 | 6360.7 |
| publish_queue | 407 | 15.69 | 149.1 | 6387.0 |
| append_dataset | 407 | 38.7 | 119.7 | 15752.1 |
| export | 407 | 0.35 | 2.7 | 142.7 |
| git_commit | 407 | 0.35 | 15.1 | 142.4 |
| push | 407 | 0.58 | 81.1 | 238.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12117 |
| Documents processed | 26742 |
| Process ratio | 220.7% (target ≥90.0%) |
| Rows published (traces) | 1964 |
| Sessions observed | 312 |
| Avg session duration (s) | 1059.612 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 14287.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
