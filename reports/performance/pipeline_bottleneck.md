# Pipeline Bottleneck Analysis

**Generated:** 2026-08-08T05:21:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 330 | 1.61 | 70.9 | 530.6 |
| source_discovery | 330 | 4.67 | 186.3 | 1540.6 |
| connector | 330 | 89468.21 | 97806.1 | 29524508.0 |
| document_discovery | 330 | 89468.4 | 97806.2 | 29524572.7 |
| document_download | 330 | 230716.99 | 1509355.9 | 76136605.5 |
| extraction | 330 | 96.29 | 274.0 | 31776.7 |
| candidate_validation | 330 | 13.77 | 136.9 | 4545.5 |
| publish_queue | 330 | 13.85 | 136.9 | 4569.1 |
| append_dataset | 330 | 39.52 | 119.7 | 13040.8 |
| export | 330 | 0.34 | 2.1 | 113.7 |
| git_commit | 330 | 0.35 | 15.1 | 116.9 |
| push | 330 | 0.65 | 81.1 | 214.9 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9770 |
| Documents processed | 22363 |
| Process ratio | 228.9% (target ≥90.0%) |
| Rows published (traces) | 1579 |
| Sessions observed | 305 |
| Avg session duration (s) | 1064.944 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.964 |
| Avg connector latency (ms) | 13691.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **228.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
