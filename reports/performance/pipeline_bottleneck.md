# Pipeline Bottleneck Analysis

**Generated:** 2026-07-16T00:19:20+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 71 | 1.04 | 6.5 | 73.7 |
| source_discovery | 71 | 2.74 | 3.3 | 194.2 |
| connector | 71 | 72902.93 | 97806.1 | 5176108.1 |
| document_discovery | 71 | 72903.07 | 97806.2 | 5176118.0 |
| document_download | 71 | 272472.4 | 1509355.9 | 19345540.6 |
| extraction | 71 | 81.69 | 274.0 | 5800.2 |
| candidate_validation | 71 | 6.65 | 18.7 | 472.0 |
| publish_queue | 71 | 6.92 | 34.7 | 491.2 |
| append_dataset | 71 | 50.55 | 119.7 | 3588.7 |
| export | 71 | 0.34 | 0.6 | 23.9 |
| git_commit | 71 | 0.32 | 2.1 | 23.0 |
| push | 71 | 0.32 | 0.8 | 22.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1832 |
| Documents processed | 7053 |
| Process ratio | 385.0% (target ≥90.0%) |
| Rows published (traces) | 287 |
| Sessions observed | 99 |
| Avg session duration (s) | 749.131 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.469 |
| Avg connector latency (ms) | 13742.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **385.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
