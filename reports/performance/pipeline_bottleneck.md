# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T09:03:05+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 287 | 1.38 | 70.9 | 395.1 |
| source_discovery | 287 | 4.12 | 186.3 | 1183.7 |
| connector | 287 | 88791.56 | 97806.1 | 25483177.5 |
| document_discovery | 287 | 88791.77 | 97806.2 | 25483237.2 |
| document_download | 287 | 234783.88 | 1509355.9 | 67382974.8 |
| extraction | 287 | 93.9 | 274.0 | 26949.1 |
| candidate_validation | 287 | 12.6 | 102.5 | 3616.0 |
| publish_queue | 287 | 12.68 | 102.7 | 3638.7 |
| append_dataset | 287 | 40.53 | 119.7 | 11631.0 |
| export | 287 | 0.35 | 2.1 | 100.1 |
| git_commit | 287 | 0.36 | 15.1 | 104.1 |
| push | 287 | 0.6 | 81.1 | 171.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8447 |
| Documents processed | 20044 |
| Process ratio | 237.3% (target ≥90.0%) |
| Rows published (traces) | 1364 |
| Sessions observed | 315 |
| Avg session duration (s) | 959.543 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.868 |
| Avg connector latency (ms) | 13970.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **237.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
