# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T22:23:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 229 | 1.3 | 70.9 | 297.1 |
| source_discovery | 229 | 3.85 | 186.3 | 881.1 |
| connector | 229 | 87470.79 | 97806.1 | 20030810.6 |
| document_discovery | 229 | 87470.94 | 97806.2 | 20030844.9 |
| document_download | 229 | 245729.85 | 1509355.9 | 56272135.8 |
| extraction | 229 | 91.57 | 274.0 | 20970.6 |
| candidate_validation | 229 | 10.92 | 37.2 | 2500.6 |
| publish_queue | 229 | 11.01 | 37.4 | 2521.3 |
| append_dataset | 229 | 41.88 | 119.7 | 9590.8 |
| export | 229 | 0.35 | 1.9 | 79.2 |
| git_commit | 229 | 0.31 | 2.1 | 71.3 |
| push | 229 | 0.31 | 0.8 | 71.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6660 |
| Documents processed | 16869 |
| Process ratio | 253.3% (target ≥90.0%) |
| Rows published (traces) | 1074 |
| Sessions observed | 257 |
| Avg session duration (s) | 947.393 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.833 |
| Avg connector latency (ms) | 13871.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **253.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
