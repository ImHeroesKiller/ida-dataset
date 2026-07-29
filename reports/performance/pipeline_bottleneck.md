# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T09:08:11+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 222 | 1.31 | 70.9 | 290.3 |
| source_discovery | 222 | 3.88 | 186.3 | 861.3 |
| connector | 222 | 87263.01 | 97806.1 | 19372387.3 |
| document_discovery | 222 | 87263.15 | 97806.2 | 19372419.6 |
| document_download | 222 | 247368.39 | 1509355.9 | 54915783.5 |
| extraction | 222 | 91.05 | 274.0 | 20212.3 |
| candidate_validation | 222 | 10.75 | 37.2 | 2387.2 |
| publish_queue | 222 | 10.85 | 37.4 | 2407.6 |
| append_dataset | 222 | 41.98 | 119.7 | 9319.6 |
| export | 222 | 0.35 | 1.9 | 77.1 |
| git_commit | 222 | 0.31 | 2.1 | 69.1 |
| push | 222 | 0.31 | 0.8 | 69.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6443 |
| Documents processed | 16446 |
| Process ratio | 255.3% (target ≥90.0%) |
| Rows published (traces) | 1039 |
| Sessions observed | 250 |
| Avg session duration (s) | 945.04 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.828 |
| Avg connector latency (ms) | 13821.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **255.3%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
