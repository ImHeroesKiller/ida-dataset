# Throughput Analysis

**Generated:** 2026-07-11T19:20:56+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 32 |
| URLs discovered | 187 |
| URLs accepted | 139 |
| URLs rejected | 48 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 761991.3 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
