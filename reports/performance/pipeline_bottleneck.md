# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T16:00:06+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 205 | 0.99 | 6.5 | 203.4 |
| source_discovery | 205 | 3.07 | 39.8 | 629.5 |
| connector | 205 | 86699.93 | 97806.1 | 17773484.9 |
| document_discovery | 205 | 86700.07 | 97806.2 | 17773514.7 |
| document_download | 205 | 254101.72 | 1509355.9 | 52090851.7 |
| extraction | 205 | 89.7 | 274.0 | 18388.0 |
| candidate_validation | 205 | 10.32 | 37.2 | 2115.6 |
| publish_queue | 205 | 10.44 | 37.4 | 2140.3 |
| append_dataset | 205 | 42.56 | 119.7 | 8723.8 |
| export | 205 | 0.35 | 1.9 | 71.4 |
| git_commit | 205 | 0.31 | 2.1 | 64.0 |
| push | 205 | 0.32 | 0.8 | 64.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5926 |
| Documents processed | 15517 |
| Process ratio | 261.8% (target ≥90.0%) |
| Rows published (traces) | 957 |
| Sessions observed | 233 |
| Avg session duration (s) | 940.064 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.828 |
| Avg connector latency (ms) | 13834.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **261.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
