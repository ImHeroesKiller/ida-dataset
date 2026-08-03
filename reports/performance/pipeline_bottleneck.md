# Pipeline Bottleneck Analysis

**Generated:** 2026-08-03T19:10:42+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 281 | 1.38 | 70.9 | 388.8 |
| source_discovery | 281 | 4.15 | 186.3 | 1165.5 |
| connector | 281 | 88678.81 | 97806.1 | 24918746.2 |
| document_discovery | 281 | 88679.02 | 97806.2 | 24918805.1 |
| document_download | 281 | 235951.93 | 1509355.9 | 66302493.5 |
| extraction | 281 | 93.61 | 274.0 | 26304.5 |
| candidate_validation | 281 | 12.47 | 102.5 | 3503.9 |
| publish_queue | 281 | 12.55 | 102.7 | 3526.3 |
| append_dataset | 281 | 40.66 | 119.7 | 11425.6 |
| export | 281 | 0.35 | 2.1 | 98.2 |
| git_commit | 281 | 0.36 | 15.1 | 102.2 |
| push | 281 | 0.6 | 81.1 | 169.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8261 |
| Documents processed | 19745 |
| Process ratio | 239.0% (target ≥90.0%) |
| Rows published (traces) | 1334 |
| Sessions observed | 309 |
| Avg session duration (s) | 958.767 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.865 |
| Avg connector latency (ms) | 13741.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **239.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
