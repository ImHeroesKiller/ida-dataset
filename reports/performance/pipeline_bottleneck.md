# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T08:59:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 233 | 1.29 | 70.9 | 301.4 |
| source_discovery | 233 | 3.83 | 186.3 | 892.8 |
| connector | 233 | 87582.52 | 97806.1 | 20406726.6 |
| document_discovery | 233 | 87582.67 | 97806.2 | 20406761.4 |
| document_download | 233 | 243817.27 | 1509355.9 | 56809422.8 |
| extraction | 233 | 91.86 | 274.0 | 21404.1 |
| candidate_validation | 233 | 11.01 | 37.2 | 2566.3 |
| publish_queue | 233 | 11.1 | 37.4 | 2587.0 |
| append_dataset | 233 | 41.91 | 119.7 | 9764.9 |
| export | 233 | 0.35 | 1.9 | 80.6 |
| git_commit | 233 | 0.31 | 2.1 | 72.6 |
| push | 233 | 0.31 | 0.8 | 73.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6784 |
| Documents processed | 17117 |
| Process ratio | 252.3% (target ≥90.0%) |
| Rows published (traces) | 1094 |
| Sessions observed | 261 |
| Avg session duration (s) | 947.797 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.836 |
| Avg connector latency (ms) | 13797.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **252.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
