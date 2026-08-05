# Throughput Analysis

**Generated:** 2026-08-05T19:47:20+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 26 |
| URLs discovered | 32 |
| URLs accepted | 22 |
| URLs rejected | 10 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 561067.1 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
