# Throughput Analysis

**Generated:** 2026-08-02T22:13:36+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 27 |
| URLs discovered | 84 |
| URLs accepted | 46 |
| URLs rejected | 38 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 771332.5 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
