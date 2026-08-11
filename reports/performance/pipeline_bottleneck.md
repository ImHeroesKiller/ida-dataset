# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T09:16:57+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 391 | 1.51 | 70.9 | 590.2 |
| source_discovery | 391 | 4.38 | 186.3 | 1712.9 |
| connector | 391 | 90171.76 | 97806.1 | 35257157.5 |
| document_discovery | 391 | 90171.95 | 97806.2 | 35257230.9 |
| document_download | 391 | 237203.94 | 1509355.9 | 92746739.1 |
| extraction | 391 | 98.59 | 274.0 | 38547.2 |
| candidate_validation | 391 | 15.3 | 149.0 | 5983.8 |
| publish_queue | 391 | 15.37 | 149.1 | 6009.2 |
| append_dataset | 391 | 38.77 | 119.7 | 15159.2 |
| export | 391 | 0.35 | 2.7 | 137.6 |
| git_commit | 391 | 0.35 | 15.1 | 136.9 |
| push | 391 | 0.6 | 81.1 | 233.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11621 |
| Documents processed | 25783 |
| Process ratio | 221.9% (target ≥90.0%) |
| Rows published (traces) | 1884 |
| Sessions observed | 309 |
| Avg session duration (s) | 1061.641 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13848.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
