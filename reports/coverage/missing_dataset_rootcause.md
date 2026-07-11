# Missing Dataset Root Cause

**Generated:** 2026-07-11T06:11:47.381806+00:00  
**Status:** Production freeze active — analysis + production enablement only  

## Symptom

| Dataset | Rows before sprint | Rows after enablement |
|---------|-------------------:|----------------------:|
| buyer_persona_library | 0 (no CSV) | 4 |
| decision_maker_library | 0 (no CSV) | 3 |
| regulation_library | 0 (no CSV) | 5 |
| risk_library | 0 (no CSV) | 10 |
| trend_library | 0 (no CSV) | 10 |
| competitor_library | 0 (header only) | 7 |

## Root causes (real system)

### 1. No durable store (CSV missing)

Five libraries had **no** `domains/business_development/*.csv` file.  
Mission selector treated `buyer_persona_library` / `regulation_library` as `logical_only` and hard-coded counts to **0**.  
Publisher path `domains/business_development/{dataset}.csv` could not append.

### 2. Extraction never routed to these datasets

`extract_staged` only ran:
- `extract_industry_candidates`
- `extract_business_signal_candidates` (fallback)

There were **no** grounded extractors for persona / decision maker / regulation / risk / trend / competitor.

### 3. Live runtime always defaulted to industry

`run_live_session(dataset="industry_library")` and learning CI telemetry hard-coded `dataset: industry_library`.  
Even when mission selector chose Batch-009 Buyer Persona, acquisition still extracted industry rows.

### 4. Continuous catalog starvation / mis-route

`learning.yaml` continuous catalog:
- Competitor was P2 only
- Regulation task pointed at **framework_library** (wrong target)
- No buyer persona / decision maker / risk / trend continuous tasks

### 5. Source mapping incomplete

Trusted sources `allowed_datasets` rarely included the six libraries, so adaptive source selection under-weighted them.

### 6. Integrity guard unaware of new ID schemas

`ID_FIELDS` / `ID_PATTERNS` omitted PER / DM / REG / RISK / TRD prefixes (competitor CMP already present).

## Why not permanently blocked by dependencies?

Industry (~53) and company (~86) baselines already satisfy hard deps for these libraries.  
Selector *could* schedule Buyer Persona (Batch-009) and did rank it first — production still failed because of stores + extraction + routing.

## Fix summary (this sprint)

| Layer | Fix |
|-------|-----|
| Store | Created dedicated CSVs + schemas |
| Extraction | `library_extract.py` grounded extractors |
| Routing | `dataset_routing.py` + live_runtime/CI dataset pass-through |
| Selector | Real counts; Batch-010/013/014; anti-starvation score |
| Continuous | learning.yaml missions for all six |
| Sources | Expanded `allowed_datasets` |
| Integrity | ID patterns for new libraries |
| Test | Real connector missions published rows (trusted sources only) |

## Residual risks

- Competitor name extraction remains precision-sensitive (PT/Ltd patterns only)
- Decision-maker yield depends on role language in documents
- Some connectors return metadata-only pages → lower field density

