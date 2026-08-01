# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T08:43:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 254 | 1.27 | 70.9 | 321.9 |
| source_discovery | 254 | 3.75 | 186.3 | 952.8 |
| connector | 254 | 88111.74 | 97806.1 | 22380381.2 |
| document_discovery | 254 | 88111.95 | 97806.2 | 22380436.2 |
| document_download | 254 | 239335.94 | 1509355.9 | 60791329.5 |
| extraction | 254 | 92.68 | 274.0 | 23541.2 |
| candidate_validation | 254 | 11.93 | 102.5 | 3030.0 |
| publish_queue | 254 | 12.02 | 102.7 | 3051.9 |
| append_dataset | 254 | 41.36 | 119.7 | 10506.3 |
| export | 254 | 0.35 | 2.1 | 89.4 |
| git_commit | 254 | 0.37 | 15.1 | 93.8 |
| push | 254 | 0.63 | 81.1 | 160.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7424 |
| Documents processed | 18296 |
| Process ratio | 246.4% (target ≥90.0%) |
| Rows published (traces) | 1199 |
| Sessions observed | 282 |
| Avg session duration (s) | 954.39 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.85 |
| Avg connector latency (ms) | 13769.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **246.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
