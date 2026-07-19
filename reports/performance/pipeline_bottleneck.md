# Pipeline Bottleneck Analysis

**Generated:** 2026-07-19T08:46:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 112 | 1.01 | 6.5 | 112.7 |
| source_discovery | 112 | 3.09 | 39.8 | 346.6 |
| connector | 112 | 80638.11 | 97806.1 | 9031468.6 |
| document_discovery | 112 | 80638.25 | 97806.2 | 9031484.3 |
| document_download | 112 | 266665.32 | 1509355.9 | 29866516.1 |
| extraction | 112 | 81.99 | 274.0 | 9182.8 |
| candidate_validation | 112 | 7.85 | 30.0 | 879.1 |
| publish_queue | 112 | 8.05 | 34.7 | 901.1 |
| append_dataset | 112 | 45.65 | 119.7 | 5112.3 |
| export | 112 | 0.34 | 0.7 | 37.6 |
| git_commit | 112 | 0.32 | 2.1 | 35.7 |
| push | 112 | 0.31 | 0.8 | 35.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3083 |
| Documents processed | 9672 |
| Process ratio | 313.7% (target ≥90.0%) |
| Rows published (traces) | 492 |
| Sessions observed | 140 |
| Avg session duration (s) | 848.893 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.676 |
| Avg connector latency (ms) | 13806.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **313.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
