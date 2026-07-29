# Factory Capacity

**Generated:** 2026-07-29T15:27:13+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 17.04 |
| Docs/hour | 211.35 |
| Rows/session | 4.83 |
| Top connector | SRC-000004 |
| Top source | SRC-000004 |
| Top mission | corporate governance — service knowledge for Corporate Governance — continuous k |
| Avg connector latency (ms) | 13701.9 |
| Worker utilization | 1.0 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 7 |
| Process ratio | 254.5% |
| Knowledge growth velocity | 4.83 rows/productive session |
| Production efficiency | 0.081 rows/doc |
| Auto-publish confidence gate | 0.92 |
| Automatic publish (last) | 5 |
| Manual review (last) | 0 |

## Success targets

| Target | Status basis |
|--------|--------------|
| ≥50 rows/night | Use rows/hour × overnight window after optimization |
| ≥90% docs processed | Process budget + priority queue |
| Maximize scheduler utilization | More work per non-overlapping hourly slot |
| 0 rejects (quality) | Integrity guard + provenance retained |
| Confidence ≥92% | Auto-publish gate |
