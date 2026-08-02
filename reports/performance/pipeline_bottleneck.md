# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T11:34:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 267 | 1.4 | 70.9 | 374.4 |
| source_discovery | 267 | 4.12 | 186.3 | 1100.6 |
| connector | 267 | 88398.5 | 97806.1 | 23602400.2 |
| document_discovery | 267 | 88398.72 | 97806.2 | 23602457.0 |
| document_download | 267 | 238209.1 | 1509355.9 | 63601828.6 |
| extraction | 267 | 93.04 | 274.0 | 24840.4 |
| candidate_validation | 267 | 12.17 | 102.5 | 3248.7 |
| publish_queue | 267 | 12.25 | 102.7 | 3270.8 |
| append_dataset | 267 | 41.0 | 119.7 | 10946.6 |
| export | 267 | 0.35 | 2.1 | 93.5 |
| git_commit | 267 | 0.37 | 15.1 | 98.1 |
| push | 267 | 0.62 | 81.1 | 164.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7827 |
| Documents processed | 19022 |
| Process ratio | 243.0% (target ≥90.0%) |
| Rows published (traces) | 1264 |
| Sessions observed | 295 |
| Avg session duration (s) | 956.308 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.858 |
| Avg connector latency (ms) | 13652.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **243.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
