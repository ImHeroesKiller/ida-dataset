# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T20:16:04+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 382 | 1.52 | 70.9 | 580.9 |
| source_discovery | 382 | 4.41 | 186.3 | 1686.0 |
| connector | 382 | 90083.85 | 97806.1 | 34412032.4 |
| document_discovery | 382 | 90084.04 | 97806.2 | 34412104.7 |
| document_download | 382 | 238322.26 | 1509355.9 | 91039102.5 |
| extraction | 382 | 98.23 | 274.0 | 37523.1 |
| candidate_validation | 382 | 15.09 | 149.0 | 5766.0 |
| publish_queue | 382 | 15.16 | 149.1 | 5791.1 |
| append_dataset | 382 | 38.8 | 119.7 | 14821.3 |
| export | 382 | 0.35 | 2.7 | 134.7 |
| git_commit | 382 | 0.35 | 15.1 | 134.1 |
| push | 382 | 0.6 | 81.1 | 230.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11352 |
| Documents processed | 25279 |
| Process ratio | 222.7% (target ≥90.0%) |
| Rows published (traces) | 1839 |
| Sessions observed | 312 |
| Avg session duration (s) | 1061.788 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13777.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
