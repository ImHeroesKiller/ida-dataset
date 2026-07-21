# Pipeline Bottleneck Analysis

**Generated:** 2026-07-21T14:14:44+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 139 | 1.0 | 6.5 | 139.2 |
| source_discovery | 139 | 3.16 | 39.8 | 439.3 |
| connector | 139 | 83230.76 | 97806.1 | 11569075.5 |
| document_discovery | 139 | 83230.9 | 97806.2 | 11569094.9 |
| document_download | 139 | 254247.32 | 1509355.9 | 35340376.9 |
| extraction | 139 | 84.97 | 274.0 | 11810.7 |
| candidate_validation | 139 | 8.5 | 30.0 | 1182.0 |
| publish_queue | 139 | 8.67 | 34.7 | 1204.9 |
| append_dataset | 139 | 44.26 | 119.7 | 6152.4 |
| export | 139 | 0.35 | 1.9 | 48.5 |
| git_commit | 139 | 0.32 | 2.1 | 44.0 |
| push | 139 | 0.31 | 0.8 | 43.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 3900 |
| Documents processed | 11392 |
| Process ratio | 292.1% (target ≥90.0%) |
| Rows published (traces) | 627 |
| Sessions observed | 167 |
| Avg session duration (s) | 879.713 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.742 |
| Avg connector latency (ms) | 14304.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **292.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
