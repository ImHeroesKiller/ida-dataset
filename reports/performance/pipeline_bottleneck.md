# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T21:30:33+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 208 | 1.33 | 70.9 | 276.4 |
| source_discovery | 208 | 3.95 | 186.3 | 821.5 |
| connector | 208 | 86805.37 | 97806.1 | 18055516.1 |
| document_discovery | 208 | 86805.51 | 97806.2 | 18055546.3 |
| document_download | 208 | 252482.96 | 1509355.9 | 52516454.8 |
| extraction | 208 | 89.89 | 274.0 | 18697.3 |
| candidate_validation | 208 | 10.37 | 37.2 | 2156.9 |
| publish_queue | 208 | 10.49 | 37.4 | 2181.9 |
| append_dataset | 208 | 42.46 | 119.7 | 8832.1 |
| export | 208 | 0.35 | 1.9 | 72.2 |
| git_commit | 208 | 0.31 | 2.1 | 64.8 |
| push | 208 | 0.32 | 0.8 | 65.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6019 |
| Documents processed | 15703 |
| Process ratio | 260.9% (target ≥90.0%) |
| Rows published (traces) | 972 |
| Sessions observed | 236 |
| Avg session duration (s) | 940.669 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.831 |
| Avg connector latency (ms) | 13714.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **260.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
