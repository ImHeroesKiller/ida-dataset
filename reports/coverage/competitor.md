# Competitor Coverage

**Generated:** 2026-07-11T06:11:47.381806+00:00  
**Dataset:** `competitor_library`  
**Rows:** 6  

## Production status

| Field | Value |
|-------|------:|
| Rows | 7 |
| Store | `domains/business_development/competitor_library.csv` |
| Extractor | grounded (`library_extract.py`) |
| Mission batch | continuous + mission selector eligible |

## Trusted source mapping

Official company docs, annual reports, public catalogs, procurement, BEI, BKPM

## Extraction fields (grounded only)

company, product, service, strength, weakness, market

## Sample published entities

- PT Alcomex Indo
- PT. Primacon Mahatama Sejahtera
- PT Indoptune Net Manufacturing
- PT Indoneptune Net Mfg
- PT Indoeptune Net Mfg

## Eligibility path

Eligible → Scheduled (selector / continuous catalog) → Executed (`run_acquisition` with dataset route) → Published (append-only CSV)

## Notes

No blogs. No AI-invented facts. Empty fields when document lacks evidence.
