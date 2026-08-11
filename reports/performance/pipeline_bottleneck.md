# Pipeline Bottleneck Analysis

**Generated:** 2026-08-11T16:23:55+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 396 | 1.5 | 70.9 | 594.6 |
| source_discovery | 396 | 4.36 | 186.3 | 1726.0 |
| connector | 396 | 90223.38 | 97806.1 | 35728459.3 |
| document_discovery | 396 | 90223.57 | 97806.2 | 35728533.2 |
| document_download | 396 | 236224.81 | 1509355.9 | 93545023.6 |
| extraction | 396 | 98.77 | 274.0 | 39112.3 |
| candidate_validation | 396 | 15.37 | 149.0 | 6086.2 |
| publish_queue | 396 | 15.43 | 149.1 | 6112.1 |
| append_dataset | 396 | 38.69 | 119.7 | 15323.1 |
| export | 396 | 0.35 | 2.7 | 139.1 |
| git_commit | 396 | 0.35 | 15.1 | 138.7 |
| push | 396 | 0.59 | 81.1 | 234.7 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11776 |
| Documents processed | 26082 |
| Process ratio | 221.5% (target ≥90.0%) |
| Rows published (traces) | 1909 |
| Sessions observed | 301 |
| Avg session duration (s) | 1057.196 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13735.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **221.5%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
