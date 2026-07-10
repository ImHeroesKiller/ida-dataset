# Mission Library — IDA Dataset Factory

Missions are **production jobs** that tell the factory *what dataset to grow*.  
They are not AI agents and not decision workflows.

---

## Mission principles

1. One mission → one primary dataset class (may touch related rows)  
2. Trusted sources only  
3. Append-only publish  
4. Provenance required  
5. Priority prefers **lowest coverage / highest business value**  
6. Retry on recoverable failure  

---

## Default continuous mission

| Field | Value |
|-------|--------|
| **Title** | Expand Industry Library |
| **ID** | `MIS-20260710-EXPAND-IND` / CL-IND-001 |
| **Dataset** | `industry_library` |
| **Priority** | P1 / continuous |
| **Rule** | Lowest industry field coverage first |
| **KPI** | Coverage, Quality |

---

## Production mission catalog

### Industry & market

| Mission | Target dataset | Priority | Sources (examples) | KPI |
|---------|----------------|----------|----------------------|-----|
| Produce Industry Dataset | industry_library | P0 | BPS, World Bank, OECD, Kemenperin | Coverage |
| Produce Trend Dataset | trend / industry fields | P2 | WB, OECD, industry reports | Coverage, Freshness |
| Produce Risk Dataset | risk library / fields | P2 | WB, regulators | Coverage |
| Produce Competitor Dataset | competitor_library | P1 | Annual reports, public filings | Coverage |

### Company & commercial

| Mission | Target dataset | Priority | Sources | KPI |
|---------|----------------|----------|---------|-----|
| Produce Company Dataset | company_profile | P0 | Annual reports, official sites, IDX | Coverage |
| Produce Opportunity Patterns | opportunity_analysis | P2 | Public RFPs, industry signals | Coverage |
| Produce Buyer Persona Dataset | persona / discovery | P2 | Industry practice, associations | Coverage |
| Produce Decision Maker Patterns | decision maker fields | P2 | Public org charts, reports | Coverage |

### Offer & value

| Mission | Target dataset | Priority | Sources | KPI |
|---------|----------------|----------|---------|-----|
| Produce Product Dataset | product_catalog | P1 | Official product pages, catalogs | Coverage |
| Produce Service Dataset | product/service rows | P1 | Company sites, case studies | Coverage |
| Produce Pain Point Dataset | pain_point_library | P0 | Industry reports, WB sector notes | Coverage |
| Produce Solution Dataset | solution_library | P1 | Case studies, vendor-neutral reports | Coverage |
| Produce Framework Dataset | framework_library | P2 | Public frameworks, standards | Coverage |
| Produce Case Study Dataset | case_study_library | P1 | Sustainability/annual reports | Coverage |
| Produce KPI Dataset | KPI library / fields | P2 | Industry standards | Coverage |

### Regulation & labor

| Mission | Target dataset | Priority | Sources | KPI |
|---------|----------------|----------|---------|-----|
| Produce Regulation Dataset | regulation / framework | P1 | OJK, Kemenperin, Kemnaker, LKPP | Coverage, Freshness |
| Produce Banking Dataset | industry + company + regulation (banking focus) | P1 | OJK, BI public, WB finance | Coverage |
| Produce Outsourcing Dataset | industry/company/pain (BPO focus) | P2 | Associations, public market notes | Coverage |

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
