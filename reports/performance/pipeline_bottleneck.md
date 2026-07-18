# Pipeline Bottleneck Analysis

**Generated:** 2026-07-18T08:12:00+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 98 | 1.02 | 6.5 | 100.2 |
| source_discovery | 98 | 2.76 | 3.5 | 270.9 |
| connector | 98 | 78725.73 | 97806.1 | 7715121.7 |
| document_discovery | 98 | 78725.88 | 97806.2 | 7715135.8 |
| document_download | 98 | 267751.32 | 1509355.9 | 26239629.8 |
| extraction | 98 | 83.28 | 274.0 | 8161.2 |
| candidate_validation | 98 | 7.37 | 18.7 | 722.4 |
| publish_queue | 98 | 7.59 | 34.7 | 743.9 |
| append_dataset | 98 | 47.26 | 119.7 | 4631.9 |
| export | 98 | 0.34 | 0.6 | 33.1 |
| git_commit | 98 | 0.32 | 2.1 | 31.3 |
| push | 98 | 0.31 | 0.8 | 30.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 2659 |
| Documents processed | 8812 |
| Process ratio | 331.4% (target ≥90.0%) |
| Rows published (traces) | 422 |
| Sessions observed | 126 |
| Avg session duration (s) | 821.548 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.626 |
| Avg connector latency (ms) | 13697.2 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **331.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
