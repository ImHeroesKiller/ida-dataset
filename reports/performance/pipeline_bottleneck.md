# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T20:11:17+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 323 | 1.62 | 70.9 | 523.6 |
| source_discovery | 323 | 4.71 | 186.3 | 1520.0 |
| connector | 323 | 89371.33 | 97806.1 | 28866938.9 |
| document_discovery | 323 | 89371.53 | 97806.2 | 28867002.6 |
| document_download | 323 | 231923.61 | 1509355.9 | 74911326.5 |
| extraction | 323 | 95.98 | 274.0 | 31002.9 |
| candidate_validation | 323 | 13.65 | 136.9 | 4407.6 |
| publish_queue | 323 | 13.72 | 136.9 | 4430.7 |
| append_dataset | 323 | 39.62 | 119.7 | 12798.3 |
| export | 323 | 0.34 | 2.1 | 111.4 |
| git_commit | 323 | 0.36 | 15.1 | 114.8 |
| push | 323 | 0.66 | 81.1 | 212.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9553 |
| Documents processed | 21951 |
| Process ratio | 229.8% (target ≥90.0%) |
| Rows published (traces) | 1544 |
| Sessions observed | 319 |
| Avg session duration (s) | 1056.614 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.932 |
| Avg connector latency (ms) | 13837.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **229.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
