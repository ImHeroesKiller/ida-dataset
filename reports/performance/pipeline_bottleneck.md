# Pipeline Bottleneck Analysis

**Generated:** 2026-07-31T04:40:41+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 242 | 1.28 | 70.9 | 310.5 |
| source_discovery | 242 | 3.8 | 186.3 | 918.5 |
| connector | 242 | 87821.33 | 97806.1 | 21252762.0 |
| document_discovery | 242 | 87821.55 | 97806.2 | 21252815.5 |
| document_download | 242 | 243705.09 | 1509355.9 | 58976632.9 |
| extraction | 242 | 92.26 | 274.0 | 22326.1 |
| candidate_validation | 242 | 11.6 | 102.5 | 2806.1 |
| publish_queue | 242 | 11.68 | 102.7 | 2827.2 |
| append_dataset | 242 | 41.68 | 119.7 | 10086.3 |
| export | 242 | 0.35 | 1.9 | 83.7 |
| git_commit | 242 | 0.37 | 15.1 | 90.3 |
| push | 242 | 0.65 | 81.1 | 156.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7063 |
| Documents processed | 17626 |
| Process ratio | 249.6% (target ≥90.0%) |
| Rows published (traces) | 1139 |
| Sessions observed | 270 |
| Avg session duration (s) | 952.607 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.843 |
| Avg connector latency (ms) | 13653.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **249.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
