# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T22:05:45+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 416 | 1.48 | 70.9 | 615.2 |
| source_discovery | 416 | 4.29 | 186.3 | 1783.3 |
| connector | 416 | 90405.68 | 97806.1 | 37608764.4 |
| document_discovery | 416 | 90406.01 | 97806.2 | 37608900.7 |
| document_download | 416 | 235332.19 | 1509355.9 | 97898189.2 |
| extraction | 416 | 99.41 | 274.0 | 41352.6 |
| candidate_validation | 416 | 15.81 | 149.0 | 6577.3 |
| publish_queue | 416 | 15.88 | 149.1 | 6604.1 |
| append_dataset | 416 | 38.57 | 119.7 | 16043.6 |
| export | 416 | 0.35 | 2.7 | 145.4 |
| git_commit | 416 | 0.35 | 15.1 | 145.0 |
| push | 416 | 0.63 | 81.1 | 263.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12386 |
| Documents processed | 27235 |
| Process ratio | 219.9% (target ≥90.0%) |
| Rows published (traces) | 2009 |
| Sessions observed | 307 |
| Avg session duration (s) | 1056.814 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13825.0 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **219.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
