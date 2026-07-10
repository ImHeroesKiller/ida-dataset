# Mission Library — IDA Dataset Factory

Missions are **production jobs** that tell the factory *what dataset to grow*.  
They are not AI agents and not decision workflows.

Missions **execute production batches**. Sequence authority:

| Document | Role |
|----------|------|
| [docs/PRODUCTION_BATCH_LIBRARY.md](./docs/PRODUCTION_BATCH_LIBRARY.md) | Batch catalog |
| [docs/DATASET_DEPENDENCY_MATRIX.md](./docs/DATASET_DEPENDENCY_MATRIX.md) | Dependencies |
| [docs/PRODUCTION_ORDER.md](./docs/PRODUCTION_ORDER.md) | Manufacturing plan |
| [docs/DATASET_PRODUCTION_STANDARD.md](./docs/DATASET_PRODUCTION_STANDARD.md) | DPS v1.0 |

---

## Mission principles

1. One mission → one primary dataset class (may touch related rows)  
2. Trusted sources only  
3. Append-only publish  
4. Provenance required  
5. Priority follows **production batch order** (dependency matrix), then lowest coverage  
6. Retry on recoverable failure  
7. Every mission reports DPS KPIs (rows added/rejected, coverage, confidence, dups, freshness, sources, duration)  

---

## Default continuous mission

| Field | Value |
|-------|--------|
| **Title** | Expand Industry Library |
| **ID** | `MIS-20260710-EXPAND-IND` / CL-IND-001 |
| **Batch** | Batch-001 (continuous) |
| **Dataset** | `industry_library` |
| **Priority** | P0 / continuous background |
| **Rule** | Grow toward product target 250; never use sprint 50 as denominator |
| **KPI** | Coverage, Quality |

---

## Next primary mission

| Field | Value |
|-------|--------|
| **Title** | Produce Service Dataset |
| **Batch** | **Batch-002** |
| **Dataset** | `service_library` (via `product_catalog` service-type rows until dedicated CSV) |
| **Dependency** | Industry (Batch-001 baseline ✅) |
| **Priority** | P0 |
| **KPI** | Coverage, Quality, Export |

---

## Production mission catalog

### Ordered by production batch

| Mission | Batch | Target dataset | Priority | Depends on | Sources (examples) | KPI |
|---------|-------|----------------|----------|------------|----------------------|-----|
| Produce Industry Dataset | 001 | industry_library | P0 | — | BPS, World Bank, OECD, Kemenperin | Coverage |
| Produce Service Dataset | 002 | service / product_catalog | P0 | Industry | Official service pages, associations | Coverage |
| Produce Product Dataset | 003 | product_catalog | P0 | Industry | Official product pages, catalogs | Coverage |
| Produce Company Dataset | 004 | company_profile | P0 | Industry + Service + Product | Annual reports, official sites, IDX | Coverage |
| Produce Pain Point Dataset | 005 | pain_point_library | P0 | Industry + Company | Industry reports, WB sector notes | Coverage |
| Produce Solution Dataset | 006 | solution_library | P0 | Pain Point | Case studies, vendor-neutral reports | Coverage |
| Produce Framework Dataset | 007 | framework_library | P1 | Solution (preferred) | Public frameworks, standards | Coverage |
| Produce Case Study Dataset | 008 | case_study_library | P1 | Company + Solution | Sustainability/annual reports | Coverage |
| Produce Buyer Persona Dataset | 009 | buyer_persona_library | P1 | Industry + Company | Industry practice, associations | Coverage |
| Produce Decision Maker Patterns | 010 | decision_maker_library | P1 | Buyer Persona | Public org charts, reports | Coverage |
| Produce Regulation Dataset | 011 | regulation_library | P1 | Industry | OJK, Kemenperin, Kemnaker, LKPP | Coverage, Freshness |
| Produce Opportunity Patterns | 012 | opportunity_analysis | P1 | Industry + Company + Pain + Solution | Public RFPs, industry signals | Coverage |
| Produce Risk Dataset | 013 | risk fields / library | P2 | Industry + Company | WB, regulators | Coverage |
| Produce Trend Dataset | 014 | trend fields / library | P2 | Industry | WB, OECD, industry reports | Coverage, Freshness |
| Produce Competitor Dataset | 015 | competitor_library | P1 | Company + Product + Service | Annual reports, public filings | Coverage |
| Produce Business Signal Dataset | 016 | business_signal_library | P2 | Industry | Official stats, market publications | Coverage |
| Produce Discovery Question Dataset | 017 | discovery_question_library | P2 | Industry + Framework + Pain + Solution | Practice guides, associations | Coverage |

### Focused vertical missions (after spine exists)

| Mission | Target | Priority | Notes |
|---------|--------|----------|-------|
| Produce Banking Dataset | industry + company + regulation focus | P1 | Requires Industry + Regulation path |
| Produce Outsourcing Dataset | industry + company + pain focus | P2 | Requires Pain Point path |

---

## Scheduling

| Trigger | Use |
|---------|-----|
| GHA `learn.yml` hourly/daily | Continuous expansion |
| Manual workflow_dispatch | Directed mission |
| Factory UI “Start factory learn” | Dispatches learn job |
| Future: mission-specific schedules | Per-dataset cadences |

---

## Priority model

| Priority | Meaning |
|----------|---------|
| P0 | Blocks coverage goals this train |
| P1 | Core production value |
| P2 | Important but deferrable |
| P3–P4 | Background / opportunistic |

**Scheduler rule:** continuous never fully stops; directed P0 can temporarily rebalance allocation without killing continuous growth.

---

## Retry policy (target)

| Failure | Action |
|---------|--------|
| Transient source error | Retry with backoff |
| Validation fail | Do not publish; log; optional re-extract |
| Duplicate | Skip or merge with provenance note |
| Hard schema fail | Fail mission step; alert quality |

---

## Mission success rate

```text
mission_success_rate = successful_or_completed_missions / total_missions
```

Tracked as an official Factory KPI.

---

## Adding a mission

1. Define target dataset + schema fields  
2. List allowed sources (registry IDs)  
3. Set priority and coverage rule  
4. Wire to learn pipeline (no new architecture)  
5. Update this library + BACKLOG epic E7  
6. Prove one successful dry-run then publish  

---

## Non-missions (forbidden)

- “Reason about a deal”  
- “Chat with executive”  
- “Build knowledge graph”  
- “Run RAG over documents for answers”  

Those are **not** Dataset Factory missions.
