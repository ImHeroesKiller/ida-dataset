# Changelog

## 2.0 — Production Freeze — 2026-07-11

### Governance

- **Production Freeze Declaration** active ([PRODUCTION_FREEZE.md](./PRODUCTION_FREEZE.md))
- Core architecture, queues, mission engine, acquisition, connectors, DPS, dashboard, and exports declared **FROZEN**
- Growth strategy: **knowledge expansion only** (connectors, datasets, coverage, quality, production fixes)
- Forbidden: architecture/schema/queue redesign, RAG, agents, decision/reasoning engines

### Dataset coverage completion (P0 — no architecture change)

- Enabled continuous production for Buyer Persona, Decision Maker, Regulation, Risk, Trend, Competitor
- Dedicated CSVs + grounded extractors + mission/dataset routing
- Continuous catalog + selector anti-starvation so libraries are never permanently blocked
- Root-cause and coverage reports under `reports/coverage/`

### Performance (throughput — no architecture change)

- Adaptive document prioritization + pre-download dedupe; process budget targets ≥90% of discovered docs
- Concurrent downloads with adaptive worker pool (2→4→8→16) from connector latency
- Multi-stage extraction: fast / medium / deep; LLM skipped when deterministic extraction suffices
- Auto-publish gate at confidence ≥0.92; lower confidence → manual review queue
- Queue rebalance drains leftover incoming documents into the active session
- Per-session document budget raised (32) within policy hard caps
- Performance reports under `reports/performance/` (bottleneck, capacity, queues, connectors)
- Dashboard metrics only: rows/hour, docs/hour, worker utilization, queue depth, process ratio

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
