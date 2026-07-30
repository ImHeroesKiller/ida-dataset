# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T09:48:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 234 | 1.29 | 70.9 | 302.4 |
| source_discovery | 234 | 3.83 | 186.3 | 895.5 |
| connector | 234 | 87609.38 | 97806.1 | 20500595.2 |
| document_discovery | 234 | 87609.53 | 97806.2 | 20500630.1 |
| document_download | 234 | 244693.86 | 1509355.9 | 57258364.0 |
| extraction | 234 | 91.91 | 274.0 | 21506.5 |
| candidate_validation | 234 | 11.03 | 37.2 | 2582.1 |
| publish_queue | 234 | 11.12 | 37.4 | 2602.9 |
| append_dataset | 234 | 41.9 | 119.7 | 9804.3 |
| export | 234 | 0.35 | 1.9 | 80.9 |
| git_commit | 234 | 0.31 | 2.1 | 72.9 |
| push | 234 | 0.31 | 0.8 | 73.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6815 |
| Documents processed | 17179 |
| Process ratio | 252.1% (target ≥90.0%) |
| Rows published (traces) | 1099 |
| Sessions observed | 262 |
| Avg session duration (s) | 949.069 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.837 |
| Avg connector latency (ms) | 13778.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **252.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
