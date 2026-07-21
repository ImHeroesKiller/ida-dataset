# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T00:14:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 133 | 1.0 | 6.5 | 133.4 |
| source_discovery | 133 | 3.17 | 39.8 | 421.9 |
| connector | 133 | 82742.24 | 97806.1 | 11004718.5 |
| document_discovery | 133 | 82742.38 | 97806.2 | 11004737.0 |
| document_download | 133 | 258146.77 | 1509355.9 | 34333520.6 |
| extraction | 133 | 84.39 | 274.0 | 11224.3 |
| candidate_validation | 133 | 8.33 | 30.0 | 1108.5 |
| publish_queue | 133 | 8.5 | 34.7 | 1131.0 |
| append_dataset | 133 | 44.57 | 119.7 | 5927.3 |
| export | 133 | 0.35 | 1.9 | 46.5 |
| git_commit | 133 | 0.32 | 2.1 | 42.2 |
| push | 133 | 0.31 | 0.8 | 41.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3714 |
| Documents processed | 11040 |
| Process ratio | 297.3% (target ≥90.0%) |
| Rows published (traces) | 597 |
| Sessions observed | 161 |
| Avg session duration (s) | 875.062 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.73 |
| Avg connector latency (ms) | 13814.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **297.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
