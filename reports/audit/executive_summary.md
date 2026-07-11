# Executive Summary — Knowledge Yield Forensic Audit

**Generated:** 2026-07-11T13:39:39+00:00  
**Mode:** OBSERVATION ONLY — no production code modified  
**Evidence:** 105 processed documents · 106 candidates · 23 production traces · 39 sessions · discovery + acquisition state  

---

## Measured funnel (all production traces)

```
346 discovered
  ↓ 59.54%
206 downloaded   (+ 156 document duplicates skipped)
  ↓ 63.11%
130 candidates extracted
  ↓ 89.23%
116 validated
  ↓ 94.83%
110 published
```

| Conversion | % |
|------------|--:|
| Discovery → Download | 59.54 |
| Download → Extract | 63.11 |
| Extract → Validate | 89.23 |
| Validate → Publish | 94.83 |
| **Discovery → Publish** | **31.79** |

Last discovery snapshot: **595** URLs discovered · **248** accepted.  
Session `knowledge_added` sum: **40**.

---

## 1. Biggest bottleneck

**Pre-download duplicate document skips**

- Score: **156**
- Evidence: 156

Pre-download fingerprint/duplicate classification removes **156** docs across traces while only **206** download — nearly as large as the download set itself.

---

## 2. Second bottleneck

**Discovery→Download drop (trace aggregate)**

- Score: **140**
- Evidence: 346→206

**59.54%** of discoveries become downloads. Remainder are never parsed or extracted.

---

## 3. Third bottleneck

**Single-dataset mapping (missed multi-library rows)**

- Score: **135**
- Evidence: 45 single-ds docs ×3

Corpus mapping of 105 stored docs:

| Mapping | N | % |
|---------|--:|--:|
| 0 datasets | 57 | 54.29 |
| 1 dataset | 45 | 42.86 |
| ≥2 datasets | 3 | 2.86 |

Docs with zero candidates: **57** (54.29%).

---

## Content reality (parser is not the PDF-page problem)

| Metric | Value |
|--------|------:|
| PDFs in processed corpus | **0** |
| JSON API share | **76.19%** |
| Multi-dataset docs | 3 (2.86%) |

**CRITICAL (reclassified):** Not “parser only reads first pages.”  
**CRITICAL:** Factory acquires **API JSON / thin HTML**, not full reports — 0 PDFs; extraction has little text to mine.

---

## 4. Estimated row loss

| Channel | Units |
|---------|------:|
| Discoveries not published (E2E) | 236 |
| Discoveries not downloaded | 140 |
| Document dups skipped | 156 |
| Downloaded − extracted (cand gap) | 76 |
| Validated − published | 6 |
| Rejected candidates (trace) | 20 |
| Single-dataset under-map (est. ×3) | ~135 |

---

## 5. Estimated recoverable rows

| Lever | Est. |
|-------|-----:|
| Multi-map on single-dataset docs (×3) | ~135 |
| Extract ≥1 cand from zero-cand usable docs | see capacity report |
| Aggressive usable×3 entities×4 datasets | see capacity (~usable×12) |
| Close disc→dl gap (if each dl → 1 row) | up to ~140 |

---

## 6. Highest ROI improvement

**Multi-entity + multi-dataset extraction**, then **full-text/PDF acquisition**.

Why (measured): Validate→Publish is already **94.83%** when candidates exist. The factory does not *lose* most rows in validation — it **never creates** multi-library candidates and often never downloads discoveries.

---

## 7. Risk of changing it

| Change | Risk |
|--------|------|
| Multi-dataset extract | Medium (extractor frozen until approved sprint) |
| Full-text/PDF path | Medium (acquisition/parser) |
| Loosen fingerprint dups | Medium (may reprocess true dups) |
| Soften integrity `duplicate_id` | **High** (dataset pollution) |

---

## 8. Recommended implementation order

1. Multi-dataset / multi-entity extraction design  
2. Full-text/PDF acquisition for scholarly + institutional sources  
3. Improve discovery→download conversion (budget + false-dup reduction)  
4. Chunking/OCR only after full-text exists  
5. Integrity duplicate policy last  

---

## Stage loss ranking

| Rank | Transition | From | To | Loss % |
|-----:|------------|-----:|---:|-------:|
| 1 | Discovery → Publish (E2E) | 346 | 110 | 68.21% |
| 2 | Discovery → Download | 346 | 206 | 40.46% |
| 3 | Download → Extraction (candidates) | 206 | 130 | 36.89% |
| 4 | Extraction → Validation | 130 | 116 | 10.77% |
| 5 | Validation → Publish | 116 | 110 | 5.17% |
| 6 | Download → Parsed (proxy=downloaded) | 206 | 206 | 0.0% |

---

## Answers (evidence only)

| # | Answer |
|---|--------|
| 1 | Pre-download duplicate document skips |
| 2 | Discovery→Download drop (trace aggregate) |
| 3 | Single-dataset mapping (missed multi-library rows) |
| 4 | E2E non-publish leave-behind **236** discoveries; under-map ~**135** |
| 5 | Conservative ~**135+** multi-map; larger if full-text + disc→dl closed |
| 6 | Multi-dataset/multi-entity extraction (+ full-text next) |
| 7 | Medium for extract/full-text; High for integrity soften |
| 8 | Multi-map extract → full-text → download conversion → chunking → integrity |

---

*Supporting reports in `reports/audit/`. Lifecycles: `document_lifecycle_latest_100.md`. Metrics: `audit_metrics.json`.*
