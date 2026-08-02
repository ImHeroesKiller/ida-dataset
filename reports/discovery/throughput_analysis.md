# Throughput Analysis

**Generated:** 2026-08-02T19:23:57+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 10 |
| Queries executed | 27 |
| URLs discovered | 65 |
| URLs accepted | 51 |
| URLs rejected | 14 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 651047.9 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 0
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
