# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T21:14:03+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 228 | 1.3 | 70.9 | 296.1 |
| source_discovery | 228 | 3.85 | 186.3 | 878.2 |
| connector | 228 | 87441.61 | 97806.1 | 19936686.5 |
| document_discovery | 228 | 87441.76 | 97806.2 | 19936720.7 |
| document_download | 228 | 246262.95 | 1509355.9 | 56147953.5 |
| extraction | 228 | 91.5 | 274.0 | 20862.2 |
| candidate_validation | 228 | 10.89 | 37.2 | 2483.9 |
| publish_queue | 228 | 10.99 | 37.4 | 2504.6 |
| append_dataset | 228 | 41.89 | 119.7 | 9551.2 |
| export | 228 | 0.35 | 1.9 | 78.9 |
| git_commit | 228 | 0.31 | 2.1 | 71.0 |
| push | 228 | 0.31 | 0.8 | 71.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6629 |
| Documents processed | 16807 |
| Process ratio | 253.5% (target ≥90.0%) |
| Rows published (traces) | 1069 |
| Sessions observed | 256 |
| Avg session duration (s) | 947.379 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.833 |
| Avg connector latency (ms) | 13766.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **253.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
