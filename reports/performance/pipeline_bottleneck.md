# Pipeline Bottleneck Analysis

**Generated:** 2026-08-09T04:01:19+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 351 | 1.57 | 70.9 | 552.1 |
| source_discovery | 351 | 4.56 | 186.3 | 1600.8 |
| connector | 351 | 89741.18 | 97806.1 | 31499154.6 |
| document_discovery | 351 | 89741.37 | 97806.2 | 31499222.2 |
| document_download | 351 | 232177.19 | 1509355.9 | 81494194.4 |
| extraction | 351 | 97.03 | 274.0 | 34056.3 |
| candidate_validation | 351 | 14.19 | 136.9 | 4979.2 |
| publish_queue | 351 | 14.25 | 136.9 | 5003.3 |
| append_dataset | 351 | 39.17 | 119.7 | 13747.9 |
| export | 351 | 0.35 | 2.1 | 122.0 |
| git_commit | 351 | 0.35 | 15.1 | 124.3 |
| push | 351 | 0.63 | 81.1 | 221.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10401 |
| Documents processed | 23489 |
| Process ratio | 225.8% (target ≥90.0%) |
| Rows published (traces) | 1684 |
| Sessions observed | 302 |
| Avg session duration (s) | 1066.195 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13733.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **225.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
