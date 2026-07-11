# Regulation Coverage

**Generated:** 2026-07-11T06:11:47.381806+00:00  
**Dataset:** `regulation_library`  
**Rows:** 5  

## Production status

| Field | Value |
|-------|------:|
| Rows | 5 |
| Store | `domains/business_development/regulation_library.csv` |
| Extractor | grounded (`library_extract.py`) |
| Mission batch | continuous + mission selector eligible |

## Trusted source mapping

JDIH, OJK, Kemnaker, Kemendag, BKPM, LKPP, OSS, BPK, Kementerian + OECD/WB

## Extraction fields (grounded only)

law, issuer, effective date, scope, industry

## Sample published entities

- Indonesia: GDP, education, product market regulation, employment
- Regulation Dataset — employment regulation Indonesia World Bank document related
- Regulation of regular and temporary employment {"status":"ok","message-type":"wo
- Regulation of regular and temporary employment","reference-count":0,"publisher":
- Regulation of regular and temporary employment"],"prefix":"10

## Eligibility path

Eligible → Scheduled (selector / continuous catalog) → Executed (`run_acquisition` with dataset route) → Published (append-only CSV)

## Notes

No blogs. No AI-invented facts. Empty fields when document lacks evidence.
