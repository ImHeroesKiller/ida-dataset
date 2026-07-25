# Pipeline Bottleneck Analysis

**Generated:** 2026-07-25T08:32:02+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 179 | 0.99 | 6.5 | 177.0 |
| source_discovery | 179 | 3.09 | 39.8 | 553.3 |
| connector | 179 | 85637.88 | 97806.1 | 15329181.0 |
| document_discovery | 179 | 85638.03 | 97806.2 | 15329207.8 |
| document_download | 179 | 254452.92 | 1509355.9 | 45547071.8 |
| extraction | 179 | 87.59 | 274.0 | 15678.7 |
| candidate_validation | 179 | 9.55 | 30.0 | 1709.3 |
| publish_queue | 179 | 9.68 | 34.7 | 1733.3 |
| append_dataset | 179 | 43.18 | 119.7 | 7730.0 |
| export | 179 | 0.35 | 1.9 | 62.9 |
| git_commit | 179 | 0.31 | 2.1 | 55.9 |
| push | 179 | 0.31 | 0.8 | 56.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5130 |
| Documents processed | 13981 |
| Process ratio | 272.5% (target ≥90.0%) |
| Rows published (traces) | 827 |
| Sessions observed | 207 |
| Avg session duration (s) | 921.314 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.802 |
| Avg connector latency (ms) | 13741.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **272.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
