# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T03:17:42+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 189 | 0.99 | 6.5 | 187.3 |
| source_discovery | 189 | 3.08 | 39.8 | 582.4 |
| connector | 189 | 86077.69 | 97806.1 | 16268683.1 |
| document_discovery | 189 | 86077.84 | 97806.2 | 16268711.0 |
| document_download | 189 | 254282.37 | 1509355.9 | 48059368.8 |
| extraction | 189 | 88.43 | 274.0 | 16713.3 |
| candidate_validation | 189 | 9.8 | 30.0 | 1851.6 |
| publish_queue | 189 | 9.92 | 34.7 | 1875.8 |
| append_dataset | 189 | 43.0 | 119.7 | 8126.6 |
| export | 189 | 0.35 | 1.9 | 66.3 |
| git_commit | 189 | 0.31 | 2.1 | 58.9 |
| push | 189 | 0.32 | 0.8 | 59.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5440 |
| Documents processed | 14590 |
| Process ratio | 268.2% (target ≥90.0%) |
| Rows published (traces) | 877 |
| Sessions observed | 217 |
| Avg session duration (s) | 929.171 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.813 |
| Avg connector latency (ms) | 13785.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **268.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
