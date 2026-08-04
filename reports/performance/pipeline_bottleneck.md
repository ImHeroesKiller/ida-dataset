# Pipeline Bottleneck Analysis

**Generated:** 2026-08-04T18:47:49+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 291 | 1.37 | 70.9 | 398.0 |
| source_discovery | 291 | 4.36 | 186.3 | 1268.3 |
| connector | 291 | 88862.43 | 97806.1 | 25858968.3 |
| document_discovery | 291 | 88862.64 | 97806.2 | 25859028.4 |
| document_download | 291 | 235018.75 | 1509355.9 | 68390457.5 |
| extraction | 291 | 94.04 | 274.0 | 27366.6 |
| candidate_validation | 291 | 12.64 | 102.5 | 3678.4 |
| publish_queue | 291 | 12.72 | 102.7 | 3700.7 |
| append_dataset | 291 | 40.33 | 119.7 | 11736.1 |
| export | 291 | 0.35 | 2.1 | 101.4 |
| git_commit | 291 | 0.36 | 15.1 | 105.4 |
| push | 291 | 0.7 | 81.1 | 203.8 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 8571 |
| Documents processed | 20242 |
| Process ratio | 236.2% (target ≥90.0%) |
| Rows published (traces) | 1384 |
| Sessions observed | 319 |
| Avg session duration (s) | 960.458 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.87 |
| Avg connector latency (ms) | 14043.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **236.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
