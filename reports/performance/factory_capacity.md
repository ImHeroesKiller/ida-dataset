# Factory Capacity

**Generated:** 2026-07-11T08:14:59+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 30.64 |
| Docs/hour | 67.41 |
| Rows/session | 2.5 |
| Top connector | SRC-CROSSREF |
| Top source | SRC-CROSSREF |
| Top mission | Bootstrap Buyer Persona Library — continuous knowledge manufacturing for buyer_p |
| Avg connector latency (ms) | 2670.4 |
| Worker utilization | 0.039 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 6 |
| Process ratio | 54.8% |
| Knowledge growth velocity | 2.5 rows/productive session |
| Production efficiency | 0.455 rows/doc |
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
