# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T14:56:13+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 361 | 1.55 | 70.9 | 561.3 |
| source_discovery | 361 | 4.51 | 186.3 | 1628.3 |
| connector | 361 | 89857.89 | 97806.1 | 32438697.2 |
| document_discovery | 361 | 89858.08 | 97806.2 | 32438766.3 |
| document_download | 361 | 232212.4 | 1509355.9 | 83828675.5 |
| extraction | 361 | 97.31 | 274.0 | 35128.3 |
| candidate_validation | 361 | 14.36 | 136.9 | 5185.2 |
| publish_queue | 361 | 14.43 | 136.9 | 5209.5 |
| append_dataset | 361 | 39.02 | 119.7 | 14087.2 |
| export | 361 | 0.35 | 2.1 | 124.9 |
| git_commit | 361 | 0.35 | 15.1 | 127.1 |
| push | 361 | 0.62 | 81.1 | 224.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10711 |
| Documents processed | 24068 |
| Process ratio | 224.7% (target ≥90.0%) |
| Rows published (traces) | 1734 |
| Sessions observed | 301 |
| Avg session duration (s) | 1061.166 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13691.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **224.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
