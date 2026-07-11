# Decision Maker Coverage

**Generated:** 2026-07-11T06:11:47.381806+00:00  
**Dataset:** `decision_maker_library`  
**Rows:** 3  

## Production status

| Field | Value |
|-------|------:|
| Rows | 3 |
| Store | `domains/business_development/decision_maker_library.csv` |
| Extractor | grounded (`library_extract.py`) |
| Mission batch | continuous + mission selector eligible |

## Trusted source mapping

Annual reports, company profiles, government institutions, org structures

## Extraction fields (grounded only)

title, authority, department, responsibility, approval chain

## Sample published entities

- Director
- Manager
- Board of Directors

## Eligibility path

Eligible → Scheduled (selector / continuous catalog) → Executed (`run_acquisition` with dataset route) → Published (append-only CSV)

## Notes

No blogs. No AI-invented facts. Empty fields when document lacks evidence.
