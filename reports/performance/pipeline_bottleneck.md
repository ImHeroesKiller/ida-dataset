# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T22:25:22+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 199 | 0.99 | 6.5 | 197.0 |
| source_discovery | 199 | 3.07 | 39.8 | 611.1 |
| connector | 199 | 86477.83 | 97806.1 | 17209087.7 |
| document_discovery | 199 | 86477.97 | 97806.2 | 17209116.7 |
| document_download | 199 | 254444.87 | 1509355.9 | 50634530.1 |
| extraction | 199 | 89.21 | 274.0 | 17753.5 |
| candidate_validation | 199 | 10.17 | 37.2 | 2023.8 |
| publish_queue | 199 | 10.29 | 37.4 | 2048.4 |
| append_dataset | 199 | 42.65 | 119.7 | 8487.0 |
| export | 199 | 0.35 | 1.9 | 69.5 |
| git_commit | 199 | 0.31 | 2.1 | 62.1 |
| push | 199 | 0.32 | 0.8 | 62.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5740 |
| Documents processed | 15145 |
| Process ratio | 263.9% (target ≥90.0%) |
| Rows published (traces) | 927 |
| Sessions observed | 227 |
| Avg session duration (s) | 936.471 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.823 |
| Avg connector latency (ms) | 13719.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **263.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
