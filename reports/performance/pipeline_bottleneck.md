# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T05:06:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 404 | 1.49 | 70.9 | 602.7 |
| source_discovery | 404 | 4.33 | 186.3 | 1749.6 |
| connector | 404 | 90299.08 | 97806.1 | 36480829.2 |
| document_discovery | 404 | 90299.27 | 97806.2 | 36480904.2 |
| document_download | 404 | 235878.5 | 1509355.9 | 95294915.1 |
| extraction | 404 | 99.16 | 274.0 | 40061.9 |
| candidate_validation | 404 | 15.56 | 149.0 | 6285.1 |
| publish_queue | 404 | 15.62 | 149.1 | 6311.4 |
| append_dataset | 404 | 38.7 | 119.7 | 15636.2 |
| export | 404 | 0.35 | 2.7 | 141.7 |
| git_commit | 404 | 0.35 | 15.1 | 141.3 |
| push | 404 | 0.59 | 81.1 | 237.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12024 |
| Documents processed | 26567 |
| Process ratio | 220.9% (target ≥90.0%) |
| Rows published (traces) | 1949 |
| Sessions observed | 309 |
| Avg session duration (s) | 1057.971 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13862.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
