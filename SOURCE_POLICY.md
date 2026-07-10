# Source Policy

## Principle

Only **trusted** public sources. No random crawl. Respect robots.txt and terms.

## Phase 1 categories

- Government (BPS, BKPM, Kemnaker, Kemenperin, OSS, LKPP, OJK)  
- International (World Bank, OECD, IFC, ADB)  
- Industry (official sites, annual reports, sustainability reports)  
- Associations (APINDO, KADIN)  

## Registry

- Runtime list: `metadata/source_registry.csv`  
- Config: `automation/config/sources.yaml`  

## Allow rules

- `status=active` and `allowed=true`  
- Trust score ≥ configured minimum (`trust_score_min`)  
- Blocklist: `example.com`, `example.invalid`, localhost  

## Placeholders

Inactive placeholder sources must never produce published rows.
