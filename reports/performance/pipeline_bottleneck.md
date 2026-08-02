# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T17:24:04+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 270 | 1.4 | 70.9 | 377.4 |
| source_discovery | 270 | 4.11 | 186.3 | 1109.6 |
| connector | 270 | 88460.62 | 97806.1 | 23884367.7 |
| document_discovery | 270 | 88460.83 | 97806.2 | 23884425.0 |
| document_download | 270 | 238077.24 | 1509355.9 | 64280855.6 |
| extraction | 270 | 93.18 | 274.0 | 25159.7 |
| candidate_validation | 270 | 12.24 | 102.5 | 3304.6 |
| publish_queue | 270 | 12.32 | 102.7 | 3326.7 |
| append_dataset | 270 | 40.96 | 119.7 | 11059.5 |
| export | 270 | 0.35 | 2.1 | 94.6 |
| git_commit | 270 | 0.37 | 15.1 | 99.0 |
| push | 270 | 0.61 | 81.1 | 165.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7920 |
| Documents processed | 19197 |
| Process ratio | 242.4% (target ≥90.0%) |
| Rows published (traces) | 1279 |
| Sessions observed | 298 |
| Avg session duration (s) | 957.601 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.859 |
| Avg connector latency (ms) | 13847.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **242.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
