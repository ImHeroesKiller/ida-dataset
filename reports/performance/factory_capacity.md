# Factory Capacity

**Generated:** 2026-07-12T21:10:46+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 16.49 |
| Docs/hour | 438.55 |
| Rows/session | 4.0 |
| Top connector | SRC-CROSSREF |
| Top source | SRC-CROSSREF |
| Top mission | corporate governance — service knowledge for Corporate Governance — continuous k |
| Avg connector latency (ms) | 14099.6 |
| Worker utilization | 1.0 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 7 |
| Process ratio | 355.1% |
| Knowledge growth velocity | 4.0 rows/productive session |
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
