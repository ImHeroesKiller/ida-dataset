# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T20:37:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 239 | 1.29 | 70.9 | 307.5 |
| source_discovery | 239 | 3.81 | 186.3 | 909.8 |
| connector | 239 | 87742.7 | 97806.1 | 20970504.6 |
| document_discovery | 239 | 87742.92 | 97806.2 | 20970557.7 |
| document_download | 239 | 243879.67 | 1509355.9 | 58287240.6 |
| extraction | 239 | 92.11 | 274.0 | 22015.1 |
| candidate_validation | 239 | 11.54 | 102.5 | 2758.2 |
| publish_queue | 239 | 11.63 | 102.7 | 2779.3 |
| append_dataset | 239 | 41.79 | 119.7 | 9988.9 |
| export | 239 | 0.35 | 1.9 | 82.8 |
| git_commit | 239 | 0.37 | 15.1 | 89.5 |
| push | 239 | 0.65 | 81.1 | 155.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6970 |
| Documents processed | 17459 |
| Process ratio | 250.5% (target ≥90.0%) |
| Rows published (traces) | 1124 |
| Sessions observed | 267 |
| Avg session duration (s) | 951.015 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.841 |
| Avg connector latency (ms) | 13795.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **250.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
