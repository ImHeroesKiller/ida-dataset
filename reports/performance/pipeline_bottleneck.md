# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T03:44:07+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 329 | 1.61 | 70.9 | 530.0 |
| source_discovery | 329 | 4.68 | 186.3 | 1538.4 |
| connector | 329 | 89454.89 | 97806.1 | 29430658.2 |
| document_discovery | 329 | 89455.08 | 97806.2 | 29430722.8 |
| document_download | 329 | 231023.96 | 1509355.9 | 76006883.9 |
| extraction | 329 | 96.31 | 274.0 | 31684.9 |
| candidate_validation | 329 | 13.77 | 136.9 | 4530.9 |
| publish_queue | 329 | 13.84 | 136.9 | 4554.5 |
| append_dataset | 329 | 39.57 | 119.7 | 13017.9 |
| export | 329 | 0.34 | 2.1 | 113.5 |
| git_commit | 329 | 0.35 | 15.1 | 116.7 |
| push | 329 | 0.65 | 81.1 | 214.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9739 |
| Documents processed | 22301 |
| Process ratio | 229.0% (target ≥90.0%) |
| Rows published (traces) | 1574 |
| Sessions observed | 304 |
| Avg session duration (s) | 1065.273 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.964 |
| Avg connector latency (ms) | 13792.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **229.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
