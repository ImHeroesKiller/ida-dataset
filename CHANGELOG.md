# Changelog

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
