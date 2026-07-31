# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T10:58:10+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 245 | 1.28 | 70.9 | 313.7 |
| source_discovery | 245 | 3.78 | 186.3 | 927.3 |
| connector | 245 | 87896.95 | 97806.1 | 21534751.7 |
| document_discovery | 245 | 87897.17 | 97806.2 | 21534805.6 |
| document_download | 245 | 242350.41 | 1509355.9 | 59375849.4 |
| extraction | 245 | 92.42 | 274.0 | 22643.5 |
| candidate_validation | 245 | 11.67 | 102.5 | 2858.4 |
| publish_queue | 245 | 11.75 | 102.7 | 2879.7 |
| append_dataset | 245 | 41.62 | 119.7 | 10198.1 |
| export | 245 | 0.35 | 2.1 | 86.5 |
| git_commit | 245 | 0.37 | 15.1 | 91.2 |
| push | 245 | 0.64 | 81.1 | 157.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7156 |
| Documents processed | 17793 |
| Process ratio | 248.6% (target ≥90.0%) |
| Rows published (traces) | 1154 |
| Sessions observed | 273 |
| Avg session duration (s) | 953.073 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.845 |
| Avg connector latency (ms) | 13776.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **248.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
