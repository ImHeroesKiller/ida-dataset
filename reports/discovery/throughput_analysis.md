# Throughput Analysis

**Generated:** 2026-07-11T12:46:46+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 35 |
| Queries executed | 115 |
| URLs discovered | 1042 |
| URLs accepted | 596 |
| URLs rejected | 446 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 803686.6 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 5
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
