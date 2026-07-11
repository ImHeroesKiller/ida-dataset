# Trend Coverage

**Generated:** 2026-07-11T06:11:47.381806+00:00  
**Dataset:** `trend_library`  
**Rows:** 10  

## Production status

| Field | Value |
|-------|------:|
| Rows | 10 |
| Store | `domains/business_development/trend_library.csv` |
| Extractor | grounded (`library_extract.py`) |
| Mission batch | continuous + mission selector eligible |

## Trusted source mapping

OECD, World Bank, OpenAlex, Crossref, RSS, official newsrooms

## Extraction fields (grounded only)

title, direction, industry, time, signal

## Sample published entities

- World Bank document
- INFLUENCE OF THE DIGITAL ECONOMY ON THE TRENDS OF THE MODERN LABOR MARKET
- University’s Cultivation Model Transformation Under Labor Market New Trends In D
- Labor market trends in the digital economy
- The labor market conjuncture assessment in the digital economy

## Eligibility path

Eligible → Scheduled (selector / continuous catalog) → Executed (`run_acquisition` with dataset route) → Published (append-only CSV)

## Notes

No blogs. No AI-invented facts. Empty fields when document lacks evidence.
