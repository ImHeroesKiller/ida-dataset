# Factory Capacity

**Generated:** 2026-08-13T00:03:57+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 41.22 |
| Docs/hour | 150.16 |
| Rows/session | 4.99 |
| Top connector | SRC-000004 |
| Top source | SRC-000004 |
| Top mission | corporate governance — service knowledge for Corporate Governance — continuous k |
| Avg connector latency (ms) | 13778.4 |
| Worker utilization | 1.0 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 33 |
| Process ratio | 219.8% |
| Knowledge growth velocity | 4.99 rows/productive session |
| Production efficiency | 0.275 rows/doc |
| Auto-publish confidence gate | 0.92 |
| Automatic publish (last) | 14 |
| Manual review (last) | 0 |

## Success targets

| Target | Status basis |
|--------|--------------|
| ≥50 rows/night | Use rows/hour × overnight window after optimization |
| ≥90% docs processed | Process budget + priority queue |
| Maximize scheduler utilization | More work per non-overlapping hourly slot |
| 0 rejects (quality) | Integrity guard + provenance retained |
| Confidence ≥92% | Auto-publish gate |
