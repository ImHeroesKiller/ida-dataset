# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T03:13:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 252 | 1.27 | 70.9 | 319.8 |
| source_discovery | 252 | 3.76 | 186.3 | 947.0 |
| connector | 252 | 88064.99 | 97806.1 | 22192376.7 |
| document_discovery | 252 | 88065.2 | 97806.2 | 22192431.5 |
| document_download | 252 | 239412.59 | 1509355.9 | 60331972.6 |
| extraction | 252 | 92.56 | 274.0 | 23324.9 |
| candidate_validation | 252 | 11.88 | 102.5 | 2994.8 |
| publish_queue | 252 | 11.97 | 102.7 | 3016.5 |
| append_dataset | 252 | 41.4 | 119.7 | 10432.5 |
| export | 252 | 0.35 | 2.1 | 88.7 |
| git_commit | 252 | 0.37 | 15.1 | 93.2 |
| push | 252 | 0.63 | 81.1 | 160.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7362 |
| Documents processed | 18183 |
| Process ratio | 247.0% (target ≥90.0%) |
| Rows published (traces) | 1189 |
| Sessions observed | 280 |
| Avg session duration (s) | 953.432 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.849 |
| Avg connector latency (ms) | 13665.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **247.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
