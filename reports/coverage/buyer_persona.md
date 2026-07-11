# Buyer Persona Coverage

**Generated:** 2026-07-11T06:11:47.381806+00:00  
**Dataset:** `buyer_persona_library`  
**Rows:** 4  

## Production status

| Field | Value |
|-------|------:|
| Rows | 4 |
| Store | `domains/business_development/buyer_persona_library.csv` |
| Extractor | grounded (`library_extract.py`) |
| Mission batch | continuous + mission selector eligible |

## Trusted source mapping

BPS, Kemnaker, ILO, World Bank, OECD, APINDO, KADIN

## Extraction fields (grounded only)

industry, company size, job role, pain, goal, budget, behavior

## Sample published entities

- Industry Buyer — Manufacturing
- Industry Stakeholder — Banking
- Industry Buyer — Mining & Quarrying
- Industry Buyer — Manufacturing

## Eligibility path

Eligible → Scheduled (selector / continuous catalog) → Executed (`run_acquisition` with dataset route) → Published (append-only CSV)

## Notes

No blogs. No AI-invented facts. Empty fields when document lacks evidence.
