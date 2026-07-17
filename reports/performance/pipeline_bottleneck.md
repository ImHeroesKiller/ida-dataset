# Pipeline Bottleneck Analysis

**Generated:** 2026-07-17T15:32:17+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 90 | 1.03 | 6.5 | 92.4 |
| source_discovery | 90 | 2.76 | 3.3 | 248.0 |
| connector | 90 | 77364.54 | 97806.1 | 6962808.5 |
| document_discovery | 90 | 77364.69 | 97806.2 | 6962821.9 |
| document_download | 90 | 274395.25 | 1509355.9 | 24695572.7 |
| extraction | 90 | 83.27 | 274.0 | 7494.2 |
| candidate_validation | 90 | 7.18 | 18.7 | 645.8 |
| publish_queue | 90 | 7.39 | 34.7 | 665.5 |
| append_dataset | 90 | 48.13 | 119.7 | 4332.1 |
| export | 90 | 0.34 | 0.6 | 30.2 |
| git_commit | 90 | 0.32 | 2.1 | 28.9 |
| push | 90 | 0.32 | 0.8 | 28.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2421 |
| Documents processed | 8282 |
| Process ratio | 342.1% (target ≥90.0%) |
| Rows published (traces) | 382 |
| Sessions observed | 118 |
| Avg session duration (s) | 807.763 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.59 |
| Avg connector latency (ms) | 14230.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **342.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
