# Changelog

## 2.0 — Production Freeze — 2026-07-11

### Governance

- **Production Freeze Declaration** active ([PRODUCTION_FREEZE.md](./PRODUCTION_FREEZE.md))
- Core architecture, queues, mission engine, acquisition, connectors, DPS, dashboard, and exports declared **FROZEN**
- Growth strategy: **knowledge expansion only** (connectors, datasets, coverage, quality, production fixes)
- Forbidden: architecture/schema/queue redesign, RAG, agents, decision/reasoning engines

## 2.0.0 — 2026-07-10

### IDA Dataset Factory (Knowledge Factory reset)

- Product rebranded to **IDA Dataset Factory**
- UI reduced to factory surfaces: Dashboard, Datasets, Missions, Sources, Quality, Exports, Logs, Settings
- Removed ECC / brain / ontology / network / planner product surfaces
- Official pipeline packages: collector · extractor · validator · publisher · quality · export
- Factory KPIs on dashboard
- Export packager: JSONL · OpenAI fine-tune · Hugging Face
- GHA: `validate` · `learn` · `quality` · `publish` · `export`
- Charter docs at repository root
- Domain datasets preserved (append-only)

## 0.1.x — prior

Legacy ECC + continuous learning architecture (archived under `docs/archive/`).
