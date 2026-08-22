# Throughput Analysis

**Generated:** 2026-08-22T03:05:54+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 21 |
| URLs discovered | 52 |
| URLs accepted | 32 |
| URLs rejected | 20 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 609297.2 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
