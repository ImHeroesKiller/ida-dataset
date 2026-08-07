# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T13:23:28+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 317 | 1.64 | 70.9 | 518.6 |
| source_discovery | 317 | 4.75 | 186.3 | 1504.5 |
| connector | 317 | 89283.52 | 97806.1 | 28302876.3 |
| document_discovery | 317 | 89283.72 | 97806.2 | 28302939.4 |
| document_download | 317 | 232046.75 | 1509355.9 | 73558820.4 |
| extraction | 317 | 95.74 | 274.0 | 30349.4 |
| candidate_validation | 317 | 13.55 | 136.9 | 4294.8 |
| publish_queue | 317 | 13.62 | 136.9 | 4317.7 |
| append_dataset | 317 | 39.81 | 119.7 | 12621.0 |
| export | 317 | 0.35 | 2.1 | 109.5 |
| git_commit | 317 | 0.36 | 15.1 | 113.1 |
| push | 317 | 0.67 | 81.1 | 211.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9367 |
| Documents processed | 21632 |
| Process ratio | 230.9% (target ≥90.0%) |
| Rows published (traces) | 1514 |
| Sessions observed | 313 |
| Avg session duration (s) | 1056.224 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.931 |
| Avg connector latency (ms) | 13782.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **230.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
