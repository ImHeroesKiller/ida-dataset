# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T10:25:14+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 408 | 1.49 | 70.9 | 607.3 |
| source_discovery | 408 | 4.32 | 186.3 | 1761.8 |
| connector | 408 | 90335.44 | 97806.1 | 36856861.2 |
| document_discovery | 408 | 90335.63 | 97806.2 | 36856936.7 |
| document_download | 408 | 236667.61 | 1509355.9 | 96560385.6 |
| extraction | 408 | 99.3 | 274.0 | 40513.2 |
| candidate_validation | 408 | 15.65 | 149.0 | 6385.3 |
| publish_queue | 408 | 15.71 | 149.1 | 6411.6 |
| append_dataset | 408 | 38.68 | 119.7 | 15780.7 |
| export | 408 | 0.35 | 2.7 | 143.0 |
| git_commit | 408 | 0.35 | 15.1 | 142.7 |
| push | 408 | 0.58 | 81.1 | 238.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12138 |
| Documents processed | 26783 |
| Process ratio | 220.7% (target ≥90.0%) |
| Rows published (traces) | 1969 |
| Sessions observed | 313 |
| Avg session duration (s) | 1059.297 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13952.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
