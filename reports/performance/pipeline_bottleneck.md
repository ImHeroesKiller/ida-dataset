# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T13:30:34+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 410 | 1.49 | 70.9 | 609.6 |
| source_discovery | 410 | 4.31 | 186.3 | 1768.0 |
| connector | 410 | 90352.77 | 97806.1 | 37044633.9 |
| document_discovery | 410 | 90352.95 | 97806.2 | 37044709.6 |
| document_download | 410 | 236470.6 | 1509355.9 | 96952944.3 |
| extraction | 410 | 99.38 | 274.0 | 40745.4 |
| candidate_validation | 410 | 15.69 | 149.0 | 6433.7 |
| publish_queue | 410 | 15.76 | 149.1 | 6460.1 |
| append_dataset | 410 | 38.66 | 119.7 | 15851.5 |
| export | 410 | 0.35 | 2.7 | 143.7 |
| git_commit | 410 | 0.35 | 15.1 | 143.4 |
| push | 410 | 0.58 | 81.1 | 239.0 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12200 |
| Documents processed | 26885 |
| Process ratio | 220.4% (target ≥90.0%) |
| Rows published (traces) | 1979 |
| Sessions observed | 301 |
| Avg session duration (s) | 1057.598 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13774.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
