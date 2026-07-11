# Pipeline Bottleneck Analysis

**Generated:** 2026-07-11T14:16:57+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 16 | 0.88 | 1.3 | 14.0 |
| source_discovery | 16 | 2.4 | 2.9 | 38.4 |
| connector | 16 | 22160.21 | 94176.1 | 354563.4 |
| document_discovery | 16 | 22160.39 | 94176.2 | 354566.2 |
| document_download | 16 | 106369.53 | 1263152.2 | 1701912.5 |
| extraction | 16 | 25.77 | 61.2 | 412.3 |
| candidate_validation | 16 | 4.34 | 6.9 | 69.4 |
| publish_queue | 16 | 4.34 | 6.9 | 69.5 |
| append_dataset | 16 | 14.35 | 119.7 | 229.6 |
| export | 16 | 0.32 | 0.6 | 5.2 |
| git_commit | 16 | 0.29 | 0.4 | 4.7 |
| push | 16 | 0.29 | 0.3 | 4.6 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 220 |
| Documents processed | 458 |
| Process ratio | 208.2% (target ≥90.0%) |
| Rows published (traces) | 43 |
| Sessions observed | 42 |
| Avg session duration (s) | 255.571 |
| Max session duration (s) | 2163.0 |
| Rows / session (productive) | 3.231 |
| Avg connector latency (ms) | 2503.3 |
| Worker utilization (est) | 0.372 |
| Idle fraction (est) | 0.628 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **208.2%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
