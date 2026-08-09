# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T17:55:50+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 364 | 1.55 | 70.9 | 564.3 |
| source_discovery | 364 | 4.5 | 186.3 | 1636.9 |
| connector | 364 | 89890.77 | 97806.1 | 32720240.7 |
| document_discovery | 364 | 89890.96 | 97806.2 | 32720310.8 |
| document_download | 364 | 232578.37 | 1509355.9 | 84658526.7 |
| extraction | 364 | 97.36 | 274.0 | 35440.7 |
| candidate_validation | 364 | 14.43 | 136.9 | 5252.2 |
| publish_queue | 364 | 14.5 | 136.9 | 5276.5 |
| append_dataset | 364 | 39.01 | 119.7 | 14200.3 |
| export | 364 | 0.35 | 2.1 | 125.9 |
| git_commit | 364 | 0.35 | 15.1 | 128.0 |
| push | 364 | 0.62 | 81.1 | 225.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10804 |
| Documents processed | 24243 |
| Process ratio | 224.4% (target ≥90.0%) |
| Rows published (traces) | 1749 |
| Sessions observed | 304 |
| Avg session duration (s) | 1061.618 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13693.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **224.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
