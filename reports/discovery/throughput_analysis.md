# Throughput Analysis

**Generated:** 2026-07-16T00:13:20+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 32 |
| URLs discovered | 196 |
| URLs accepted | 150 |
| URLs rejected | 46 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 773859.6 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
