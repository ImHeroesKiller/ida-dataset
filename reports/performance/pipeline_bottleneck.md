# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T14:04:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 339 | 1.59 | 70.9 | 539.6 |
| source_discovery | 339 | 4.62 | 186.3 | 1565.9 |
| connector | 339 | 89589.33 | 97806.1 | 30370782.3 |
| document_discovery | 339 | 89589.52 | 97806.2 | 30370848.2 |
| document_download | 339 | 231911.61 | 1509355.9 | 78618034.3 |
| extraction | 339 | 96.61 | 274.0 | 32750.0 |
| candidate_validation | 339 | 13.96 | 136.9 | 4733.1 |
| publish_queue | 339 | 14.03 | 136.9 | 4756.9 |
| append_dataset | 339 | 39.41 | 119.7 | 13360.3 |
| export | 339 | 0.34 | 2.1 | 116.5 |
| git_commit | 339 | 0.36 | 15.1 | 120.5 |
| push | 339 | 0.64 | 81.1 | 217.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10039 |
| Documents processed | 22861 |
| Process ratio | 227.7% (target ≥90.0%) |
| Rows published (traces) | 1624 |
| Sessions observed | 314 |
| Avg session duration (s) | 1066.863 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.965 |
| Avg connector latency (ms) | 13869.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **227.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
