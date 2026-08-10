# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T23:52:52+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 386 | 1.52 | 70.9 | 585.0 |
| source_discovery | 386 | 4.4 | 186.3 | 1697.9 |
| connector | 386 | 90124.67 | 97806.1 | 34788123.6 |
| document_discovery | 386 | 90124.86 | 97806.2 | 34788196.5 |
| document_download | 386 | 238182.69 | 1509355.9 | 91938518.9 |
| extraction | 386 | 98.4 | 274.0 | 37982.3 |
| candidate_validation | 386 | 15.19 | 149.0 | 5863.8 |
| publish_queue | 386 | 15.26 | 149.1 | 5889.1 |
| append_dataset | 386 | 38.78 | 119.7 | 14968.2 |
| export | 386 | 0.35 | 2.7 | 136.1 |
| git_commit | 386 | 0.35 | 15.1 | 135.4 |
| push | 386 | 0.6 | 81.1 | 231.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11476 |
| Documents processed | 25494 |
| Process ratio | 222.2% (target ≥90.0%) |
| Rows published (traces) | 1859 |
| Sessions observed | 304 |
| Avg session duration (s) | 1062.602 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 14119.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
