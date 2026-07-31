# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T19:49:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 249 | 1.27 | 70.9 | 317.1 |
| source_discovery | 249 | 3.77 | 186.3 | 938.3 |
| connector | 249 | 87995.07 | 97806.1 | 21910772.9 |
| document_discovery | 249 | 87995.29 | 97806.2 | 21910827.3 |
| document_download | 249 | 240538.8 | 1509355.9 | 59894160.7 |
| extraction | 249 | 92.51 | 274.0 | 23034.7 |
| candidate_validation | 249 | 11.82 | 102.5 | 2942.7 |
| publish_queue | 249 | 11.91 | 102.7 | 2964.4 |
| append_dataset | 249 | 41.49 | 119.7 | 10330.2 |
| export | 249 | 0.35 | 2.1 | 87.7 |
| git_commit | 249 | 0.37 | 15.1 | 92.3 |
| push | 249 | 0.64 | 81.1 | 158.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7280 |
| Documents processed | 18019 |
| Process ratio | 247.5% (target ≥90.0%) |
| Rows published (traces) | 1174 |
| Sessions observed | 277 |
| Avg session duration (s) | 952.906 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.847 |
| Avg connector latency (ms) | 13698.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **247.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
