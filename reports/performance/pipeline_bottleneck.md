# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T06:38:31+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 405 | 1.49 | 70.9 | 603.8 |
| source_discovery | 405 | 4.33 | 186.3 | 1752.8 |
| connector | 405 | 90308.53 | 97806.1 | 36574955.5 |
| document_discovery | 405 | 90308.72 | 97806.2 | 36575030.6 |
| document_download | 405 | 235769.09 | 1509355.9 | 95486483.2 |
| extraction | 405 | 99.21 | 274.0 | 40179.9 |
| candidate_validation | 405 | 15.58 | 149.0 | 6309.4 |
| publish_queue | 405 | 15.64 | 149.1 | 6335.7 |
| append_dataset | 405 | 38.71 | 119.7 | 15676.4 |
| export | 405 | 0.35 | 2.7 | 142.0 |
| git_commit | 405 | 0.35 | 15.1 | 141.7 |
| push | 405 | 0.59 | 81.1 | 237.4 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12055 |
| Documents processed | 26629 |
| Process ratio | 220.9% (target ≥90.0%) |
| Rows published (traces) | 1954 |
| Sessions observed | 310 |
| Avg session duration (s) | 1057.961 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13695.4 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **220.9%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
