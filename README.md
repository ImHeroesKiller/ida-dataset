# IDA Dataset

Scalable knowledge repository for the IDA Executive AI platform.

## Contents

| Path | Purpose |
| --- | --- |
| `domains/` | Domain knowledge datasets (CSV) |
| `metadata/ontology/` | Knowledge Ontology Engine (KOE) |
| `automation/` | Knowledge Acquisition System (KAS) + CI tools |
| `ecc/` | **Executive Control Center** (Next.js dashboard) |
| `reports/` | Validation / planner / review / publish reports |
| `docs/` | Architecture and operations docs |

## Executive Control Center (web UI)

```bash
cd ecc
npm install
npm run dev
```

### Deploy on Vercel

1. Import this GitHub repository  
2. **Root Directory must be `ecc`** (Project Settings → General)  
3. Deploy  

See [docs/vercel.md](docs/vercel.md).

## Knowledge control flow

```text
Planner → Policy → Pipeline → Review → Publisher
```

Human-controlled. Not autonomous.
