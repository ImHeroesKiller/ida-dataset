# Throughput Analysis

**Generated:** 2026-08-06T06:03:59+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 27 |
| URLs discovered | 80 |
| URLs accepted | 56 |
| URLs rejected | 24 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 780898.5 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
