# Throughput Analysis

**Generated:** 2026-07-15T11:05:19+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 32 |
| URLs discovered | 198 |
| URLs accepted | 152 |
| URLs rejected | 46 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 772913.7 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
