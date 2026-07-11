# Architecture — IDA Dataset Factory

## Pipeline

```text
Mission → Source Discovery → Document Collection → Extraction →
Normalization → Validation → Schema Mapping → Append Dataset →
Quality Validation → Export → Dashboard Update
```

## Packages

| Package | Role |
|---------|------|
| `automation/collector` | Trusted source acquisition (`connectors`) |
| `automation/extractor` | Entity extraction / normalize |
| `automation/validator` | Schema, confidence, duplicates |
| `automation/publisher` | Append-only dataset write |
| `automation/quality` | Growth & quality metrics |
| `automation/export` | JSONL / OpenAI / HF packages |
| `automation/missions` | Mission definitions |
| `automation/scheduler` | Priority & dispatch |
| `automation/ci` | GHA job entrypoints |
| `automation/config` | Sources, policies, scheduler |

## UI

Next.js App Router **Operator UI v1.0 (FROZEN)**:

Dashboard · Mission · Sources · Export · Settings  

Compact console typography · operator status language · no further UI expansion.  
(Datasets/Quality/Logs merged into Export + bottom console.)

## Deploy

- Root Directory: repository root  
- Output: default `.next`  
- Region: `sin1`  
- See `vercel.json`  

## Data

- `domains/` — product datasets (append-only)  
- `metadata/` — schemas, source registry  
- `exports/` — generated training packages  
- `reports/` — quality / publish / export reports  
