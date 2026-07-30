# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T22:24:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 240 | 1.29 | 70.9 | 308.5 |
| source_discovery | 240 | 3.8 | 186.3 | 912.6 |
| connector | 240 | 87769.12 | 97806.1 | 21064589.8 |
| document_discovery | 240 | 87769.35 | 97806.2 | 21064643.1 |
| document_download | 240 | 244721.97 | 1509355.9 | 58733272.2 |
| extraction | 240 | 92.15 | 274.0 | 22116.0 |
| candidate_validation | 240 | 11.55 | 102.5 | 2772.3 |
| publish_queue | 240 | 11.64 | 102.7 | 2793.4 |
| append_dataset | 240 | 41.74 | 119.7 | 10016.8 |
| export | 240 | 0.35 | 1.9 | 83.1 |
| git_commit | 240 | 0.37 | 15.1 | 89.7 |
| push | 240 | 0.65 | 81.1 | 156.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7001 |
| Documents processed | 17521 |
| Process ratio | 250.3% (target ≥90.0%) |
| Rows published (traces) | 1129 |
| Sessions observed | 268 |
| Avg session duration (s) | 952.257 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.841 |
| Avg connector latency (ms) | 13696.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **250.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
