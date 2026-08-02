# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T19:29:39+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 271 | 1.4 | 70.9 | 378.2 |
| source_discovery | 271 | 4.19 | 186.3 | 1136.2 |
| connector | 271 | 88480.7 | 97806.1 | 23978270.5 |
| document_discovery | 271 | 88480.91 | 97806.2 | 23978327.9 |
| document_download | 271 | 238943.74 | 1509355.9 | 64753752.6 |
| extraction | 271 | 93.14 | 274.0 | 25241.9 |
| candidate_validation | 271 | 12.25 | 102.5 | 3319.1 |
| publish_queue | 271 | 12.33 | 102.7 | 3341.2 |
| append_dataset | 271 | 40.91 | 119.7 | 11086.0 |
| export | 271 | 0.35 | 2.1 | 94.9 |
| git_commit | 271 | 0.37 | 15.1 | 99.2 |
| push | 271 | 0.61 | 81.1 | 165.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7951 |
| Documents processed | 19248 |
| Process ratio | 242.1% (target ≥90.0%) |
| Rows published (traces) | 1284 |
| Sessions observed | 299 |
| Avg session duration (s) | 958.856 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.86 |
| Avg connector latency (ms) | 13778.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **242.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
