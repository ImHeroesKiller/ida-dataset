# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T21:20:25+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 81 | 1.03 | 6.5 | 83.3 |
| source_discovery | 81 | 2.74 | 3.3 | 222.3 |
| connector | 81 | 75513.57 | 97806.1 | 6116598.9 |
| document_discovery | 81 | 75513.72 | 97806.2 | 6116611.2 |
| document_download | 81 | 265858.93 | 1509355.9 | 21534573.1 |
| extraction | 81 | 82.67 | 274.0 | 6696.6 |
| candidate_validation | 81 | 6.91 | 18.7 | 560.1 |
| publish_queue | 81 | 7.16 | 34.7 | 579.8 |
| append_dataset | 81 | 49.4 | 119.7 | 4001.0 |
| export | 81 | 0.33 | 0.6 | 27.1 |
| git_commit | 81 | 0.32 | 2.1 | 26.2 |
| push | 81 | 0.32 | 0.8 | 25.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2142 |
| Documents processed | 7731 |
| Process ratio | 360.9% (target ≥90.0%) |
| Rows published (traces) | 337 |
| Sessions observed | 109 |
| Avg session duration (s) | 776.037 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.541 |
| Avg connector latency (ms) | 13681.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **360.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
