# Throughput Analysis

**Generated:** 2026-07-12T19:31:57+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 32 |
| URLs discovered | 200 |
| URLs accepted | 147 |
| URLs rejected | 53 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 754587.3 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
