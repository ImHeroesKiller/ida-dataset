# Throughput Analysis

**Generated:** 2026-07-11T15:17:15+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 35 |
| Queries executed | 115 |
| URLs discovered | 1041 |
| URLs accepted | 610 |
| URLs rejected | 431 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 770651.1 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 5
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
