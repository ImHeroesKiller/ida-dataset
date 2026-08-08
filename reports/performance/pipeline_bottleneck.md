# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T16:56:35+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 342 | 1.59 | 70.9 | 542.8 |
| source_discovery | 342 | 4.6 | 186.3 | 1574.8 |
| connector | 342 | 89627.92 | 97806.1 | 30652749.0 |
| document_discovery | 342 | 89628.12 | 97806.2 | 30652815.4 |
| document_download | 342 | 231192.38 | 1509355.9 | 79067794.4 |
| extraction | 342 | 96.7 | 274.0 | 33069.7 |
| candidate_validation | 342 | 14.02 | 136.9 | 4794.8 |
| publish_queue | 342 | 14.09 | 136.9 | 4818.5 |
| append_dataset | 342 | 39.31 | 119.7 | 13442.5 |
| export | 342 | 0.35 | 2.1 | 118.8 |
| git_commit | 342 | 0.35 | 15.1 | 121.3 |
| push | 342 | 0.64 | 81.1 | 218.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 10122 |
| Documents processed | 22978 |
| Process ratio | 227.0% (target ≥90.0%) |
| Rows published (traces) | 1639 |
| Sessions observed | 302 |
| Avg session duration (s) | 1065.974 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.977 |
| Avg connector latency (ms) | 13803.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **227.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
