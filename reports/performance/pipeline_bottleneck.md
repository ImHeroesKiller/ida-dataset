# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T19:30:42+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 414 | 1.48 | 70.9 | 613.5 |
| source_discovery | 414 | 4.3 | 186.3 | 1778.5 |
| connector | 414 | 90387.98 | 97806.1 | 37420625.4 |
| document_discovery | 414 | 90388.17 | 97806.2 | 37420701.5 |
| document_download | 414 | 235845.75 | 1509355.9 | 97640141.4 |
| extraction | 414 | 99.44 | 274.0 | 41167.5 |
| candidate_validation | 414 | 15.79 | 149.0 | 6537.7 |
| publish_queue | 414 | 15.86 | 149.1 | 6564.4 |
| append_dataset | 414 | 38.62 | 119.7 | 15987.9 |
| export | 414 | 0.35 | 2.7 | 144.9 |
| git_commit | 414 | 0.35 | 15.1 | 144.6 |
| push | 414 | 0.64 | 81.1 | 263.3 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12324 |
| Documents processed | 27122 |
| Process ratio | 220.1% (target ≥90.0%) |
| Rows published (traces) | 1999 |
| Sessions observed | 305 |
| Avg session duration (s) | 1057.184 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13936.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.1%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
