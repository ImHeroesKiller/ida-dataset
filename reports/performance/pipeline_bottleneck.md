# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T00:19:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 165 | 0.99 | 6.5 | 163.0 |
| source_discovery | 165 | 3.11 | 39.8 | 513.0 |
| connector | 165 | 84930.5 | 97806.1 | 14013532.0 |
| document_discovery | 165 | 84930.65 | 97806.2 | 14013556.9 |
| document_download | 165 | 252165.59 | 1509355.9 | 41607322.3 |
| extraction | 165 | 86.87 | 274.0 | 14333.2 |
| candidate_validation | 165 | 9.23 | 30.0 | 1522.5 |
| publish_queue | 165 | 9.37 | 34.7 | 1546.2 |
| append_dataset | 165 | 43.65 | 119.7 | 7202.2 |
| export | 165 | 0.35 | 1.9 | 58.1 |
| git_commit | 165 | 0.31 | 2.1 | 51.8 |
| push | 165 | 0.32 | 0.8 | 52.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4696 |
| Documents processed | 13145 |
| Process ratio | 279.9% (target ≥90.0%) |
| Rows published (traces) | 757 |
| Sessions observed | 193 |
| Avg session duration (s) | 906.725 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.785 |
| Avg connector latency (ms) | 13730.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **279.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
