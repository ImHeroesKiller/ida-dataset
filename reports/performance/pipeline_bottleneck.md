# Pipeline Bottleneck Analysis

**Generated:** 2026-08-12T22:59:15+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 417 | 1.48 | 70.9 | 616.2 |
| source_discovery | 417 | 4.28 | 186.3 | 1786.2 |
| connector | 417 | 90413.74 | 97806.1 | 37702529.7 |
| document_discovery | 417 | 90414.07 | 97806.2 | 37702666.1 |
| document_download | 417 | 235081.48 | 1509355.9 | 98028977.7 |
| extraction | 417 | 99.45 | 274.0 | 41469.1 |
| candidate_validation | 417 | 15.83 | 149.0 | 6602.1 |
| publish_queue | 417 | 15.9 | 149.1 | 6628.9 |
| append_dataset | 417 | 38.57 | 119.7 | 16083.7 |
| export | 417 | 0.35 | 2.7 | 145.7 |
| git_commit | 417 | 0.35 | 15.1 | 145.3 |
| push | 417 | 0.63 | 81.1 | 264.1 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 12417 |
| Documents processed | 27297 |
| Process ratio | 219.8% (target ≥90.0%) |
| Rows published (traces) | 2014 |
| Sessions observed | 308 |
| Avg session duration (s) | 1056.705 |
| Max session duration (s) | 1573.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13754.5 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **219.8%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
