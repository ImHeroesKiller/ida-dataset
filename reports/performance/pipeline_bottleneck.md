# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T08:08:51+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 374 | 1.53 | 70.9 | 572.8 |
| source_discovery | 374 | 4.45 | 186.3 | 1663.2 |
| connector | 374 | 90001.08 | 97806.1 | 33660402.4 |
| document_discovery | 374 | 90001.27 | 97806.2 | 33660473.5 |
| document_download | 374 | 237100.59 | 1509355.9 | 88675622.1 |
| extraction | 374 | 97.82 | 274.0 | 36583.0 |
| candidate_validation | 374 | 14.93 | 149.0 | 5584.2 |
| publish_queue | 374 | 15.0 | 149.1 | 5609.2 |
| append_dataset | 374 | 38.85 | 119.7 | 14528.1 |
| export | 374 | 0.35 | 2.1 | 129.7 |
| git_commit | 374 | 0.35 | 15.1 | 131.4 |
| push | 374 | 0.61 | 81.1 | 228.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11114 |
| Documents processed | 24819 |
| Process ratio | 223.3% (target ≥90.0%) |
| Rows published (traces) | 1799 |
| Sessions observed | 304 |
| Avg session duration (s) | 1059.845 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13651.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **223.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
