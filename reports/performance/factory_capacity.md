# Factory Capacity

**Generated:** 2026-07-12T18:23:01+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 2.66 |
| Docs/hour | 354.15 |
| Rows/session | 4.071 |
| Top connector | SRC-CROSSREF |
| Top source | SRC-CROSSREF |
| Top mission | corporate governance — service knowledge for Corporate Governance — continuous k |
| Avg connector latency (ms) | 13792.0 |
| Worker utilization | 1.0 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 7 |
| Process ratio | 354.0% |
| Knowledge growth velocity | 4.071 rows/productive session |
| Production efficiency | 0.008 rows/doc |
| Auto-publish confidence gate | 0.92 |
| Automatic publish (last) | 1 |
| Manual review (last) | 0 |

## Success targets

| Target | Status basis |
|--------|--------------|
| ≥50 rows/night | Use rows/hour × overnight window after optimization |
| ≥90% docs processed | Process budget + priority queue |
| Maximize scheduler utilization | More work per non-overlapping hourly slot |
| 0 rejects (quality) | Integrity guard + provenance retained |
| Confidence ≥92% | Auto-publish gate |
