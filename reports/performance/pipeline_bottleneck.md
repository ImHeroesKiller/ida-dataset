# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T07:27:01+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 390 | 1.51 | 70.9 | 589.1 |
| source_discovery | 390 | 4.38 | 186.3 | 1710.0 |
| connector | 390 | 90162.49 | 97806.1 | 35163370.3 |
| document_discovery | 390 | 90162.68 | 97806.2 | 35163443.6 |
| document_download | 390 | 237543.34 | 1509355.9 | 92641902.6 |
| extraction | 390 | 98.54 | 274.0 | 38430.9 |
| candidate_validation | 390 | 15.28 | 149.0 | 5960.7 |
| publish_queue | 390 | 15.35 | 149.1 | 5986.1 |
| append_dataset | 390 | 38.77 | 119.7 | 15119.0 |
| export | 390 | 0.35 | 2.7 | 137.3 |
| git_commit | 390 | 0.35 | 15.1 | 136.6 |
| push | 390 | 0.6 | 81.1 | 233.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11590 |
| Documents processed | 25721 |
| Process ratio | 221.9% (target ≥90.0%) |
| Rows published (traces) | 1879 |
| Sessions observed | 308 |
| Avg session duration (s) | 1062.0 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13903.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
