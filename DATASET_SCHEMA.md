# Dataset Schema

Schemas live under `metadata/schema/`.

Primary domain (Business Development):

| Dataset | Path |
|---------|------|
| Industry Library | `domains/business_development/industry_library.csv` |
| Company Profile | `domains/business_development/company_profile.csv` |
| Pain Point Library | `domains/business_development/pain_point_library.csv` |
| Solution Library | `domains/business_development/solution_library.csv` |
| … | See `metadata/schema/*.md` |

## Rules

1. **Do not change column headers** without a versioned migration.  
2. **Append-only** for verified rows.  
3. Encode provenance in dataset fields (Data Sources / Notes) and/or companion metadata:  
   - Source  
   - Published / Retrieved dates  
   - Confidence  
   - Version  

## Industry Library (32 columns)

See `metadata/schema/industry_library.md` and header row of `industry_library.csv`.
