# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T06:52:30+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 232 | 1.29 | 70.9 | 300.3 |
| source_discovery | 232 | 3.84 | 186.3 | 889.9 |
| connector | 232 | 87554.98 | 97806.1 | 20312754.4 |
| document_discovery | 232 | 87555.13 | 97806.2 | 20312789.1 |
| document_download | 232 | 244307.19 | 1509355.9 | 56679268.5 |
| extraction | 232 | 91.79 | 274.0 | 21295.5 |
| candidate_validation | 232 | 10.99 | 37.2 | 2549.8 |
| publish_queue | 232 | 11.08 | 37.4 | 2570.5 |
| append_dataset | 232 | 41.89 | 119.7 | 9718.5 |
| export | 232 | 0.35 | 1.9 | 80.2 |
| git_commit | 232 | 0.31 | 2.1 | 72.3 |
| push | 232 | 0.31 | 0.8 | 72.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6753 |
| Documents processed | 17055 |
| Process ratio | 252.6% (target ≥90.0%) |
| Rows published (traces) | 1089 |
| Sessions observed | 260 |
| Avg session duration (s) | 947.723 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.836 |
| Avg connector latency (ms) | 13746.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **252.6%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
