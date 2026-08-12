# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T18:16:56+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 413 | 1.48 | 70.9 | 612.3 |
| source_discovery | 413 | 4.3 | 186.3 | 1775.5 |
| connector | 413 | 90379.05 | 97806.1 | 37326546.8 |
| document_discovery | 413 | 90379.23 | 97806.2 | 37326622.8 |
| document_download | 413 | 236087.55 | 1509355.9 | 97504156.4 |
| extraction | 413 | 99.39 | 274.0 | 41049.6 |
| candidate_validation | 413 | 15.77 | 149.0 | 6512.4 |
| publish_queue | 413 | 15.83 | 149.1 | 6539.1 |
| append_dataset | 413 | 38.61 | 119.7 | 15947.8 |
| export | 413 | 0.35 | 2.7 | 144.6 |
| git_commit | 413 | 0.35 | 15.1 | 144.3 |
| push | 413 | 0.64 | 81.1 | 263.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12293 |
| Documents processed | 27060 |
| Process ratio | 220.1% (target ≥90.0%) |
| Rows published (traces) | 1994 |
| Sessions observed | 304 |
| Avg session duration (s) | 1057.339 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13915.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
