# Throughput Analysis

**Generated:** 2026-07-11T14:45:55+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 37 |
| Queries executed | 91 |
| URLs discovered | 288 |
| URLs accepted | 262 |
| URLs rejected | 26 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 501609.4 |
| Stop reason | runtime_budget_reached |

## Bottleneck diagnosis

- ACTIVE providers: 7
- MISCONFIGURED providers: 5
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
