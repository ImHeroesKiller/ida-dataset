# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T09:26:19+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 266 | 1.25 | 70.9 | 333.0 |
| source_discovery | 266 | 3.71 | 186.3 | 986.4 |
| connector | 266 | 88377.05 | 97806.1 | 23508295.2 |
| document_discovery | 266 | 88377.26 | 97806.2 | 23508351.9 |
| document_download | 266 | 238655.13 | 1509355.9 | 63482265.1 |
| extraction | 266 | 93.03 | 274.0 | 24745.0 |
| candidate_validation | 266 | 12.15 | 102.5 | 3233.2 |
| publish_queue | 266 | 12.24 | 102.7 | 3255.3 |
| append_dataset | 266 | 41.04 | 119.7 | 10916.8 |
| export | 266 | 0.35 | 2.1 | 93.2 |
| git_commit | 266 | 0.37 | 15.1 | 97.8 |
| push | 266 | 0.62 | 81.1 | 164.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7796 |
| Documents processed | 18971 |
| Process ratio | 243.3% (target ≥90.0%) |
| Rows published (traces) | 1259 |
| Sessions observed | 294 |
| Avg session duration (s) | 956.299 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.857 |
| Avg connector latency (ms) | 13776.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **243.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
