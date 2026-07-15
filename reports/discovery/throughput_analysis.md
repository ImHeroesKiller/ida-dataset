# Throughput Analysis

**Generated:** 2026-07-15T18:22:47+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 32 |
| URLs discovered | 276 |
| URLs accepted | 197 |
| URLs rejected | 79 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 761705.9 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
