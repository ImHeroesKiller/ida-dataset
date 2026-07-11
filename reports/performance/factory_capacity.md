# Factory Capacity

**Generated:** 2026-07-11T12:21:16+00:00

| Dimension | Value |
|-----------|------:|
| Rows/hour | 0.0 |
| Docs/hour | 391.78 |
| Rows/session | 3.333 |
| Top connector | SRC-CROSSREF |
| Top source | SRC-CROSSREF |
| Top mission | Bootstrap Buyer Persona Library — continuous knowledge manufacturing for buyer_p |
| Avg connector latency (ms) | 2413.9 |
| Worker utilization | 0.107 |
| Document queue depth | 0 |
| Candidate queue depth | 4 |
| Publish queue depth | 6 |
| Process ratio | 71.4% |
| Knowledge growth velocity | 3.333 rows/productive session |
| Production efficiency | 0.672 rows/doc |
| Auto-publish confidence gate | 0.92 |
| Automatic publish (last) | 0 |
| Manual review (last) | 2 |

## Success targets

| Target | Status basis |
|--------|--------------|
| ≥50 rows/night | Use rows/hour × overnight window after optimization |
| ≥90% docs processed | Process budget + priority queue |
| Maximize scheduler utilization | More work per non-overlapping hourly slot |
| 0 rejects (quality) | Integrity guard + provenance retained |
| Confidence ≥92% | Auto-publish gate |
