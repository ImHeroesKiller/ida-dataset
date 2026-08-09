# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T19:00:24+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 365 | 1.55 | 70.9 | 565.3 |
| source_discovery | 365 | 4.49 | 186.3 | 1639.9 |
| connector | 365 | 89902.53 | 97806.1 | 32814424.0 |
| document_discovery | 365 | 89902.72 | 97806.2 | 32814494.2 |
| document_download | 365 | 233370.9 | 1509355.9 | 85180379.0 |
| extraction | 365 | 97.38 | 274.0 | 35545.1 |
| candidate_validation | 365 | 14.45 | 136.9 | 5275.2 |
| publish_queue | 365 | 14.52 | 136.9 | 5299.5 |
| append_dataset | 365 | 39.01 | 119.7 | 14239.7 |
| export | 365 | 0.35 | 2.1 | 126.2 |
| git_commit | 365 | 0.35 | 15.1 | 128.3 |
| push | 365 | 0.62 | 81.1 | 225.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10835 |
| Documents processed | 24305 |
| Process ratio | 224.3% (target ≥90.0%) |
| Rows published (traces) | 1754 |
| Sessions observed | 305 |
| Avg session duration (s) | 1062.557 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13789.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **224.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
