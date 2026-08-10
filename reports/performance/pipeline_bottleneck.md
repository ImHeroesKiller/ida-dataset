# Pipeline Bottleneck Analysis

**Generated:** 2026-08-10T21:59:25+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 384 | 1.52 | 70.9 | 583.0 |
| source_discovery | 384 | 4.41 | 186.3 | 1692.1 |
| connector | 384 | 90104.41 | 97806.1 | 34600093.5 |
| document_discovery | 384 | 90104.6 | 97806.2 | 34600166.1 |
| document_download | 384 | 238804.11 | 1509355.9 | 91700778.4 |
| extraction | 384 | 98.3 | 274.0 | 37749.0 |
| candidate_validation | 384 | 15.15 | 149.0 | 5815.9 |
| publish_queue | 384 | 15.21 | 149.1 | 5841.2 |
| append_dataset | 384 | 38.78 | 119.7 | 14892.4 |
| export | 384 | 0.35 | 2.7 | 135.5 |
| git_commit | 384 | 0.35 | 15.1 | 134.7 |
| push | 384 | 0.6 | 81.1 | 231.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 11414 |
| Documents processed | 25381 |
| Process ratio | 222.4% (target ≥90.0%) |
| Rows published (traces) | 1849 |
| Sessions observed | 302 |
| Avg session duration (s) | 1063.252 |
| Max session duration (s) | 2265.0 |
| Rows / session (productive) | 4.99 |
| Avg connector latency (ms) | 13712.8 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **222.4%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
