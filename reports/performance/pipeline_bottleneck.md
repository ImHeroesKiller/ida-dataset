# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T02:57:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 50 | 1.09 | 6.5 | 54.4 |
| source_discovery | 50 | 2.72 | 3.3 | 136.2 |
| connector | 50 | 64054.11 | 97806.1 | 3202705.4 |
| document_discovery | 50 | 64054.25 | 97806.2 | 3202712.5 |
| document_download | 50 | 222523.54 | 1509355.9 | 11126177.1 |
| extraction | 50 | 71.69 | 109.5 | 3584.3 |
| candidate_validation | 50 | 5.79 | 8.7 | 289.4 |
| publish_queue | 50 | 5.84 | 8.8 | 292.1 |
| append_dataset | 50 | 47.12 | 119.7 | 2356.2 |
| export | 50 | 0.35 | 0.6 | 17.3 |
| git_commit | 50 | 0.33 | 2.1 | 16.7 |
| push | 50 | 0.33 | 0.8 | 16.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1201 |
| Documents processed | 4540 |
| Process ratio | 378.0% (target ≥90.0%) |
| Rows published (traces) | 182 |
| Sessions observed | 78 |
| Avg session duration (s) | 615.038 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.209 |
| Avg connector latency (ms) | 13676.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **378.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
