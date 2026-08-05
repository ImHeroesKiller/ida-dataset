# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T00:29:11+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 294 | 1.36 | 70.9 | 400.8 |
| source_discovery | 294 | 4.34 | 186.3 | 1276.6 |
| connector | 294 | 88914.95 | 97806.1 | 26140994.5 |
| document_discovery | 294 | 88915.15 | 97806.2 | 26141054.9 |
| document_download | 294 | 234283.45 | 1509355.9 | 68879335.1 |
| extraction | 294 | 94.19 | 274.0 | 27692.9 |
| candidate_validation | 294 | 12.69 | 102.5 | 3730.9 |
| publish_queue | 294 | 12.77 | 102.7 | 3753.3 |
| append_dataset | 294 | 40.27 | 119.7 | 11839.7 |
| export | 294 | 0.35 | 2.1 | 102.2 |
| git_commit | 294 | 0.36 | 15.1 | 106.2 |
| push | 294 | 0.7 | 81.1 | 204.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8664 |
| Documents processed | 20417 |
| Process ratio | 235.7% (target ≥90.0%) |
| Rows published (traces) | 1399 |
| Sessions observed | 322 |
| Avg session duration (s) | 961.012 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.871 |
| Avg connector latency (ms) | 13859.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **235.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
