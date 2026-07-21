# Throughput Analysis

**Generated:** 2026-07-21T09:40:56+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 27 |
| URLs discovered | 124 |
| URLs accepted | 66 |
| URLs rejected | 58 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 742856.6 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
