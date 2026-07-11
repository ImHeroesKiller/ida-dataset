# Parser Audit

**Generated:** 2026-07-11T13:38:49+00:00

## Scope of evidence

Per-document parser instrumentation (pages parsed, OCR, encrypted flags, skip lists) is **NOT present** in production document JSON. Audit uses:

- `content_type`, `bytes`, `local_path` raw body
- Visible text after HTML tag strip
- Absence of PDF binaries in `automation/raw_documents`

## Corpus parser input types

| Content type | Count | % |
|--------------|------:|--:|
| application/json | 80 | 76.19% |
| text/plain | 19 | 18.1% |
| text/html | 6 | 5.71% |

## PDF page analysis

| Metric | Value | Evidence |
|--------|------:|----------|
| Total PDF documents | **0** | content_type/path scan of 105 docs |
| Pages total | n/a | no PDFs |
| Pages parsed | n/a | no PDFs |
| Skipped / broken / OCR / encrypted pages | n/a | no PDFs |

### CRITICAL?

**No PDF multi-page truncation issue can be measured — because the factory is not acquiring PDFs.**

If the product expectation is annual reports / full WDS PDFs, the critical finding is:

> **Parser never sees full documents; acquisition stores API JSON and small HTML shells instead.**

## HTML / JSON parse completeness (measured)

| Class | Count | Definition |
|-------|------:|------------|
| JSON API payload | 80 | application/json or body starts with `{`/`[` |
| HTML shell (chars&lt;500 after strip) | 5 | HTML with almost no readable text |
| Usable text chars≥200 | 86 | extractable prose/metadata |
| Empty/near-empty chars&lt;50 | 11 | |

## Tables / images / references (regex on raw body)

| Signal | Docs with ≥1 hit | Method |
|--------|----------------:|--------|
| Tables | 80 | regex table markers |
| Images | 1 | regex img/figure |
| References | NOT INSTRUMENTED as structured field | — |
| Appendices | NOT INSTRUMENTED | — |

## Metadata extracted?

| Metric | Value |
|--------|------:|
| Docs with metadata object | 105 / 105 |

## Conclusion

1. **Entire-document parse of PDFs:** N/A (0 PDFs).  
2. **For JSON records:** body is fully stored (median 1735 bytes) — parser is not page-limiting; **source body is the limit**.  
3. **CRITICAL (reclassified):** Knowledge starvation is **upstream of parser** (document type acquired), not partial PDF page reads.
