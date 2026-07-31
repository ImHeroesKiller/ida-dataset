# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T09:27:50+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 244 | 1.28 | 70.9 | 312.5 |
| source_discovery | 244 | 3.79 | 186.3 | 924.3 |
| connector | 244 | 87872.01 | 97806.1 | 21440770.5 |
| document_discovery | 244 | 87872.23 | 97806.2 | 21440824.3 |
| document_download | 244 | 242679.34 | 1509355.9 | 59213758.1 |
| extraction | 244 | 92.35 | 274.0 | 22532.2 |
| candidate_validation | 244 | 11.64 | 102.5 | 2840.0 |
| publish_queue | 244 | 11.73 | 102.7 | 2861.2 |
| append_dataset | 244 | 41.63 | 119.7 | 10157.9 |
| export | 244 | 0.35 | 1.9 | 84.4 |
| git_commit | 244 | 0.37 | 15.1 | 90.9 |
| push | 244 | 0.64 | 81.1 | 157.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7125 |
| Documents processed | 17731 |
| Process ratio | 248.9% (target ≥90.0%) |
| Rows published (traces) | 1149 |
| Sessions observed | 272 |
| Avg session duration (s) | 952.779 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.844 |
| Avg connector latency (ms) | 13799.6 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **248.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
