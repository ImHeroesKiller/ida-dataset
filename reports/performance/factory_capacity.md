# Factory Capacity

**Generated:** 2026-07-11T17:59:27+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 5.82 |
| Docs/hour | 261.86 |
| Rows/session | 3.357 |
| Top connector | SRC-CROSSREF |
| Top source | SRC-CROSSREF |
| Top mission | Bootstrap Buyer Persona Library — continuous knowledge manufacturing for buyer_p |
| Avg connector latency (ms) | 13712.4 |
| Worker utilization | 0.583 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 7 |
| Process ratio | 254.8% |
| Knowledge growth velocity | 3.357 rows/productive session |
| Production efficiency | 0.022 rows/doc |
| Auto-publish confidence gate | 0.92 |
| Automatic publish (last) | 2 |
| Manual review (last) | 0 |

## Success targets

| Target | Status basis |
|--------|--------------|
| ≥50 rows/night | Use rows/hour × overnight window after optimization |
| ≥90% docs processed | Process budget + priority queue |
| Maximize scheduler utilization | More work per non-overlapping hourly slot |
| 0 rejects (quality) | Integrity guard + provenance retained |
| Confidence ≥92% | Auto-publish gate |
