# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T18:37:37+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 173 | 0.99 | 6.5 | 170.6 |
| source_discovery | 173 | 3.1 | 39.8 | 535.7 |
| connector | 173 | 85349.55 | 97806.1 | 14765472.8 |
| document_discovery | 173 | 85349.7 | 97806.2 | 14765498.8 |
| document_download | 173 | 252688.0 | 1509355.9 | 43715023.4 |
| extraction | 173 | 87.22 | 274.0 | 15089.3 |
| candidate_validation | 173 | 9.4 | 30.0 | 1625.4 |
| publish_queue | 173 | 9.53 | 34.7 | 1649.4 |
| append_dataset | 173 | 43.33 | 119.7 | 7495.8 |
| export | 173 | 0.35 | 1.9 | 60.8 |
| git_commit | 173 | 0.31 | 2.1 | 54.1 |
| push | 173 | 0.31 | 0.8 | 54.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4944 |
| Documents processed | 13620 |
| Process ratio | 275.5% (target ≥90.0%) |
| Rows published (traces) | 797 |
| Sessions observed | 201 |
| Avg session duration (s) | 914.687 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.795 |
| Avg connector latency (ms) | 13657.3 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **275.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
