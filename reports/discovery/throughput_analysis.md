# Throughput Analysis

**Generated:** 2026-07-16T17:28:51+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 26 |
| URLs discovered | 12 |
| URLs accepted | 12 |
| URLs rejected | 0 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 564416.7 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
