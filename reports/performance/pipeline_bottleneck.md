# Pipeline Bottleneck Analysis

**Generated:** 2026-07-12T16:24:07+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 34 | 1.14 | 6.5 | 38.6 |
| source_discovery | 34 | 2.68 | 3.3 | 91.0 |
| connector | 34 | 49964.17 | 97806.1 | 1698781.9 |
| document_discovery | 34 | 49964.32 | 97806.2 | 1698786.8 |
| document_download | 34 | 202426.17 | 1509355.9 | 6882489.9 |
| extraction | 34 | 60.53 | 109.5 | 2058.0 |
| candidate_validation | 34 | 5.09 | 8.7 | 173.2 |
| publish_queue | 34 | 5.16 | 8.8 | 175.6 |
| append_dataset | 34 | 38.91 | 119.7 | 1323.0 |
| export | 34 | 0.32 | 0.6 | 11.0 |
| git_commit | 34 | 0.3 | 0.4 | 10.1 |
| push | 34 | 0.31 | 0.6 | 10.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 725 |
| Documents processed | 2571 |
| Process ratio | 354.6% (target ≥90.0%) |
| Rows published (traces) | 110 |
| Sessions observed | 62 |
| Avg session duration (s) | 482.984 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.037 |
| Avg connector latency (ms) | 13660.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **354.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
