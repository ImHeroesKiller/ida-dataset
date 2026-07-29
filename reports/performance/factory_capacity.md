# Factory Capacity

**Generated:** 2026-07-29T03:45:05+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 19.02 |
| Docs/hour | 117.93 |
| Rows/session | 4.826 |
| Top connector | SRC-000004 |
| Top source | SRC-000004 |
| Top mission | corporate governance — service knowledge for Corporate Governance — continuous k |
| Avg connector latency (ms) | 13709.2 |
| Worker utilization | 1.0 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 7 |
| Process ratio | 256.8% |
| Knowledge growth velocity | 4.826 rows/productive session |
| Production efficiency | 0.161 rows/doc |
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
