# Pipeline Bottleneck Analysis

**Generated:** 2026-07-22T10:43:48+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 149 | 0.99 | 6.5 | 148.0 |
| source_discovery | 149 | 3.14 | 39.8 | 467.4 |
| connector | 149 | 83952.98 | 97806.1 | 12508994.0 |
| document_discovery | 149 | 83953.13 | 97806.2 | 12509016.8 |
| document_download | 149 | 253307.72 | 1509355.9 | 37742849.7 |
| extraction | 149 | 85.77 | 274.0 | 12779.1 |
| candidate_validation | 149 | 8.8 | 30.0 | 1311.1 |
| publish_queue | 149 | 8.96 | 34.7 | 1334.6 |
| append_dataset | 149 | 43.95 | 119.7 | 6548.3 |
| export | 149 | 0.35 | 1.9 | 51.7 |
| git_commit | 149 | 0.31 | 2.1 | 46.9 |
| push | 149 | 0.31 | 0.8 | 46.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4210 |
| Documents processed | 12086 |
| Process ratio | 287.1% (target ≥90.0%) |
| Rows published (traces) | 677 |
| Sessions observed | 177 |
| Avg session duration (s) | 891.141 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.761 |
| Avg connector latency (ms) | 13752.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **287.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
