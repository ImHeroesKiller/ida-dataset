# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T17:43:34+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 152 | 0.99 | 6.5 | 150.7 |
| source_discovery | 152 | 3.13 | 39.8 | 475.9 |
| connector | 152 | 84154.77 | 97806.1 | 12791525.3 |
| document_discovery | 152 | 84154.92 | 97806.2 | 12791548.6 |
| document_download | 152 | 251798.14 | 1509355.9 | 38273316.6 |
| extraction | 152 | 86.05 | 274.0 | 13079.5 |
| candidate_validation | 152 | 8.88 | 30.0 | 1349.8 |
| publish_queue | 152 | 9.04 | 34.7 | 1373.4 |
| append_dataset | 152 | 43.95 | 119.7 | 6679.7 |
| export | 152 | 0.35 | 1.9 | 52.6 |
| git_commit | 152 | 0.32 | 2.1 | 47.9 |
| push | 152 | 0.31 | 0.8 | 47.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4303 |
| Documents processed | 12308 |
| Process ratio | 286.0% (target ≥90.0%) |
| Rows published (traces) | 692 |
| Sessions observed | 180 |
| Avg session duration (s) | 893.267 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.766 |
| Avg connector latency (ms) | 13676.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **286.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
