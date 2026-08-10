# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T13:28:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 377 | 1.53 | 70.9 | 575.6 |
| source_discovery | 377 | 4.43 | 186.3 | 1671.4 |
| connector | 377 | 90031.98 | 97806.1 | 33942057.3 |
| document_discovery | 377 | 90032.17 | 97806.2 | 33942128.8 |
| document_download | 377 | 237312.99 | 1509355.9 | 89466996.7 |
| extraction | 377 | 97.98 | 274.0 | 36940.2 |
| candidate_validation | 377 | 14.99 | 149.0 | 5649.7 |
| publish_queue | 377 | 15.05 | 149.1 | 5674.8 |
| append_dataset | 377 | 38.79 | 119.7 | 14625.3 |
| export | 377 | 0.35 | 2.7 | 133.0 |
| git_commit | 377 | 0.35 | 15.1 | 132.2 |
| push | 377 | 0.61 | 81.1 | 229.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11197 |
| Documents processed | 24973 |
| Process ratio | 223.0% (target ≥90.0%) |
| Rows published (traces) | 1814 |
| Sessions observed | 307 |
| Avg session duration (s) | 1060.296 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13855.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
