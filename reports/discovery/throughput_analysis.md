# Throughput Analysis

**Generated:** 2026-07-11T11:54:23+00:00

## Last discovery session

| Metric | Value |
|--------|------:|
| Queries generated | 37 |
| Queries executed | 85 |
| URLs discovered | 595 |
| URLs accepted | 248 |
| URLs rejected | 347 |
| URLs remaining (budget − accepted) | 0 |
| Elapsed ms | 51750.1 |
| Stop reason | completed |

## Bottleneck diagnosis

- ACTIVE providers: 6
- MISCONFIGURED providers: 6
- Typical low session (~10 discovered / ~5 downloaded) matches feed-only path + previous hard caps (max_urls=20, discover limit=5).
- Engine works; discovery breadth was limited by credentials + artificial caps.
