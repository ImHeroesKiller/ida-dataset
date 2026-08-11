# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T05:27:39+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 389 | 1.51 | 70.9 | 588.0 |
| source_discovery | 389 | 4.39 | 186.3 | 1707.1 |
| connector | 389 | 90153.41 | 97806.1 | 35069675.3 |
| document_discovery | 389 | 90153.6 | 97806.2 | 35069748.5 |
| document_download | 389 | 237815.01 | 1509355.9 | 92510038.3 |
| extraction | 389 | 98.51 | 274.0 | 38319.0 |
| candidate_validation | 389 | 15.26 | 149.0 | 5937.4 |
| publish_queue | 389 | 15.33 | 149.1 | 5962.8 |
| append_dataset | 389 | 38.76 | 119.7 | 15079.0 |
| export | 389 | 0.35 | 2.7 | 137.0 |
| git_commit | 389 | 0.35 | 15.1 | 136.3 |
| push | 389 | 0.6 | 81.1 | 232.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11559 |
| Documents processed | 25659 |
| Process ratio | 222.0% (target ≥90.0%) |
| Rows published (traces) | 1874 |
| Sessions observed | 307 |
| Avg session duration (s) | 1062.257 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13792.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
