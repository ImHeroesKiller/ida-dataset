# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T03:50:17+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 134 | 1.0 | 6.5 | 134.2 |
| source_discovery | 134 | 3.17 | 39.8 | 424.7 |
| connector | 134 | 82825.85 | 97806.1 | 11098663.5 |
| document_discovery | 134 | 82825.99 | 97806.2 | 11098682.1 |
| document_download | 134 | 257120.77 | 1509355.9 | 34454183.5 |
| extraction | 134 | 84.49 | 274.0 | 11322.0 |
| candidate_validation | 134 | 8.36 | 30.0 | 1120.5 |
| publish_queue | 134 | 8.53 | 34.7 | 1143.1 |
| append_dataset | 134 | 44.5 | 119.7 | 5963.1 |
| export | 134 | 0.35 | 1.9 | 46.9 |
| git_commit | 134 | 0.32 | 2.1 | 42.5 |
| push | 134 | 0.31 | 0.8 | 41.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3745 |
| Documents processed | 11091 |
| Process ratio | 296.2% (target ≥90.0%) |
| Rows published (traces) | 602 |
| Sessions observed | 162 |
| Avg session duration (s) | 875.568 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.732 |
| Avg connector latency (ms) | 13720.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **296.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
