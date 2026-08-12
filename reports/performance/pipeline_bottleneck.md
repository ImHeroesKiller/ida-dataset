# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T16:22:26+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 412 | 1.48 | 70.9 | 611.2 |
| source_discovery | 412 | 4.3 | 186.3 | 1772.7 |
| connector | 412 | 90370.05 | 97806.1 | 37232460.4 |
| document_discovery | 412 | 90370.23 | 97806.2 | 37232536.3 |
| document_download | 412 | 236164.34 | 1509355.9 | 97299707.3 |
| extraction | 412 | 99.35 | 274.0 | 40933.6 |
| candidate_validation | 412 | 15.75 | 149.0 | 6488.0 |
| publish_queue | 412 | 15.81 | 149.1 | 6514.7 |
| append_dataset | 412 | 38.61 | 119.7 | 15907.8 |
| export | 412 | 0.35 | 2.7 | 144.3 |
| git_commit | 412 | 0.35 | 15.1 | 144.0 |
| push | 412 | 0.64 | 81.1 | 262.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12262 |
| Documents processed | 26998 |
| Process ratio | 220.2% (target ≥90.0%) |
| Rows published (traces) | 1989 |
| Sessions observed | 303 |
| Avg session duration (s) | 1057.35 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13852.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
