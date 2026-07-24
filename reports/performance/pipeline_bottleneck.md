# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T12:45:17+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 170 | 0.99 | 6.5 | 168.0 |
| source_discovery | 170 | 3.11 | 39.8 | 527.9 |
| connector | 170 | 85199.4 | 97806.1 | 14483898.5 |
| document_discovery | 170 | 85199.55 | 97806.2 | 14483924.0 |
| document_download | 170 | 250824.12 | 1509355.9 | 42640101.0 |
| extraction | 170 | 87.25 | 274.0 | 14832.8 |
| candidate_validation | 170 | 9.36 | 30.0 | 1590.4 |
| publish_queue | 170 | 9.5 | 34.7 | 1614.3 |
| append_dataset | 170 | 43.54 | 119.7 | 7401.6 |
| export | 170 | 0.35 | 1.9 | 59.8 |
| git_commit | 170 | 0.31 | 2.1 | 53.4 |
| push | 170 | 0.31 | 0.8 | 53.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4851 |
| Documents processed | 13445 |
| Process ratio | 277.2% (target ≥90.0%) |
| Rows published (traces) | 782 |
| Sessions observed | 198 |
| Avg session duration (s) | 910.197 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.791 |
| Avg connector latency (ms) | 13821.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **277.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
