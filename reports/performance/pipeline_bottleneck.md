# Pipeline Bottleneck Analysis

**Generated:** 2026-07-24T15:13:59+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 171 | 0.99 | 6.5 | 168.9 |
| source_discovery | 171 | 3.1 | 39.8 | 530.5 |
| connector | 171 | 85249.44 | 97806.1 | 14577654.8 |
| document_discovery | 171 | 85249.59 | 97806.2 | 14577680.5 |
| document_download | 171 | 252959.33 | 1509355.9 | 43256045.9 |
| extraction | 171 | 87.25 | 274.0 | 14919.2 |
| candidate_validation | 171 | 9.36 | 30.0 | 1600.9 |
| publish_queue | 171 | 9.5 | 34.7 | 1624.8 |
| append_dataset | 171 | 43.46 | 119.7 | 7431.3 |
| export | 171 | 0.35 | 1.9 | 60.1 |
| git_commit | 171 | 0.31 | 2.1 | 53.6 |
| push | 171 | 0.31 | 0.8 | 53.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 4882 |
| Documents processed | 13507 |
| Process ratio | 276.7% (target ≥90.0%) |
| Rows published (traces) | 787 |
| Sessions observed | 199 |
| Avg session duration (s) | 913.0 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.793 |
| Avg connector latency (ms) | 13803.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **276.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
