# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T06:07:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 331 | 1.61 | 70.9 | 531.7 |
| source_discovery | 331 | 4.66 | 186.3 | 1543.5 |
| connector | 331 | 89481.02 | 97806.1 | 29618217.8 |
| document_discovery | 331 | 89481.22 | 97806.2 | 29618282.7 |
| document_download | 331 | 231659.61 | 1509355.9 | 76679329.3 |
| extraction | 331 | 96.34 | 274.0 | 31887.4 |
| candidate_validation | 331 | 13.8 | 136.9 | 4567.3 |
| publish_queue | 331 | 13.87 | 136.9 | 4590.9 |
| append_dataset | 331 | 39.52 | 119.7 | 13080.1 |
| export | 331 | 0.34 | 2.1 | 114.1 |
| git_commit | 331 | 0.35 | 15.1 | 117.3 |
| push | 331 | 0.65 | 81.1 | 215.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9801 |
| Documents processed | 22425 |
| Process ratio | 228.8% (target ≥90.0%) |
| Rows published (traces) | 1584 |
| Sessions observed | 306 |
| Avg session duration (s) | 1065.948 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.964 |
| Avg connector latency (ms) | 13792.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **228.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
