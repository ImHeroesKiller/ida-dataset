# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T08:08:26+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 243 | 1.28 | 70.9 | 311.6 |
| source_discovery | 243 | 3.79 | 186.3 | 921.5 |
| connector | 243 | 87847.02 | 97806.1 | 21346825.6 |
| document_discovery | 243 | 87847.24 | 97806.2 | 21346879.2 |
| document_download | 243 | 243155.07 | 1509355.9 | 59086683.1 |
| extraction | 243 | 92.32 | 274.0 | 22434.8 |
| candidate_validation | 243 | 11.62 | 102.5 | 2822.9 |
| publish_queue | 243 | 11.7 | 102.7 | 2844.1 |
| append_dataset | 243 | 41.66 | 119.7 | 10123.4 |
| export | 243 | 0.35 | 1.9 | 84.1 |
| git_commit | 243 | 0.37 | 15.1 | 90.6 |
| push | 243 | 0.65 | 81.1 | 157.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7094 |
| Documents processed | 17680 |
| Process ratio | 249.2% (target ≥90.0%) |
| Rows published (traces) | 1144 |
| Sessions observed | 271 |
| Avg session duration (s) | 952.697 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.843 |
| Avg connector latency (ms) | 13733.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **249.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
