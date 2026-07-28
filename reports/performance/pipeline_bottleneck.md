# Pipeline Bottleneck Analysis

**Generated:** 2026-07-28T02:57:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 210 | 1.33 | 70.9 | 278.4 |
| source_discovery | 210 | 3.94 | 186.3 | 827.3 |
| connector | 210 | 86876.47 | 97806.1 | 18244058.9 |
| document_discovery | 210 | 86876.62 | 97806.2 | 18244089.4 |
| document_download | 210 | 251808.09 | 1509355.9 | 52879698.0 |
| extraction | 210 | 90.04 | 274.0 | 18907.7 |
| candidate_validation | 210 | 10.41 | 37.2 | 2187.1 |
| publish_queue | 210 | 10.53 | 37.4 | 2212.3 |
| append_dataset | 210 | 42.44 | 119.7 | 8911.9 |
| export | 210 | 0.35 | 1.9 | 72.9 |
| git_commit | 210 | 0.31 | 2.1 | 65.4 |
| push | 210 | 0.32 | 0.8 | 66.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6081 |
| Documents processed | 15816 |
| Process ratio | 260.1% (target ≥90.0%) |
| Rows published (traces) | 982 |
| Sessions observed | 238 |
| Avg session duration (s) | 941.311 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.833 |
| Avg connector latency (ms) | 13702.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **260.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
