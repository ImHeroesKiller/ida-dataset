# Pipeline Bottleneck Analysis

**Generated:** 2026-08-05T15:34:07+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 300 | 1.53 | 70.9 | 460.3 |
| source_discovery | 300 | 4.31 | 186.3 | 1293.6 |
| connector | 300 | 89016.35 | 97806.1 | 26704905.8 |
| document_discovery | 300 | 89016.56 | 97806.2 | 26704967.0 |
| document_download | 300 | 234211.41 | 1509355.9 | 70263422.1 |
| extraction | 300 | 94.8 | 274.0 | 28439.0 |
| candidate_validation | 300 | 12.81 | 102.5 | 3843.7 |
| publish_queue | 300 | 12.89 | 102.7 | 3866.2 |
| append_dataset | 300 | 40.13 | 119.7 | 12040.0 |
| export | 300 | 0.35 | 2.1 | 104.1 |
| git_commit | 300 | 0.36 | 15.1 | 108.0 |
| push | 300 | 0.69 | 81.1 | 206.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8840 |
| Documents processed | 20729 |
| Process ratio | 234.5% (target ≥90.0%) |
| Rows published (traces) | 1429 |
| Sessions observed | 328 |
| Avg session duration (s) | 963.076 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.874 |
| Avg connector latency (ms) | 13704.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **234.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
