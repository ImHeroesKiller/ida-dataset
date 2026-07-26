# Pipeline Bottleneck Analysis

**Generated:** 2026-07-26T21:20:27+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 198 | 0.99 | 6.5 | 196.0 |
| source_discovery | 198 | 3.07 | 39.8 | 608.3 |
| connector | 198 | 86439.85 | 97806.1 | 17115089.4 |
| document_discovery | 198 | 86439.99 | 97806.2 | 17115118.3 |
| document_download | 198 | 253727.6 | 1509355.9 | 50238063.9 |
| extraction | 198 | 89.14 | 274.0 | 17649.1 |
| candidate_validation | 198 | 10.14 | 37.2 | 2008.1 |
| publish_queue | 198 | 10.27 | 37.4 | 2032.6 |
| append_dataset | 198 | 42.68 | 119.7 | 8450.9 |
| export | 198 | 0.35 | 1.9 | 69.2 |
| git_commit | 198 | 0.31 | 2.1 | 61.7 |
| push | 198 | 0.32 | 0.8 | 62.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5709 |
| Documents processed | 15094 |
| Process ratio | 264.4% (target ≥90.0%) |
| Rows published (traces) | 922 |
| Sessions observed | 226 |
| Avg session duration (s) | 935.137 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.822 |
| Avg connector latency (ms) | 13721.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **264.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
