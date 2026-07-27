# Pipeline Bottleneck Analysis

**Generated:** 2026-07-27T19:52:39+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 207 | 1.33 | 70.9 | 275.3 |
| source_discovery | 207 | 3.95 | 186.3 | 818.6 |
| connector | 207 | 86770.77 | 97806.1 | 17961548.9 |
| document_discovery | 207 | 86770.91 | 97806.2 | 17961579.0 |
| document_download | 207 | 253035.33 | 1509355.9 | 52378312.4 |
| extraction | 207 | 89.79 | 274.0 | 18585.6 |
| candidate_validation | 207 | 10.35 | 37.2 | 2141.7 |
| publish_queue | 207 | 10.47 | 37.4 | 2166.7 |
| append_dataset | 207 | 42.48 | 119.7 | 8793.5 |
| export | 207 | 0.35 | 1.9 | 71.9 |
| git_commit | 207 | 0.31 | 2.1 | 64.5 |
| push | 207 | 0.32 | 0.8 | 65.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 5988 |
| Documents processed | 15641 |
| Process ratio | 261.2% (target ≥90.0%) |
| Rows published (traces) | 967 |
| Sessions observed | 235 |
| Avg session duration (s) | 940.536 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.83 |
| Avg connector latency (ms) | 13698.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **261.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
