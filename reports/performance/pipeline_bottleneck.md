# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T15:18:51+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 318 | 1.63 | 70.9 | 519.7 |
| source_discovery | 318 | 4.74 | 186.3 | 1507.5 |
| connector | 318 | 89297.75 | 97806.1 | 28396685.8 |
| document_discovery | 318 | 89297.95 | 97806.2 | 28396749.0 |
| document_download | 318 | 231682.69 | 1509355.9 | 73675096.2 |
| extraction | 318 | 95.8 | 274.0 | 30464.2 |
| candidate_validation | 318 | 13.57 | 136.9 | 4315.2 |
| publish_queue | 318 | 13.64 | 136.9 | 4338.1 |
| append_dataset | 318 | 39.8 | 119.7 | 12655.6 |
| export | 318 | 0.35 | 2.1 | 109.8 |
| git_commit | 318 | 0.36 | 15.1 | 113.4 |
| push | 318 | 0.67 | 81.1 | 211.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9398 |
| Documents processed | 21683 |
| Process ratio | 230.7% (target ≥90.0%) |
| Rows published (traces) | 1519 |
| Sessions observed | 314 |
| Avg session duration (s) | 1055.92 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.931 |
| Avg connector latency (ms) | 13701.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **230.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
