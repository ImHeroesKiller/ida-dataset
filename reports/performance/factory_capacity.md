# Factory Capacity

**Generated:** 2026-07-15T05:55:01+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 14.54 |
| Docs/hour | 369.28 |
| Rows/session | 4.382 |
| Top connector | SRC-CROSSREF |
| Top source | SRC-CROSSREF |
| Top mission | corporate governance — service knowledge for Corporate Governance — continuous k |
| Avg connector latency (ms) | 13714.1 |
| Worker utilization | 1.0 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 7 |
| Process ratio | 384.4% |
| Knowledge growth velocity | 4.382 rows/productive session |
| Production efficiency | 0.039 rows/doc |
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
