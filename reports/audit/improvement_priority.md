# Improvement Priority (Audit Only)

**Generated:** 2026-07-11T13:39:39+00:00

| Pri | Item | Evidence | Upside | Risk | Frozen surface |
|----:|------|----------|--------|------|----------------|
| 1 | Multi-dataset / multi-entity extraction | multi-map 2.86%; mean 1.01 cand/doc | High (~135+) | Medium | Extractor |
| 2 | Full-text/PDF acquisition | 0 PDFs; 76.19% JSON | Very high | Medium | Acquisition |
| 3 | Download more accepted discovery URLs | accepted 248 vs DL 7; disc→dl 59.54% | Medium | Low–Med | Acquisition budgets |
| 4 | Duplicate skip precision | 156 dups | Medium | Medium | Fingerprints |
| 5 | Semantic chunking | UNDERCHUNKED but thin bodies | Low until #2 | Low | Parser/extract |
| 6 | Integrity duplicate_id policy | lifecycle blocks | Low–Med | **High** | Validator |

## Do not prioritize first

Dashboard redesign · UI · OCR before PDFs · Softening integrity without dedup strategy

## Next-sprint KPI signals

| KPI | Current |
|-----|---------|
| Cand/doc | 1.01 |
| Multi-dataset % | 2.86% |
| PDF share | 0.0% |
| Disc→Publish | 31.79% |
| Rows/hour last | 14.3 |
