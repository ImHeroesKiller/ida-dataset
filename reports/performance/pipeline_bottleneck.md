# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T10:18:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 203 | 0.99 | 6.5 | 201.2 |
| source_discovery | 203 | 3.07 | 39.8 | 623.0 |
| connector | 203 | 86628.46 | 97806.1 | 17585576.6 |
| document_discovery | 203 | 86628.6 | 97806.2 | 17585606.2 |
| document_download | 203 | 254937.77 | 1509355.9 | 51752366.5 |
| extraction | 203 | 89.52 | 274.0 | 18173.1 |
| candidate_validation | 203 | 10.27 | 37.2 | 2084.8 |
| publish_queue | 203 | 10.39 | 37.4 | 2109.5 |
| append_dataset | 203 | 42.58 | 119.7 | 8643.3 |
| export | 203 | 0.35 | 1.9 | 70.7 |
| git_commit | 203 | 0.31 | 2.1 | 63.4 |
| push | 203 | 0.32 | 0.8 | 64.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5864 |
| Documents processed | 15393 |
| Process ratio | 262.5% (target ≥90.0%) |
| Rows published (traces) | 947 |
| Sessions observed | 231 |
| Avg session duration (s) | 939.645 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.827 |
| Avg connector latency (ms) | 13767.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **262.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
