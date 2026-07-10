# IDA Dataset Factory

**Automatic Knowledge Factory** — produces high-quality structured datasets for LLM fine-tuning and knowledge corpus.

> This repository is **not** an AI assistant, decision engine, or reasoning product.  
> It is a **Dataset Factory**.

## Purpose

| | |
|--|--|
| **Product** | IDA Dataset Factory |
| **Inputs** | Missions · Trusted sources · Documents · Public data |
| **Outputs** | CSV · JSON · JSONL · Parquet · HuggingFace · OpenAI fine-tuning |
| **Consumer** | IDA Intelligent Decision Automation (external) |

## Official pipeline

```text
Mission → Source Discovery → Document Collection → Extraction →
Normalization → Validation → Schema Mapping → Append Dataset →
Quality Validation → Export → Dashboard Update
```

## Quick start

```bash
npm install
npm run dev
```

Open http://localhost:3000 — **IDA Dataset Factory** dashboard.

### Factory learn (same as GitHub Actions)

```bash
python automation/ci/learning_session.py \
  --environment development \
  --dry-run
```

### Export datasets

```bash
python3 -m automation.export.packager
```

## Factory UI

| Route | Purpose |
|-------|---------|
| `/` | Factory status & KPIs |
| `/datasets` | Domain datasets |
| `/missions` | Missions |
| `/sources` | Trusted sources |
| `/quality` | Quality gates |
| `/exports` | Export artifacts |
| `/logs` | Factory activity log |
| `/settings` | Configuration |

## GitHub Actions

| Workflow | Role |
|----------|------|
| `validate.yml` | Schema / repo validation |
| `learn.yml` | Knowledge acquisition session |
| `quality.yml` | Quality checks |
| `publish.yml` | Publish pipeline |
| `export.yml` | Export packages |

## Documentation

### Product (2026–2027)

- [BACKLOG.md](./BACKLOG.md) — official product backlog (epics)
- [ROADMAP_2026_2027.md](./ROADMAP_2026_2027.md) — 30d / 90d / 6m / 12m roadmap
- [RELEASE_PLAN.md](./RELEASE_PLAN.md) — release trains
- [MILESTONES.md](./MILESTONES.md) — product milestones
- [KPI.md](./KPI.md) — factory KPIs & definition of done
- [MISSION_LIBRARY.md](./MISSION_LIBRARY.md) — production missions

### Charter & engineering

- [VISION.md](./VISION.md)
- [PROJECT_CHARTER.md](./PROJECT_CHARTER.md)
- [ROADMAP.md](./ROADMAP.md)
- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [DATASET_SCHEMA.md](./DATASET_SCHEMA.md)
- [SOURCE_POLICY.md](./SOURCE_POLICY.md)
- [QUALITY_POLICY.md](./QUALITY_POLICY.md)
- [EXPORT_GUIDE.md](./EXPORT_GUIDE.md)
- [CONTRIBUTING.md](./CONTRIBUTING.md)

## Datasets

Append-only under `domains/`. Never delete valid knowledge rows.

## Version

**2.0.0** — IDA Dataset Factory (Knowledge Factory reset)
