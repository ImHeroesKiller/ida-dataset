# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T12:01:52+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 393 | 1.51 | 70.9 | 592.0 |
| source_discovery | 393 | 4.37 | 186.3 | 1718.2 |
| connector | 393 | 90193.26 | 97806.1 | 35445950.8 |
| document_discovery | 393 | 90193.45 | 97806.2 | 35446024.4 |
| document_download | 393 | 236878.73 | 1509355.9 | 93093340.5 |
| extraction | 393 | 98.61 | 274.0 | 38754.1 |
| candidate_validation | 393 | 15.33 | 149.0 | 6025.7 |
| publish_queue | 393 | 15.4 | 149.1 | 6051.5 |
| append_dataset | 393 | 38.74 | 119.7 | 15223.2 |
| export | 393 | 0.35 | 2.7 | 138.1 |
| git_commit | 393 | 0.35 | 15.1 | 137.4 |
| push | 393 | 0.6 | 81.1 | 233.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11683 |
| Documents processed | 25896 |
| Process ratio | 221.7% (target ≥90.0%) |
| Rows published (traces) | 1894 |
| Sessions observed | 311 |
| Avg session duration (s) | 1061.273 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13897.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
