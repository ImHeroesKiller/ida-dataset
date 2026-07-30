# Pipeline Bottleneck Analysis

**Generated:** 2026-07-30T00:18:14+00:00
**Primary bottleneck:** `document_download`

Measured from real production sessions and acquisition traces only.

## Stage durations

| Stage | Count | Avg ms | Max ms | Total ms |
|-------|------:|-------:|-------:|---------:|
| mission | 230 | 1.3 | 70.9 | 298.2 |
| source_discovery | 230 | 3.84 | 186.3 | 884.0 |
| connector | 230 | 87497.96 | 97806.1 | 20124530.5 |
| document_discovery | 230 | 87498.11 | 97806.2 | 20124564.9 |
| document_download | 230 | 245231.84 | 1509355.9 | 56403323.8 |
| extraction | 230 | 91.65 | 274.0 | 21078.4 |
| candidate_validation | 230 | 10.95 | 37.2 | 2517.4 |
| publish_queue | 230 | 11.04 | 37.4 | 2538.1 |
| append_dataset | 230 | 41.87 | 119.7 | 9631.0 |
| export | 230 | 0.35 | 1.9 | 79.5 |
| git_commit | 230 | 0.31 | 2.1 | 71.7 |
| push | 230 | 0.31 | 0.8 | 72.2 |

## End-to-end funnel

| Metric | Value |
|--------|------:|
| Documents discovered | 6691 |
| Documents processed | 16931 |
| Process ratio | 253.0% (target ≥90.0%) |
| Rows published (traces) | 1079 |
| Sessions observed | 258 |
| Avg session duration (s) | 947.43 |
| Max session duration (s) | 2353.0 |
| Rows / session (productive) | 4.834 |
| Avg connector latency (ms) | 13747.1 |
| Worker utilization (est) | 1.0 |
| Idle fraction (est) | 0.0 |
| Queue wait (doc depth) | 0 |

## Bottleneck notes

- Historical process ratio **253.0%** vs target **≥90%**.
- Primary levers: per-session document budget, concurrent downloads, prioritization.
- Scheduler remains non-overlapping (`factory-production` concurrency); density gains come from more work per idle hourly slot.
