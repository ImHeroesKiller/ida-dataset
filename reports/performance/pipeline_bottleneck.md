# Pipeline Bottleneck Analysis

**Generated:** 2026-07-20T20:39:46+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 131 | 1.0 | 6.5 | 131.4 |
| source_discovery | 131 | 3.18 | 39.8 | 416.3 |
| connector | 131 | 82570.93 | 97806.1 | 10816791.3 |
| document_discovery | 131 | 82571.06 | 97806.2 | 10816809.4 |
| document_download | 131 | 259551.04 | 1509355.9 | 34001186.1 |
| extraction | 131 | 84.27 | 274.0 | 11039.6 |
| candidate_validation | 131 | 8.28 | 30.0 | 1084.9 |
| publish_queue | 131 | 8.45 | 34.7 | 1107.3 |
| append_dataset | 131 | 44.62 | 119.7 | 5844.8 |
| export | 131 | 0.35 | 1.9 | 45.9 |
| git_commit | 131 | 0.32 | 2.1 | 41.6 |
| push | 131 | 0.31 | 0.8 | 40.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3662 |
| Documents processed | 10902 |
| Process ratio | 297.7% (target ≥90.0%) |
| Rows published (traces) | 587 |
| Sessions observed | 159 |
| Avg session duration (s) | 873.459 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.726 |
| Avg connector latency (ms) | 13683.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **297.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
