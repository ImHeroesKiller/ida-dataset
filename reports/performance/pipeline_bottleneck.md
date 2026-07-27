# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T05:00:35+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 201 | 0.99 | 6.5 | 199.0 |
| source_discovery | 201 | 3.07 | 39.8 | 616.9 |
| connector | 201 | 86552.41 | 97806.1 | 17397034.6 |
| document_discovery | 201 | 86552.56 | 97806.2 | 17397064.0 |
| document_download | 201 | 254217.2 | 1509355.9 | 51097656.8 |
| extraction | 201 | 89.38 | 274.0 | 17965.9 |
| candidate_validation | 201 | 10.22 | 37.2 | 2054.2 |
| publish_queue | 201 | 10.34 | 37.4 | 2078.9 |
| append_dataset | 201 | 42.62 | 119.7 | 8565.8 |
| export | 201 | 0.35 | 1.9 | 70.1 |
| git_commit | 201 | 0.31 | 2.1 | 62.8 |
| push | 201 | 0.32 | 0.8 | 63.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5802 |
| Documents processed | 15269 |
| Process ratio | 263.2% (target ≥90.0%) |
| Rows published (traces) | 937 |
| Sessions observed | 229 |
| Avg session duration (s) | 937.712 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.825 |
| Avg connector latency (ms) | 13765.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **263.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
