# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T17:59:27+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 19 | 0.89 | 1.3 | 16.9 |
| source_discovery | 19 | 2.48 | 3.0 | 47.1 |
| connector | 19 | 24459.34 | 97806.1 | 464727.4 |
| document_discovery | 19 | 24459.51 | 97806.2 | 464730.6 |
| document_download | 19 | 180652.08 | 1509355.9 | 3432389.5 |
| extraction | 19 | 33.52 | 93.4 | 636.8 |
| candidate_validation | 19 | 4.14 | 6.9 | 78.7 |
| publish_queue | 19 | 4.15 | 6.9 | 78.8 |
| append_dataset | 19 | 19.12 | 119.7 | 363.2 |
| export | 19 | 0.33 | 0.6 | 6.2 |
| git_commit | 19 | 0.3 | 0.4 | 5.7 |
| push | 19 | 0.29 | 0.3 | 5.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 283 |
| Documents processed | 721 |
| Process ratio | 254.8% (target ≥90.0%) |
| Rows published (traces) | 48 |
| Sessions observed | 47 |
| Avg session duration (s) | 304.809 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 3.357 |
| Avg connector latency (ms) | 13712.4 |
| Worker utilization (est) | 0.583 |
| Idle fraction (est) | 0.417 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **254.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
