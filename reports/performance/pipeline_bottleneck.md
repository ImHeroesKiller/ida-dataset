# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T00:58:10+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 310 | 1.52 | 70.9 | 470.4 |
| source_discovery | 310 | 4.27 | 186.3 | 1322.6 |
| connector | 310 | 89178.31 | 97806.1 | 27645276.3 |
| document_discovery | 310 | 89178.51 | 97806.2 | 27645338.6 |
| document_download | 310 | 234285.58 | 1509355.9 | 72628529.6 |
| extraction | 310 | 95.29 | 274.0 | 29540.8 |
| candidate_validation | 310 | 13.04 | 102.5 | 4041.8 |
| publish_queue | 310 | 13.11 | 102.7 | 4064.7 |
| append_dataset | 310 | 39.95 | 119.7 | 12385.7 |
| export | 310 | 0.35 | 2.1 | 107.4 |
| git_commit | 310 | 0.36 | 15.1 | 111.2 |
| push | 310 | 0.68 | 81.1 | 209.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9150 |
| Documents processed | 21243 |
| Process ratio | 232.2% (target ≥90.0%) |
| Rows published (traces) | 1479 |
| Sessions observed | 306 |
| Avg session duration (s) | 1058.333 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.929 |
| Avg connector latency (ms) | 13664.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **232.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
