# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T20:42:43+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 292 | 1.37 | 70.9 | 398.9 |
| source_discovery | 292 | 4.35 | 186.3 | 1270.8 |
| connector | 292 | 88880.54 | 97806.1 | 25953116.9 |
| document_discovery | 292 | 88880.74 | 97806.2 | 25953177.1 |
| document_download | 292 | 235084.09 | 1509355.9 | 68644555.5 |
| extraction | 292 | 94.08 | 274.0 | 27471.7 |
| candidate_validation | 292 | 12.65 | 102.5 | 3693.0 |
| publish_queue | 292 | 12.72 | 102.7 | 3715.2 |
| append_dataset | 292 | 40.29 | 119.7 | 11765.8 |
| export | 292 | 0.35 | 2.1 | 101.6 |
| git_commit | 292 | 0.36 | 15.1 | 105.6 |
| push | 292 | 0.7 | 81.1 | 204.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8602 |
| Documents processed | 20304 |
| Process ratio | 236.0% (target ≥90.0%) |
| Rows published (traces) | 1389 |
| Sessions observed | 320 |
| Avg session duration (s) | 961.0 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.87 |
| Avg connector latency (ms) | 13809.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **236.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
