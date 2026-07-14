# Pipeline Bottleneck Analysis

**Generated:** 2026-07-14T18:26:16+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 57 | 1.06 | 6.5 | 60.7 |
| source_discovery | 57 | 2.72 | 3.3 | 155.0 |
| connector | 57 | 67721.59 | 97806.1 | 3860130.9 |
| document_discovery | 57 | 67721.74 | 97806.2 | 3860139.1 |
| document_download | 57 | 242465.16 | 1509355.9 | 13820514.2 |
| extraction | 57 | 78.05 | 274.0 | 4449.1 |
| candidate_validation | 57 | 6.03 | 9.5 | 343.9 |
| publish_queue | 57 | 6.08 | 9.5 | 346.6 |
| append_dataset | 57 | 47.61 | 119.7 | 2713.8 |
| export | 57 | 0.34 | 0.6 | 19.3 |
| git_commit | 57 | 0.33 | 2.1 | 18.8 |
| push | 57 | 0.32 | 0.8 | 18.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1408 |
| Documents processed | 5329 |
| Process ratio | 378.5% (target ≥90.0%) |
| Rows published (traces) | 217 |
| Sessions observed | 85 |
| Avg session duration (s) | 664.741 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.32 |
| Avg connector latency (ms) | 13711.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **378.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
