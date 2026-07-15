# Pipeline Bottleneck Analysis

**Generated:** 2026-07-15T20:33:19+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 69 | 1.04 | 6.5 | 72.1 |
| source_discovery | 69 | 2.74 | 3.3 | 188.9 |
| connector | 69 | 72290.11 | 97806.1 | 4988017.4 |
| document_discovery | 69 | 72290.25 | 97806.2 | 4988027.1 |
| document_download | 69 | 269495.27 | 1509355.9 | 18595173.3 |
| extraction | 69 | 81.42 | 274.0 | 5618.2 |
| candidate_validation | 69 | 6.45 | 9.5 | 444.9 |
| publish_queue | 69 | 6.49 | 9.5 | 448.0 |
| append_dataset | 69 | 50.38 | 119.7 | 3476.0 |
| export | 69 | 0.34 | 0.6 | 23.3 |
| git_commit | 69 | 0.33 | 2.1 | 22.5 |
| push | 69 | 0.32 | 0.8 | 22.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 1770 |
| Documents processed | 6809 |
| Process ratio | 384.7% (target ≥90.0%) |
| Rows published (traces) | 277 |
| Sessions observed | 97 |
| Avg session duration (s) | 738.959 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.452 |
| Avg connector latency (ms) | 14883.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **384.7%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
