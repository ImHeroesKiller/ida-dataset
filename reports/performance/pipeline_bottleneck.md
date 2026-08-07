# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T17:18:26+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 320 | 1.63 | 70.9 | 521.5 |
| source_discovery | 320 | 4.73 | 186.3 | 1512.9 |
| connector | 320 | 89327.9 | 97806.1 | 28584929.2 |
| document_discovery | 320 | 89328.1 | 97806.2 | 28584992.6 |
| document_download | 320 | 232514.85 | 1509355.9 | 74404752.7 |
| extraction | 320 | 95.82 | 274.0 | 30662.5 |
| candidate_validation | 320 | 13.6 | 136.9 | 4352.2 |
| publish_queue | 320 | 13.67 | 136.9 | 4375.2 |
| append_dataset | 320 | 39.75 | 119.7 | 12718.8 |
| export | 320 | 0.34 | 2.1 | 110.4 |
| git_commit | 320 | 0.36 | 15.1 | 114.0 |
| push | 320 | 0.66 | 81.1 | 212.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9460 |
| Documents processed | 21796 |
| Process ratio | 230.4% (target ≥90.0%) |
| Rows published (traces) | 1529 |
| Sessions observed | 316 |
| Avg session duration (s) | 1056.946 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.932 |
| Avg connector latency (ms) | 13727.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **230.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
