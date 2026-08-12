# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T23:58:41+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 402 | 1.49 | 70.9 | 600.6 |
| source_discovery | 402 | 4.34 | 186.3 | 1743.3 |
| connector | 402 | 90279.96 | 97806.1 | 36292544.2 |
| document_discovery | 402 | 90280.15 | 97806.2 | 36292619.0 |
| document_download | 402 | 236164.62 | 1509355.9 | 94938175.9 |
| extraction | 402 | 99.05 | 274.0 | 39819.8 |
| candidate_validation | 402 | 15.51 | 149.0 | 6235.0 |
| publish_queue | 402 | 15.58 | 149.1 | 6261.3 |
| append_dataset | 402 | 38.7 | 119.7 | 15557.8 |
| export | 402 | 0.35 | 2.7 | 141.1 |
| git_commit | 402 | 0.35 | 15.1 | 140.7 |
| push | 402 | 0.59 | 81.1 | 236.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11962 |
| Documents processed | 26443 |
| Process ratio | 221.1% (target ≥90.0%) |
| Rows published (traces) | 1939 |
| Sessions observed | 307 |
| Avg session duration (s) | 1058.147 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13770.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
