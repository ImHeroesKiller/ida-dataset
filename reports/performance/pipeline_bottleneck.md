# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T08:13:39+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 333 | 1.6 | 70.9 | 533.8 |
| source_discovery | 333 | 4.65 | 186.3 | 1549.3 |
| connector | 333 | 89507.8 | 97806.1 | 29806096.4 |
| document_discovery | 333 | 89507.99 | 97806.2 | 29806161.6 |
| document_download | 333 | 231833.76 | 1509355.9 | 77200641.0 |
| extraction | 333 | 96.45 | 274.0 | 32117.0 |
| candidate_validation | 333 | 13.84 | 136.9 | 4609.4 |
| publish_queue | 333 | 13.91 | 136.9 | 4633.0 |
| append_dataset | 333 | 39.5 | 119.7 | 13153.9 |
| export | 333 | 0.34 | 2.1 | 114.7 |
| git_commit | 333 | 0.36 | 15.1 | 118.4 |
| push | 333 | 0.65 | 81.1 | 215.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9863 |
| Documents processed | 22538 |
| Process ratio | 228.5% (target ≥90.0%) |
| Rows published (traces) | 1594 |
| Sessions observed | 308 |
| Avg session duration (s) | 1066.13 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.964 |
| Avg connector latency (ms) | 14140.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **228.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
