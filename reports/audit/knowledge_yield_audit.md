# Knowledge Yield Audit

**Generated:** 2026-07-11T13:38:49+00:00

## Corpus inventory

| Artifact | Count |
|----------|------:|
| Processed documents | 105 |
| Candidates (deduped queue) | 106 |
| Production traces | 23 |
| Sessions | 39 |
| Trace document events | 206 |
| Lifecycles built (latest docs) | 100 |

## Aggregate funnel (all production traces)

```
346 discovered
  ↓  59.54% retained
206 downloaded
  ↓  (+ 156 marked duplicate/skipped in summaries)
130 candidates extracted
  ↓  89.23% 
116 validated
  ↓  94.83%
110 published
```

| Conversion | Ratio |
|------------|------:|
| Discovery → Download | 59.54% |
| Download → Extract | 63.11% |
| Extract → Validate | 89.23% |
| Validate → Publish | 94.83% |
| Discovery → Publish | 31.79% |
| Download → Publish | 53.4% |

## Last acquisition snapshot (`acquisition_performance.json`)

| Field | Value |
|-------|------:|
| Downloads requested | 20 |
| Downloaded | 7 |
| Failed | 13 |
| Skipped duplicate | 0 |
| Fingerprint skips | 7 |
| Extraction | {"fast": 5, "medium": 0, "deep": 0, "llm": 0, "llm_used": 0, "skipped_llm": 25, "llm_skipped": 25, "documents_fast": 13, "documents_medium": 8, "documents_deep": 4, "avg_ms": 1.31, "average_extraction |
| Publish | {"extracted": 5, "validated": 5, "rejected": 0, "queued": 5, "published": 5, "skipped": 0, "duplicate": 0, "by_dataset": {"business_signal_library": 5}} |
| Throughput docs | 25 |
| Throughput rows | 5 |
| Docs/hour | 71.51 |
| Rows/hour | 14.3 |

## Last discovery snapshot

| Metric | Value |
|--------|------:|
| URLs discovered | 595 |
| URLs accepted | 248 |
| URLs rejected | 347 |
| Queries executed | 85 |
| Stop reason | completed |

## Session knowledge totals

| Metric | Value |
|--------|------:|
| knowledge_added (sum) | 40 |
| knowledge_rejected (sum) | 6 |
| Sessions | 39 |
| Mean knowledge_added/session | 1.026 |

## Document → candidate yield (corpus)

| Metric | Value |
|--------|------:|
| Docs with ≥1 candidate | 53 |
| Docs with 0 candidates | 57 |
| Candidates / doc (mean over docs w/ cands) | 2 |
| Candidates / doc (mean all docs) | 1.01 |

## Why thousands of discoveries become few rows

Measured chain (last discovery + last acq + corpus):

1. Discovery may return hundreds of URLs (**595** last run)  
2. Trusted filter accepts **248**  
3. Process/download budget + connector path downloads far fewer (**7** last acq; trace download total **206**)  
4. Many downloads are short JSON/HTML (**median 1652 chars**)  
5. Extraction yields ~1 candidate for the **mission dataset only**  
6. Publish appends few rows per session (session mean **1.026**)

**Primary yield break is not validation rejects** (trace rejected=20, published=110).  
**Primary yield break is low candidates-per-document × single-dataset mapping × thin source bodies × discovery-to-download budget.**
