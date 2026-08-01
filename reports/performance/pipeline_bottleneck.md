# Pipeline Bottleneck Analysis

**Generated:** 2026-08-01T20:26:36+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 260 | 1.26 | 70.9 | 327.6 |
| source_discovery | 260 | 3.73 | 186.3 | 970.1 |
| connector | 260 | 88247.26 | 97806.1 | 22944287.4 |
| document_discovery | 260 | 88247.47 | 97806.2 | 22944343.1 |
| document_download | 260 | 238652.53 | 1509355.9 | 62049658.8 |
| extraction | 260 | 92.93 | 274.0 | 24162.0 |
| candidate_validation | 260 | 12.05 | 102.5 | 3132.0 |
| publish_queue | 260 | 12.13 | 102.7 | 3154.1 |
| append_dataset | 260 | 41.23 | 119.7 | 10720.0 |
| export | 260 | 0.35 | 2.1 | 91.5 |
| git_commit | 260 | 0.37 | 15.1 | 96.1 |
| push | 260 | 0.63 | 81.1 | 162.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 7610 |
| Documents processed | 18641 |
| Process ratio | 245.0% (target ≥90.0%) |
| Rows published (traces) | 1229 |
| Sessions observed | 288 |
| Avg session duration (s) | 954.566 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.854 |
| Avg connector latency (ms) | 13740.7 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **245.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
