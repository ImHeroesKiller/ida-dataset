# Pipeline Bottleneck Analysis

**Generated:** 2026-07-29T12:18:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 224 | 1.3 | 70.9 | 292.3 |
| source_discovery | 224 | 3.87 | 186.3 | 867.0 |
| connector | 224 | 87323.72 | 97806.1 | 19560513.4 |
| document_discovery | 224 | 87323.87 | 97806.2 | 19560546.0 |
| document_download | 224 | 246925.58 | 1509355.9 | 55311330.6 |
| extraction | 224 | 91.19 | 274.0 | 20426.6 |
| candidate_validation | 224 | 10.8 | 37.2 | 2419.2 |
| publish_queue | 224 | 10.89 | 37.4 | 2439.7 |
| append_dataset | 224 | 41.95 | 119.7 | 9397.8 |
| export | 224 | 0.35 | 1.9 | 77.7 |
| git_commit | 224 | 0.31 | 2.1 | 69.8 |
| push | 224 | 0.31 | 0.8 | 70.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6505 |
| Documents processed | 16570 |
| Process ratio | 254.7% (target ≥90.0%) |
| Rows published (traces) | 1049 |
| Sessions observed | 252 |
| Avg session duration (s) | 945.754 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.829 |
| Avg connector latency (ms) | 13723.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **254.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
