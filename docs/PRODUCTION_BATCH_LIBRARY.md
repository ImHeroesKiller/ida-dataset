# Production Batch Library

**Status:** Official catalog  
**Version:** 1.0  
**Mode:** Permanent production (not software sprints)  
**Standard:** [DATASET_PRODUCTION_STANDARD.md](./DATASET_PRODUCTION_STANDARD.md) (DPS v1.0)  
**Sequence authority:** [DATASET_DEPENDENCY_MATRIX.md](./DATASET_DEPENDENCY_MATRIX.md)  

---

## 1. What is a Production Batch?

A **Production Batch** is a bounded knowledge-manufacturing job that:

1. Targets one primary dataset class  
2. Follows DPS lifecycle end-to-end  
3. Increases product coverage (`current_rows / product_target`)  
4. Produces a production report  
5. Updates exports when in scope  

Batches produce **knowledge rows**, not software features.

### Batch rules (no exceptions)

| Rule | Requirement |
|------|-------------|
| DPS | Follow DPS v1.0 fully |
| Sources | Trusted / allow-listed only |
| Write policy | Append-only |
| Validation | Pass before publish; confidence ≥ 0.80 |
| KPIs | Update factory KPIs |
| Exports | Update when release/export stage is in scope |
| Report | Mission/batch production report required |

---

## 2. Status vocabulary

| Status | Meaning |
|--------|---------|
| **Completed** | Baseline production gate met for this batch theme; continuous growth may continue as sub-batches |
| **Active** | Currently manufacturing |
| **Planned** | Next in queue or scheduled |
| **Blocked** | Waiting on hard dependency |
| **Continuous** | Ongoing expansion toward product target after baseline |

---

## 3. Batch catalog

Coverage and row counts below are **snapshots at planning time** (2026-07-10).  
Live numbers always come from domain CSVs + `automation/config/product_targets.yaml` via factory KPIs — **never treat this table as hardcoded runtime truth**.

Product targets (config keys):

| Class | Config key | Product target |
|-------|------------|----------------|
| Industry | `industry_library` | 250 |
| Service | `service_library` | 2_000 |
| Product | `product_catalog` | 5_000 |
| Company | `company_profile` | 10_000 |
| Pain Point | `pain_point_library` | 3_000 |
| Solution | `solution_library` | 3_000 |
| Framework | `framework_library` | 500 |
| Case Study | `case_study_library` | 1_000 |
| Buyer Persona | `buyer_persona_library` | 500 |
| Decision Maker | `decision_maker_library` | 500 |
| Regulation | `regulation_library` | 1_000 |
| Opportunity | `opportunity_analysis` | 2_000 |
| Competitor | `competitor_library` | 1_000 |
| Business Signal | `business_signal_library` | 1_000 |
| Discovery Question | `discovery_question_library` | 500 |
| Risk / Trend | future / fields | see matrix |

---

### Batch-001 — Industry Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-001 |
| **Dataset** | Industry (`industry_library`) |
| **Status** | Completed (baseline) · Continuous growth remains |
| **Dependency** | None (root) |
| **Current rows** | 50 |
| **Product target** | 250 |
| **Coverage** | 50 / 250 = **20%** |
| **Priority** | P0 |
| **Mission theme** | Produce / Expand Industry Dataset |
| **Notes** | Phase-1 verified industry set delivered. Continue toward product target 250 under continuous sub-batches (Batch-001b, 001c, …). |

---

### Batch-002 — Service Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-002 |
| **Dataset** | Service (`service_library` → `product_catalog` service-type rows until dedicated CSV) |
| **Status** | Planned · **Next primary batch** |
| **Dependency** | Industry (hard) |
| **Current rows** | 0 dedicated service inventory (seed products may exist; service classification required) |
| **Product target** | 2_000 |
| **Coverage** | 0 / 2_000 = **0%** |
| **Priority** | P0 |
| **Mission theme** | Produce Service Dataset |
| **Unlocks** | Richer Company, Competitor, Solution product links |

---

### Batch-003 — Product Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-003 |
| **Dataset** | Product (`product_catalog`) |
| **Status** | Planned (may run ‖ Batch-002 after Industry) |
| **Dependency** | Industry (hard); Service (soft, preferred parallel) |
| **Current rows** | 20 (seed) |
| **Product target** | 5_000 |
| **Coverage** | 20 / 5_000 = **0.4%** |
| **Priority** | P0 |
| **Mission theme** | Produce Product Dataset |
| **Notes** | Seed rows exist; production batch must verify provenance and expand under DPS. |

---

### Batch-004 — Company Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-004 |
| **Dataset** | Company (`company_profile`) |
| **Status** | Planned |
| **Dependency** | Industry + Service + Product (hard Industry; soft Service/Product for quality scale-up) |
| **Current rows** | 25 (seed) |
| **Product target** | 10_000 |
| **Coverage** | 25 / 10_000 = **0.3%** |
| **Priority** | P0 |
| **Mission theme** | Produce Company Dataset |
| **Notes** | Do not mass-scale until Service/Product baselines exist (see dependency matrix gates). |

---

### Batch-005 — Pain Point Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-005 |
| **Dataset** | Pain Point (`pain_point_library`) |
| **Status** | Planned |
| **Dependency** | Industry + Company |
| **Current rows** | 0 |
| **Product target** | 3_000 |
| **Coverage** | 0% |
| **Priority** | P0 |
| **Mission theme** | Produce Pain Point Dataset |

---

### Batch-006 — Solution Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-006 |
| **Dataset** | Solution (`solution_library`) |
| **Status** | Planned |
| **Dependency** | Pain Point (hard); Product / Service (soft) |
| **Current rows** | 0 |
| **Product target** | 3_000 |
| **Coverage** | 0% |
| **Priority** | P0 |
| **Mission theme** | Produce Solution Dataset |

---

### Batch-007 — Framework Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-007 |
| **Dataset** | Framework (`framework_library`) |
| **Status** | Planned |
| **Dependency** | Solution (preferred soft-hard for linked production); public frameworks may start earlier without false pain links |
| **Current rows** | 0 |
| **Product target** | 500 |
| **Coverage** | 0% |
| **Priority** | P1 |
| **Mission theme** | Produce Framework Dataset |

---

### Batch-008 — Case Study Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-008 |
| **Dataset** | Case Study (`case_study_library`) |
| **Status** | Planned |
| **Dependency** | Company + Solution |
| **Current rows** | 0 |
| **Product target** | 1_000 |
| **Coverage** | 0% |
| **Priority** | P1 |
| **Mission theme** | Produce Case Study Dataset |

---

### Batch-009 — Buyer Persona Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-009 |
| **Dataset** | Buyer Persona (`buyer_persona_library`) |
| **Status** | Planned |
| **Dependency** | Industry + Company |
| **Current rows** | 0 |
| **Product target** | 500 |
| **Coverage** | 0% |
| **Priority** | P1 |
| **Mission theme** | Produce Buyer Persona Dataset |

---

### Batch-010 — Decision Maker Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-010 |
| **Dataset** | Decision Maker (`decision_maker_library`) |
| **Status** | Planned |
| **Dependency** | Buyer Persona |
| **Current rows** | 0 |
| **Product target** | 500 |
| **Coverage** | 0% |
| **Priority** | P1 |
| **Mission theme** | Produce Decision Maker Dataset |

---

### Batch-011 — Regulation Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-011 |
| **Dataset** | Regulation (`regulation_library`) |
| **Status** | Planned (may interleave post-Industry) |
| **Dependency** | Industry |
| **Current rows** | 0 dedicated |
| **Product target** | 1_000 |
| **Coverage** | 0% |
| **Priority** | P1 |
| **Mission theme** | Produce Regulation Dataset |
| **Notes** | Until dedicated store exists, limited industry regulation field enrichment is allowed without inventing a parallel schema. |

---

### Batch-012 — Opportunity Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-012 |
| **Dataset** | Opportunity (`opportunity_analysis`) |
| **Status** | Planned |
| **Dependency** | Industry + Company + Pain Point + Solution |
| **Current rows** | 25 (seed) |
| **Product target** | 2_000 |
| **Coverage** | 25 / 2_000 = **1.3%** |
| **Priority** | P1 |
| **Mission theme** | Produce Opportunity Patterns |
| **Notes** | Seed exists; scale only after commercial spine (Company + Pain + Solution). |

---

### Batch-013 — Risk Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-013 |
| **Dataset** | Risk (library or industry/company risk fields) |
| **Status** | Planned |
| **Dependency** | Industry + Company (company-level); Industry alone for industry-level |
| **Current rows** | Encoded partially in industry fields |
| **Product target** | Config `_default` or future key (informational until dedicated library) |
| **Coverage** | Field-level until library exists |
| **Priority** | P2 |
| **Mission theme** | Produce Risk Dataset |

---

### Batch-014 — Trend Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-014 |
| **Dataset** | Trend (library or industry trend fields) |
| **Status** | Planned / continuous with Industry |
| **Dependency** | Industry |
| **Current rows** | Encoded partially in industry `Industry Trends` |
| **Product target** | Config `_default` or future key |
| **Coverage** | Field-level until library exists |
| **Priority** | P2 |
| **Mission theme** | Produce Trend Dataset |

---

### Batch-015 — Competitor Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-015 |
| **Dataset** | Competitor (`competitor_library`) |
| **Status** | Planned |
| **Dependency** | Company + Product + Service (Industry hard) |
| **Current rows** | 0 |
| **Product target** | 1_000 |
| **Coverage** | 0% |
| **Priority** | P1 |
| **Mission theme** | Produce Competitor Dataset |

---

### Batch-016 — Business Signal Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-016 |
| **Dataset** | Business Signal (`business_signal_library`) |
| **Status** | Planned |
| **Dependency** | Industry; Opportunity (soft) |
| **Current rows** | 0 |
| **Product target** | 1_000 |
| **Coverage** | 0% |
| **Priority** | P2 |
| **Mission theme** | Produce Business Signal Dataset |

---

### Batch-017 — Discovery Question Dataset

| Field | Value |
|-------|--------|
| **ID** | Batch-017 |
| **Dataset** | Discovery Question (`discovery_question_library`) |
| **Status** | Planned |
| **Dependency** | Industry + Framework + Pain Point + Solution (+ Persona preferred) |
| **Current rows** | 0 |
| **Product target** | 500 |
| **Coverage** | 0% |
| **Priority** | P2 |
| **Mission theme** | Produce Discovery Question Dataset |

---

## 4. Execution queue (immediate)

| Order | Batch | Action |
|-------|-------|--------|
| 1 | Batch-001 | Continuous industry growth toward 250 (background) |
| 2 | **Batch-002** | **Execute next** — Service Dataset |
| 3 | Batch-003 | Product Dataset (parallel with 002 when capacity allows) |
| 4 | Batch-004 | Company Dataset scale-up |
| 5 | Batch-005 → 006 → 007 | Pain → Solution → Framework |
| 6 | Batch-008 → 011, 015 | Case Study, Persona, Decision Maker, Regulation, Competitor |
| 7 | Batch-012 → 017 | Opportunity, Risk, Trend, Signals, Discovery |

---

## 5. Batch completion checklist

Copy into every production report:

```text
[ ] Batch ID + dataset class
[ ] Dependencies satisfied
[ ] Trusted sources only (registry IDs listed)
[ ] Rows added / rejected
[ ] Coverage before → after (product target denominator)
[ ] Average confidence ≥ policy
[ ] Duplicate rate within policy
[ ] Freshness recorded
[ ] Append-only integrity
[ ] Exports updated (if in scope)
[ ] DPS DoD met
```

---

## 6. Related documents

- [PRODUCTION_ORDER.md](./PRODUCTION_ORDER.md) — targets, ETA, readiness, dashboard field map  
- [DATASET_DEPENDENCY_MATRIX.md](./DATASET_DEPENDENCY_MATRIX.md) — why this order  
- [MISSION_LIBRARY.md](../MISSION_LIBRARY.md) — missions that execute batches  
- [KPI.md](../KPI.md) — product KPI rules  

---

**End of Production Batch Library v1.0**
