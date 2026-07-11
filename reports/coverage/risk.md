# Risk Coverage

**Generated:** 2026-07-11T06:11:47.381806+00:00  
**Dataset:** `risk_library`  
**Rows:** 10  

## Production status

| Field | Value |
|-------|------:|
| Rows | 10 |
| Store | `domains/business_development/risk_library.csv` |
| Extractor | grounded (`library_extract.py`) |
| Mission batch | continuous + mission selector eligible |

## Trusted source mapping

OECD, World Bank, ADB, IMF, ILO, OJK, BPS

## Extraction fields (grounded only)

type, probability, impact, mitigation

## Sample published entities

- Regulatory Risk — Banking
- Risk — Banking
- Liquidity Risk — Banking
- Operational Risk — Manufacturing
- Risk — Manufacturing

## Eligibility path

Eligible → Scheduled (selector / continuous catalog) → Executed (`run_acquisition` with dataset route) → Published (append-only CSV)

## Notes

No blogs. No AI-invented facts. Empty fields when document lacks evidence.
