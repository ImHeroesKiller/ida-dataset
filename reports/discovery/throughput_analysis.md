# Throughput Analysis

**Generated:** 2026-07-13T09:52:02+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 32 |
| URLs discovered | 207 |
| URLs accepted | 140 |
| URLs rejected | 67 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 753158.2 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
