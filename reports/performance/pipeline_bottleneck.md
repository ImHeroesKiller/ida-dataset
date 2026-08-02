# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T15:25:48+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 269 | 1.4 | 70.9 | 376.5 |
| source_discovery | 269 | 4.11 | 186.3 | 1106.6 |
| connector | 269 | 88439.59 | 97806.1 | 23790250.2 |
| document_discovery | 269 | 88439.8 | 97806.2 | 23790307.3 |
| document_download | 269 | 237346.32 | 1509355.9 | 63846159.0 |
| extraction | 269 | 93.15 | 274.0 | 25058.3 |
| candidate_validation | 269 | 12.22 | 102.5 | 3286.0 |
| publish_queue | 269 | 12.3 | 102.7 | 3308.1 |
| append_dataset | 269 | 40.97 | 119.7 | 11021.5 |
| export | 269 | 0.35 | 2.1 | 94.3 |
| git_commit | 269 | 0.37 | 15.1 | 98.7 |
| push | 269 | 0.61 | 81.1 | 165.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7889 |
| Documents processed | 19135 |
| Process ratio | 242.6% (target ≥90.0%) |
| Rows published (traces) | 1274 |
| Sessions observed | 297 |
| Avg session duration (s) | 956.451 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.859 |
| Avg connector latency (ms) | 13702.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **242.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
