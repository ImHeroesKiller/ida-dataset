# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T12:04:11+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 138 | 1.0 | 6.5 | 138.3 |
| source_discovery | 138 | 3.16 | 39.8 | 436.4 |
| connector | 138 | 83152.23 | 97806.1 | 11475007.4 |
| document_discovery | 138 | 83152.37 | 97806.2 | 11475026.6 |
| document_download | 138 | 255153.13 | 1509355.9 | 35211131.8 |
| extraction | 138 | 84.87 | 274.0 | 11712.0 |
| candidate_validation | 138 | 8.48 | 30.0 | 1169.8 |
| publish_queue | 138 | 8.64 | 34.7 | 1192.6 |
| append_dataset | 138 | 44.33 | 119.7 | 6118.1 |
| export | 138 | 0.35 | 1.9 | 48.2 |
| git_commit | 138 | 0.32 | 2.1 | 43.7 |
| push | 138 | 0.31 | 0.8 | 43.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3869 |
| Documents processed | 11341 |
| Process ratio | 293.1% (target ≥90.0%) |
| Rows published (traces) | 622 |
| Sessions observed | 166 |
| Avg session duration (s) | 879.223 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.74 |
| Avg connector latency (ms) | 13822.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **293.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
