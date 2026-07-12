# Factory Capacity

**Generated:** 2026-07-12T03:53:06+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 16.59 |
| Docs/hour | 487.64 |
| Rows/session | 3.7 |
| Top connector | SRC-CROSSREF |
| Top source | SRC-CROSSREF |
| Top mission | corporate governance — service knowledge for Corporate Governance — continuous k |
| Avg connector latency (ms) | 13826.5 |
| Worker utilization | 1.0 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 7 |
| Process ratio | 317.0% |
| Knowledge growth velocity | 3.7 rows/productive session |
| Production efficiency | 0.034 rows/doc |
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
