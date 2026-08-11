# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T23:00:43+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 401 | 1.5 | 70.9 | 599.6 |
| source_discovery | 401 | 4.34 | 186.3 | 1740.4 |
| connector | 401 | 90270.53 | 97806.1 | 36198482.5 |
| document_discovery | 401 | 90270.72 | 97806.2 | 36198557.2 |
| document_download | 401 | 236367.93 | 1509355.9 | 94783540.5 |
| extraction | 401 | 98.99 | 274.0 | 39693.1 |
| candidate_validation | 401 | 15.48 | 149.0 | 6209.2 |
| publish_queue | 401 | 15.55 | 149.1 | 6235.4 |
| append_dataset | 401 | 38.7 | 119.7 | 15518.9 |
| export | 401 | 0.35 | 2.7 | 140.8 |
| git_commit | 401 | 0.35 | 15.1 | 140.3 |
| push | 401 | 0.59 | 81.1 | 236.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11931 |
| Documents processed | 26381 |
| Process ratio | 221.1% (target ≥90.0%) |
| Rows published (traces) | 1934 |
| Sessions observed | 306 |
| Avg session duration (s) | 1058.281 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13718.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
