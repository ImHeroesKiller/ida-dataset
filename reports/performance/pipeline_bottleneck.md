# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T11:15:31+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 64 | 1.05 | 6.5 | 67.3 |
| source_discovery | 64 | 2.73 | 3.3 | 174.5 |
| connector | 64 | 70599.45 | 97806.1 | 4518364.5 |
| document_discovery | 64 | 70599.59 | 97806.2 | 4518373.5 |
| document_download | 64 | 258451.0 | 1509355.9 | 16540863.9 |
| extraction | 64 | 80.08 | 274.0 | 5125.3 |
| candidate_validation | 64 | 6.26 | 9.5 | 400.9 |
| publish_queue | 64 | 6.31 | 9.5 | 403.9 |
| append_dataset | 64 | 49.39 | 119.7 | 3160.7 |
| export | 64 | 0.34 | 0.6 | 21.6 |
| git_commit | 64 | 0.33 | 2.1 | 20.9 |
| push | 64 | 0.32 | 0.8 | 20.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1615 |
| Documents processed | 6226 |
| Process ratio | 385.5% (target ≥90.0%) |
| Rows published (traces) | 252 |
| Sessions observed | 92 |
| Avg session duration (s) | 709.87 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.404 |
| Avg connector latency (ms) | 13870.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **385.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
