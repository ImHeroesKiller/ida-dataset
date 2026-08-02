# Pipeline Bottleneck Analysis

**Generated:** 2026-08-02T03:13:09+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 263 | 1.26 | 70.9 | 330.3 |
| source_discovery | 263 | 3.72 | 186.3 | 978.3 |
| connector | 263 | 88313.91 | 97806.1 | 23226558.5 |
| document_discovery | 263 | 88314.12 | 97806.2 | 23226614.7 |
| document_download | 263 | 238681.73 | 1509355.9 | 62773293.8 |
| extraction | 263 | 92.95 | 274.0 | 24445.9 |
| candidate_validation | 263 | 12.1 | 102.5 | 3181.0 |
| publish_queue | 263 | 12.18 | 102.7 | 3203.1 |
| append_dataset | 263 | 41.12 | 119.7 | 10815.6 |
| export | 263 | 0.35 | 2.1 | 92.3 |
| git_commit | 263 | 0.37 | 15.1 | 97.0 |
| push | 263 | 0.62 | 81.1 | 163.5 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7703 |
| Documents processed | 18796 |
| Process ratio | 244.0% (target ≥90.0%) |
| Rows published (traces) | 1244 |
| Sessions observed | 291 |
| Avg session duration (s) | 954.993 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.855 |
| Avg connector latency (ms) | 13818.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **244.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
