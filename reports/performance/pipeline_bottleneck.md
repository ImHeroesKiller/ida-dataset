# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T11:47:22+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 358 | 1.56 | 70.9 | 558.9 |
| source_discovery | 358 | 4.53 | 186.3 | 1620.6 |
| connector | 358 | 89824.86 | 97806.1 | 32157299.9 |
| document_discovery | 358 | 89825.05 | 97806.2 | 32157368.7 |
| document_download | 358 | 231677.76 | 1509355.9 | 82940638.0 |
| extraction | 358 | 97.33 | 274.0 | 34842.5 |
| candidate_validation | 358 | 14.32 | 136.9 | 5127.6 |
| publish_queue | 358 | 14.39 | 136.9 | 5151.8 |
| append_dataset | 358 | 39.09 | 119.7 | 13994.2 |
| export | 358 | 0.35 | 2.1 | 124.2 |
| git_commit | 358 | 0.35 | 15.1 | 126.3 |
| push | 358 | 0.62 | 81.1 | 223.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10618 |
| Documents processed | 23893 |
| Process ratio | 225.0% (target ≥90.0%) |
| Rows published (traces) | 1719 |
| Sessions observed | 309 |
| Avg session duration (s) | 1065.735 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13685.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
