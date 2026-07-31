# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T17:52:39+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 248 | 1.27 | 70.9 | 316.1 |
| source_discovery | 248 | 3.77 | 186.3 | 935.5 |
| connector | 248 | 87970.65 | 97806.1 | 21816720.9 |
| document_discovery | 248 | 87970.87 | 97806.2 | 21816775.1 |
| document_download | 248 | 241062.5 | 1509355.9 | 59783501.2 |
| extraction | 248 | 92.47 | 274.0 | 22932.2 |
| candidate_validation | 248 | 11.79 | 102.5 | 2925.0 |
| publish_queue | 248 | 11.88 | 102.7 | 2946.4 |
| append_dataset | 248 | 41.51 | 119.7 | 10295.1 |
| export | 248 | 0.35 | 2.1 | 87.4 |
| git_commit | 248 | 0.37 | 15.1 | 92.0 |
| push | 248 | 0.64 | 81.1 | 158.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7249 |
| Documents processed | 17968 |
| Process ratio | 247.9% (target ≥90.0%) |
| Rows published (traces) | 1169 |
| Sessions observed | 276 |
| Avg session duration (s) | 953.623 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.846 |
| Avg connector latency (ms) | 13819.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **247.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
