# Chunking Audit

**Generated:** 2026-07-11T13:38:49+00:00

## Instrumentation status

Production artifacts **do not persist chunk arrays** (no `chunks[]`, no overlap metadata, no semantic split logs).

Therefore chunk metrics are **derived**:

- If extraction operates on the full stored body as one window → `chunk_count = 1`
- If no usable text → `chunk_count = 0`

This matches observed extractor versions: `acquisition-library-1.0.0`, `acquisition-grounded-2.0.0` (candidate notes show single evidence snippets).

## Derived chunk statistics (all processed docs)

| Metric | Value |
|--------|------:|
| Docs | 105 |
| Mean chunk_count | 0.895 |
| Median chunk_count | 1 |
| Mean avg_chunk chars | 1942.2 |
| Max max_chunk | 8000 |
| Min min_chunk (nonzero) | 112 |
| Semantic split evidence | **None in artifacts** |
| Overlap evidence | **None in artifacts** |

## Flags

| Flag | Count | % |
|------|------:|--:|
| UNDERCHUNKED | 81 | 77.14% |
| NORMAL | 24 | 22.86% |

### Interpretation

- **UNDERCHUNKED** dominates because each document is a single small window (median words **21**).  
- **OVERCHUNKED** is not observed.  
- Chunk utilization for multi-entity extraction is poor: one window → typically one candidate.

## Latest 20 docs chunk view

| Document | Chars | Chunks | Flag | Connector |
|----------|------:|-------:|------|-----------|
| DOC-145FF9472A86 | 135 | 1 | UNDERCHUNKED | CONN-WB-001 |
| DOC-6869936E8E0F | 4523 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-5BB66628524B | 3780 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-8628C05DC1C0 | 2680 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-603F522CB0E1 | 4495 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-B25B54E1F2DA | 1427 | 1 | NORMAL | CONN-CROSSREF-001 |
| DOC-DE703E3E299C | 3084 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-C7C877E9C1BB | 4073 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-34E8BEF02B21 | 5470 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-FD186A8BEB53 | 140 | 1 | UNDERCHUNKED | CONN-WB-001 |
| DOC-7C8A8F6C80DA | 1414 | 1 | NORMAL | CONN-CROSSREF-001 |
| DOC-D30300A2A993 | 2029 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-58D299E0DC0F | 1301 | 1 | NORMAL | CONN-CROSSREF-001 |
| DOC-16F07AB3FE63 | 1307 | 1 | NORMAL | CONN-CROSSREF-001 |
| DOC-B4143B31E4B8 | 1404 | 1 | NORMAL | CONN-CROSSREF-001 |
| DOC-BA3537A9ABF7 | 3412 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-C99CC537BBBA | 1250 | 1 | NORMAL | CONN-CROSSREF-001 |
| DOC-C9CE5A00BB24 | 1872 | 1 | UNDERCHUNKED | CONN-CROSSREF-001 |
| DOC-BE5EF0355380 | 119 | 1 | UNDERCHUNKED | CONN-WB-001 |
| DOC-22BF455AD301 | 1387 | 1 | NORMAL | CONN-CROSSREF-001 |

## Conclusion

Chunking is not the primary loss mechanism — **there is almost nothing to chunk**. Full-text acquisition must precede chunk strategy work.
