# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T10:58:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 255 | 1.27 | 70.9 | 322.8 |
| source_discovery | 255 | 3.75 | 186.3 | 955.6 |
| connector | 255 | 88135.19 | 97806.1 | 22474473.2 |
| document_discovery | 255 | 88135.41 | 97806.2 | 22474528.4 |
| document_download | 255 | 239296.11 | 1509355.9 | 61020507.0 |
| extraction | 255 | 92.74 | 274.0 | 23648.8 |
| candidate_validation | 255 | 11.95 | 102.5 | 3047.6 |
| publish_queue | 255 | 12.04 | 102.7 | 3069.6 |
| append_dataset | 255 | 41.34 | 119.7 | 10542.7 |
| export | 255 | 0.35 | 2.1 | 89.9 |
| git_commit | 255 | 0.37 | 15.1 | 94.1 |
| push | 255 | 0.63 | 81.1 | 161.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7455 |
| Documents processed | 18350 |
| Process ratio | 246.1% (target ≥90.0%) |
| Rows published (traces) | 1204 |
| Sessions observed | 283 |
| Avg session duration (s) | 954.085 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.851 |
| Avg connector latency (ms) | 13785.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **246.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
