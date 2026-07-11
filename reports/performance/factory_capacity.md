# Factory Capacity

**Generated:** 2026-07-11T21:09:09+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 17.19 |
| Docs/hour | 453.74 |
| Rows/session | 3.375 |
| Top connector | SRC-CROSSREF |
| Top source | SRC-CROSSREF |
| Top mission | corporate governance — service knowledge for Corporate Governance — continuous k |
| Avg connector latency (ms) | 13666.1 |
| Worker utilization | 0.932 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 7 |
| Process ratio | 268.9% |
| Knowledge growth velocity | 3.375 rows/productive session |
| Production efficiency | 0.038 rows/doc |
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
