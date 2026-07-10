# IDA Dataset

Scalable knowledge repository for the IDA Executive AI platform, including the **Executive Control Center** web UI.

## Contents

| Path | Purpose |
| --- | --- |
| `app/` `components/` `lib/` | Executive Control Center (Next.js) |
| `domains/` | Domain knowledge datasets (CSV) |
| `metadata/ontology/` | Knowledge Ontology Engine (KOE) |
| `automation/` | Knowledge Acquisition System (KAS) + CI tools |
| `reports/` | Validation / planner / review / publish reports |
| `docs/` | Architecture and operations docs |

## Run the dashboard

```bash
npm install
npm run dev
```

Open http://localhost:3000

### Deploy on Vercel

1. Import this GitHub repository  
2. **Root Directory: leave empty** (repo root)  
3. Framework: **Next.js**  
4. Deploy  

See [docs/vercel.md](docs/vercel.md).

## Knowledge control flow

```text
Scheduler → Planner → Policy → Pipeline → Review → Publisher
```

Continuous Learning never stops. Directed Learning missions coexist.

```bash
python -m automation.scheduler mission "Learn everything about SAP ERP."
python -m automation.scheduler tick --dry-run
python -m automation.connectors health
python -m automation.search "Indonesian manufacturing" --limit 5
```

Human-controlled. Not autonomous. Knowledge Network acquires documents only (no direct dataset writes).

