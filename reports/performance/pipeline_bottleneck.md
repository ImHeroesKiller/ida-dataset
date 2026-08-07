# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T16:14:29+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 319 | 1.63 | 70.9 | 520.7 |
| source_discovery | 319 | 4.74 | 186.3 | 1510.6 |
| connector | 319 | 89313.89 | 97806.1 | 28491130.2 |
| document_discovery | 319 | 89314.09 | 97806.2 | 28491193.5 |
| document_download | 319 | 232819.26 | 1509355.9 | 74269344.8 |
| extraction | 319 | 95.84 | 274.0 | 30572.3 |
| candidate_validation | 319 | 13.59 | 136.9 | 4335.9 |
| publish_queue | 319 | 13.66 | 136.9 | 4358.8 |
| append_dataset | 319 | 39.78 | 119.7 | 12689.4 |
| export | 319 | 0.35 | 2.1 | 110.1 |
| git_commit | 319 | 0.36 | 15.1 | 113.7 |
| push | 319 | 0.66 | 81.1 | 212.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9429 |
| Documents processed | 21734 |
| Process ratio | 230.5% (target ≥90.0%) |
| Rows published (traces) | 1524 |
| Sessions observed | 315 |
| Avg session duration (s) | 1057.13 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.931 |
| Avg connector latency (ms) | 13744.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **230.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
