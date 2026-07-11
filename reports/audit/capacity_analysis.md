# Capacity Analysis

**Generated:** 2026-07-11T13:39:39+00:00

## Current output

| Metric | Value |
|--------|------:|
| Trace published | 110 |
| Trace discovered | 346 |
| Processed docs | 105 |
| Session knowledge_added | 40 |
| Session knowledge_rejected | 6 |
| Last rows/hour | 14.3 |
| Last docs/hour | 71.51 |

## Theoretical scenarios

| Scenario | Result |
|----------|-------:|
| Current published (traces) | 110 |
| If 1 row per downloaded | 206 |
| Usable docs × 1 | 0 |
| Usable × 3 entities | 0 |
| Usable × 3 entities × 4 datasets | 0 |
| All discoveries × 1 row | 346 |
| All discoveries × 4 datasets | 1384 |

```
346 discovered (trace sum)
  ↓ current
110 published
  ↓ potential multi-map on usable stored docs
~0 rows
```

## WHY

1. Only 59.54% discoveries download  
2. Only 50.48% stored docs yield candidates  
3. 42.86% docs → single dataset  
4. Median words = 0  
5. PDFs = 0

## Stage timings (session-level)

| Stage | N | Avg ms | Max ms |
|-------|--:|-------:|-------:|
| document_download | 23 | 29609.9 | 49397.5 |
| document_discovery | 23 | 13320.3 | 93987.8 |
| connector | 23 | 13320.1 | 93987.7 |
| extraction | 23 | 29.9 | 78.5 |
| append_dataset | 23 | 8.8 | 45.5 |
| publish_queue | 23 | 4.7 | 15.2 |
| candidate_validation | 23 | 4.7 | 15.2 |
| source_discovery | 23 | 2.0 | 2.8 |
| mission | 23 | 0.7 | 1.2 |
| export | 23 | 0.3 | 0.6 |
| git_commit | 23 | 0.3 | 0.6 |
| push | 23 | 0.3 | 0.4 |
