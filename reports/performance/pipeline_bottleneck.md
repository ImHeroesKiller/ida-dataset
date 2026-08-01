# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T16:17:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 258 | 1.26 | 70.9 | 325.6 |
| source_discovery | 258 | 3.74 | 186.3 | 964.0 |
| connector | 258 | 88203.42 | 97806.1 | 22756482.7 |
| document_discovery | 258 | 88203.64 | 97806.2 | 22756538.2 |
| document_download | 258 | 239432.31 | 1509355.9 | 61773535.8 |
| extraction | 258 | 92.8 | 274.0 | 23942.5 |
| candidate_validation | 258 | 12.0 | 102.5 | 3096.3 |
| publish_queue | 258 | 12.09 | 102.7 | 3118.2 |
| append_dataset | 258 | 41.25 | 119.7 | 10641.4 |
| export | 258 | 0.35 | 2.1 | 90.9 |
| git_commit | 258 | 0.37 | 15.1 | 95.4 |
| push | 258 | 0.63 | 81.1 | 162.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7548 |
| Documents processed | 18517 |
| Process ratio | 245.3% (target ≥90.0%) |
| Rows published (traces) | 1219 |
| Sessions observed | 286 |
| Avg session duration (s) | 954.636 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.853 |
| Avg connector latency (ms) | 13699.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **245.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
