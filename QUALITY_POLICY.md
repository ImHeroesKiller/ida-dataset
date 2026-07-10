# Quality Policy

## Required provenance (every published row)

| Field | Requirement |
|-------|-------------|
| Source | Trusted source id/name/url |
| Retrieved date | ISO timestamp of acquisition |
| Confidence | 0–1 validator score |
| Version | Extraction / knowledge version |

## Checks

| Check | Description |
|-------|-------------|
| Schema completeness | Required columns filled |
| Duplicate detection | Entity id / canonical name |
| Freshness | Prefer rows updated within policy window |
| Validation result | Pass before publish |
| No placeholders | Reject `example.invalid` / fake URLs |

## Factory KPIs

- Rows added today / week / month  
- Dataset coverage  
- Quality score  
- Average confidence  
- Duplicate rate  
- Schema completeness  
- Source freshness  
- Mission success rate  
- Exports generated  

## Append-only

Never delete verified knowledge rows. Corrections = new versioned rows or controlled update with audit.
