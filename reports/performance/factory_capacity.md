# Factory Capacity

**Generated:** 2026-07-11T08:32:14+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 30.73 |
| Docs/hour | 67.6 |
| Rows/session | 2.778 |
| Top connector | SRC-CROSSREF |
| Top source | SRC-CROSSREF |
| Top mission | Bootstrap Buyer Persona Library — continuous knowledge manufacturing for buyer_p |
| Avg connector latency (ms) | 2443.4 |
| Worker utilization | 0.049 |
| Document queue depth | 0 |
| Candidate queue depth | 0 |
| Publish queue depth | 6 |
| Process ratio | 60.0% |
| Knowledge growth velocity | 2.778 rows/productive session |
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
