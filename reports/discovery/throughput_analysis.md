# Throughput Analysis

**Generated:** 2026-08-24T07:14:03+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 22 |
| URLs discovered | 37 |
| URLs accepted | 33 |
| URLs rejected | 4 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 743815.7 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
