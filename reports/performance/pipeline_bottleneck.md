# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T03:53:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 26 | 0.95 | 1.3 | 24.7 |
| source_discovery | 26 | 2.61 | 3.3 | 67.8 |
| connector | 26 | 39797.7 | 97806.1 | 1034740.1 |
| document_discovery | 26 | 39797.85 | 97806.2 | 1034744.1 |
| document_download | 26 | 201808.58 | 1509355.9 | 5247023.2 |
| extraction | 26 | 50.55 | 109.5 | 1314.3 |
| candidate_validation | 26 | 4.62 | 7.8 | 120.2 |
| publish_queue | 26 | 4.71 | 8.8 | 122.5 |
| append_dataset | 26 | 30.48 | 119.7 | 792.5 |
| export | 26 | 0.32 | 0.6 | 8.3 |
| git_commit | 26 | 0.3 | 0.4 | 7.7 |
| push | 26 | 0.31 | 0.5 | 8.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 487 |
| Documents processed | 1544 |
| Process ratio | 317.0% (target ≥90.0%) |
| Rows published (traces) | 75 |
| Sessions observed | 54 |
| Avg session duration (s) | 403.463 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.7 |
| Avg connector latency (ms) | 13826.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **317.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
