# Throughput Analysis

**Generated:** 2026-07-11T12:20:31+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 37 |
| Queries executed | 93 |
| URLs discovered | 313 |
| URLs accepted | 273 |
| URLs rejected | 40 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 513140.2 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 5
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
