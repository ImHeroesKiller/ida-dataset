# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T23:22:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 155 | 0.99 | 6.5 | 153.5 |
| source_discovery | 155 | 3.13 | 39.8 | 484.5 |
| connector | 155 | 84346.45 | 97806.1 | 13073700.5 |
| document_discovery | 155 | 84346.61 | 97806.2 | 13073724.2 |
| document_download | 155 | 252974.72 | 1509355.9 | 39211082.2 |
| extraction | 155 | 86.17 | 274.0 | 13356.2 |
| candidate_validation | 155 | 8.96 | 30.0 | 1388.8 |
| publish_queue | 155 | 9.11 | 34.7 | 1412.5 |
| append_dataset | 155 | 43.79 | 119.7 | 6786.7 |
| export | 155 | 0.35 | 1.9 | 54.6 |
| git_commit | 155 | 0.31 | 2.1 | 48.8 |
| push | 155 | 0.31 | 0.8 | 48.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4386 |
| Documents processed | 12474 |
| Process ratio | 284.4% (target ≥90.0%) |
| Rows published (traces) | 707 |
| Sessions observed | 183 |
| Avg session duration (s) | 897.421 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.77 |
| Avg connector latency (ms) | 13902.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **284.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
