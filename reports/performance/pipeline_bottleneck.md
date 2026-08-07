# Pipeline Bottleneck Analysis

**Generated:** 2026-08-07T05:58:38+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 312 | 1.51 | 70.9 | 472.4 |
| source_discovery | 312 | 4.26 | 186.3 | 1328.4 |
| connector | 312 | 89209.8 | 97806.1 | 27833456.7 |
| document_discovery | 312 | 89210.0 | 97806.2 | 27833519.3 |
| document_download | 312 | 233656.41 | 1509355.9 | 72900800.9 |
| extraction | 312 | 95.4 | 274.0 | 29765.0 |
| candidate_validation | 312 | 13.08 | 102.5 | 4082.0 |
| publish_queue | 312 | 13.16 | 102.7 | 4104.9 |
| append_dataset | 312 | 39.94 | 119.7 | 12461.1 |
| export | 312 | 0.35 | 2.1 | 108.1 |
| git_commit | 312 | 0.36 | 15.1 | 111.8 |
| push | 312 | 0.67 | 81.1 | 210.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 9212 |
| Documents processed | 21356 |
| Process ratio | 231.8% (target ≥90.0%) |
| Rows published (traces) | 1489 |
| Sessions observed | 308 |
| Avg session duration (s) | 1057.838 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.93 |
| Avg connector latency (ms) | 13751.9 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **231.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
