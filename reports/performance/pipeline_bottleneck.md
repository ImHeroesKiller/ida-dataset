# Pipeline Bottleneck Analysis

**Generated:** 2026-08-13T00:03:57+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 418 | 1.48 | 70.9 | 617.0 |
| source_discovery | 418 | 4.28 | 186.3 | 1788.6 |
| connector | 418 | 90421.71 | 97806.1 | 37796276.5 |
| document_discovery | 418 | 90422.04 | 97806.2 | 37796413.0 |
| document_download | 418 | 234826.7 | 1509355.9 | 98157559.1 |
| extraction | 418 | 99.58 | 274.0 | 41625.4 |
| candidate_validation | 418 | 15.84 | 149.0 | 6622.3 |
| publish_queue | 418 | 15.91 | 149.1 | 6649.1 |
| append_dataset | 418 | 38.55 | 119.7 | 16113.4 |
| export | 418 | 0.35 | 2.7 | 146.0 |
| git_commit | 418 | 0.43 | 36.1 | 181.4 |
| push | 418 | 0.63 | 81.1 | 264.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12448 |
| Documents processed | 27359 |
| Process ratio | 219.8% (target ≥90.0%) |
| Rows published (traces) | 2019 |
| Sessions observed | 309 |
| Avg session duration (s) | 1056.485 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13778.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **219.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
