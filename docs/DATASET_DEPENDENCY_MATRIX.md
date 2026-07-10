# Dataset Dependency Matrix

**Status:** Official · Permanent production sequence authority  
**Version:** 1.0  
**Effective:** 2026-07-10  
**Architecture:** Frozen (IDA Dataset Factory v2.0)  

---

## 1. Purpose

This matrix defines **which datasets must exist before another dataset can be produced with quality**.

It is the permanent **production order** for every future production batch.

| Rule | Statement |
|------|-----------|
| Authority | Dependency matrix + [PRODUCTION_ORDER.md](./PRODUCTION_ORDER.md) govern sequencing |
| Execution | Every batch follows [DATASET_PRODUCTION_STANDARD.md](./DATASET_PRODUCTION_STANDARD.md) (DPS v1.0) |
| Targets | Row targets from `automation/config/product_targets.yaml` — **never hardcoded** |
| Non-goals | No architecture, UI, schema, or automation redesign |

---

## 2. Official production graph

Hard dependencies are **required** before quality production. Soft dependencies **improve** quality but do not fully block a minimal batch.

```text
                         ┌──────────────────┐
                         │    INDUSTRY      │  ROOT
                         │  industry_library│
                         └────────┬─────────┘
           ┌──────────────┬───────┼───────────┬────────────────┬─────────────┐
           ▼              ▼       ▼           ▼                ▼             ▼
      REGULATION       TREND    RISK     SERVICE          PRODUCT      (continuous
      (library or     (fields/  (fields/  service_library   product_    industry
       industry       industry  industry  → product_catalog  catalog)    growth)
       fields)        fields)   fields)   subtype until
                                          dedicated CSV)
           │              │       │           │                │
           └──────────────┴───────┴─────┬─────┴────────────────┘
                                        ▼
                                 ┌──────────────┐
                                 │   COMPANY    │
                                 │company_profile│
                                 └──────┬───────┘
                    ┌───────────────────┼───────────────────┐
                    ▼                   ▼                   ▼
              COMPETITOR          PAIN POINT           BUYER PERSONA
           competitor_library   pain_point_library   (persona library /
                                                       discovery fields)
                    │                   │                   │
                    │                   ▼                   ▼
                    │            ┌────────────┐      DECISION MAKER
                    │            │  SOLUTION  │      (role patterns)
                    │            │solution_lib│
                    │            └─────┬──────┘
                    │                  │
                    │         ┌────────┼────────┐
                    │         ▼        ▼        ▼
                    │    FRAMEWORK  CASE STUDY  OPPORTUNITY
                    │  framework_lib case_study  opportunity_analysis
                    │                   │              │
                    └───────────────────┴──────────────┤
                                                       ▼
                                              BUSINESS SIGNAL
                                           business_signal_library
                                                       │
                                                       ▼
                                            DISCOVERY QUESTIONS
                                          discovery_question_library
```

### Linear manufacturing order (default)

Use this sequence unless a batch explicitly documents a justified exception under DPS:

```text
Industry
  ↓
Service
  ↓
Product
  ↓
Company
  ↓
Regulation · Trend · Risk   (can run in parallel after Industry; preferred after Company for Risk)
  ↓
Pain Point
  ↓
Solution
  ↓
Framework
  ↓
Case Study
  ↓
Buyer Persona
  ↓
Decision Maker
  ↓
Competitor
  ↓
Opportunity
  ↓
Business Signal
  ↓
Discovery Question
```

**Why not Industry → Company first?**  
Schemas allow companies after Industry alone, and seed `company_profile` rows already exist. For **quality production**, Service and Product catalogs should land early so company rows can reference real offerings without inventing product IDs later. Industry remains the only hard root.

---

## 3. Dependency table

| Dataset class | Domain file / store | Hard depends on | Soft depends on | Why |
|---------------|---------------------|-----------------|-----------------|-----|
| **Industry** | `industry_library.csv` | — | — | Taxonomy root. All Industry ID foreign keys hang from here. |
| **Service** | `service_library` target → rows in `product_catalog` (`Product Type` = Service) until dedicated CSV | Industry | — | Services are verticalized by industry; no company required for catalog-level inventory. |
| **Product** | `product_catalog.csv` | Industry | Service (for cross-sell consistency) | `Target Industry` and industry-scoped ICP; products are sellable objects independent of a single company. |
| **Company** | `company_profile.csv` | Industry | Service, Product | Schema requires `Industry ID` / Industry. Soft: known products/services improve challenges, tech, and cross-sell fields without fabrication. |
| **Regulation** | `regulation_library` (target; may encode in industry fields until dedicated store) | Industry | Company | Regulations apply to industries (and sometimes firm types). Industry is hard; company enriches applicability. |
| **Trend** | Trend library or industry `Industry Trends` fields | Industry | — | Trends are industry-dated facts; company not required. |
| **Risk** | Risk library or industry `Major Risks` fields | Industry | Company | Industry risks first; company-level risk needs Company. |
| **Pain Point** | `pain_point_library.csv` | Industry | Company | Schema: `Industry ID`. Company patterns improve symptoms, severity, and ICP fidelity. |
| **Solution** | `solution_library.csv` | Pain Point | Product, Service | Schema: `Related Pain ID`, `Recommended Product IDs`. Solutions without pains are marketing fiction. |
| **Framework** | `framework_library.csv` | — (minimal) | Solution, Pain Point | Can store public frameworks early, but **production value** peaks when linked to solutions/pains. Soft dependency preferred. |
| **Case Study** | `case_study_library.csv` | Company | Solution, Product | Schema: `Company ID`, Challenge / Solution Applied / Products Used. |
| **Buyer Persona** | `buyer_persona_library` target (or discovery/persona fields) | Industry | Company | Personas are industry- and segment-specific; company archetypes raise quality. |
| **Decision Maker** | `decision_maker_library` target | Buyer Persona | Company, Industry | Decision-maker roles refine personas; not a substitute for company rows. |
| **Competitor** | `competitor_library.csv` | Industry | Company, Product, Service | Competitive set is industry-scoped; product/service catalogs make USP and pricing fields real. |
| **Opportunity** | `opportunity_analysis.csv` | Company | Pain Point, Solution, Industry | Schema: `Company ID`; quality needs challenge/pain/solution linkage. |
| **Business Signal** | `business_signal_library.csv` | Industry | Opportunity | Signals point at industries and opportunity types. |
| **Discovery Question** | `discovery_question_library.csv` | Industry | Framework, Pain Point, Solution, Persona | Schema links Framework, Industry, Pain, Solution, Target Persona. |

### Non-production datasets

| Asset | Role |
|-------|------|
| `guidance.csv` | Meta documentation of sheets/columns — **not** a knowledge product dataset |
| Other domain stubs (`finance/`, `legal/`, …) | Future domain expansion after Business Development product targets mature |

---

## 4. Dependency rationale (detail)

### 4.1 Industry is the root

Every primary BD schema that carries `Industry ID` or `Industry` assumes a stable industry taxonomy. Producing companies, pains, regulations, or competitors without industries forces invented IDs and breaks append-only identity.

### 4.2 Service before Product before Company (adjusted order)

| Decision | Rationale |
|----------|-----------|
| Service & Product after Industry | Catalog entities can be verified from official product/service pages and stats without waiting for 10k companies. |
| Company after Service + Product | Company profiles reference products/services, tech stacks, and cross-sell — empty catalogs force empty or fabricated offer fields. |
| Parallelism | Service and Product batches may run **in parallel** after Industry; both must complete a minimum quality gate before large Company scale-up. |

This adjusts the naive Industry→Company→Product chain to match **schema quality**, not only foreign-key minimalism.

### 4.3 Pain → Solution → Framework

Solutions without pains fail DPS quality (orphan `Related Pain ID`). Frameworks can exist as public standards early, but production batches should **attach** frameworks to solutions after the pain/solution spine exists.

### 4.4 Case Study late

Case studies require real `Company ID` and preferably solution/product linkage. Running them before Company/Solution produces empty or synthetic case rows — forbidden under DPS.

### 4.5 Opportunity after commercial spine

Opportunity analysis is a **derived commercial pattern**, not a CRM. It needs Company plus pain/solution context. Seed opportunity rows may exist; scale production waits for the spine.

### 4.6 Competitor after offer + company context

Competitor rows without product/service contrast become marketing blurbs. Industry is hard; Company + Product + Service are soft-but-strong.

### 4.7 Regulation / Trend / Risk

| Class | Placement |
|-------|-----------|
| Regulation | After Industry (hard); may interleave anytime post-Industry |
| Trend | After Industry; continuous with industry expansion |
| Risk | After Industry; company-risk after Company |

These may be **field expansions** on industry/company until dedicated libraries exist. Dependency rules still apply.

---

## 5. Parallelism rules

Allowed parallel production (same phase, different missions):

| Parallel set | Condition |
|--------------|-----------|
| Service ‖ Product | Industry root present |
| Regulation ‖ Trend ‖ Risk (industry-level) | Industry root present |
| Competitor ‖ Buyer Persona | Company baseline present |
| Framework (public standards) ‖ late Pain growth | Do not invent pain links |

Forbidden shortcuts:

- Solution without Pain Point  
- Case Study without Company  
- Opportunity scale-up without Company  
- Any batch using forbidden sources or confidence &lt; 0.80  

---

## 6. Minimum prerequisite coverage (quality gates)

Before starting a **dependent** batch at scale, the upstream dataset should meet a **minimum production baseline** (not the full product target):

| Upstream | Minimum baseline to unlock dependents | Product target (config) |
|----------|----------------------------------------|-------------------------|
| Industry | ≥ 50 verified rows (phase complete) | 250 |
| Service | ≥ 20 verified service rows | 2_000 |
| Product | ≥ 20 verified product rows | 5_000 |
| Company | ≥ 25 verified rows | 10_000 |
| Pain Point | ≥ 25 verified rows | 3_000 |
| Solution | ≥ 25 verified rows | 3_000 |

Baselines are **gates for sequencing**, not product success. Product success remains `current / product_target` ([KPI.md](../KPI.md)).

---

## 7. Mapping to storage today

| Logical class | Product target key | Current store |
|---------------|--------------------|---------------|
| Industry | `industry_library` | `domains/business_development/industry_library.csv` |
| Company | `company_profile` | `domains/business_development/company_profile.csv` |
| Product | `product_catalog` | `domains/business_development/product_catalog.csv` |
| Service | `service_library` | Produce as `product_catalog` rows with service type until dedicated CSV exists |
| Pain Point | `pain_point_library` | `domains/business_development/pain_point_library.csv` |
| Solution | `solution_library` | `domains/business_development/solution_library.csv` |
| Framework | `framework_library` | `domains/business_development/framework_library.csv` |
| Case Study | `case_study_library` | `domains/business_development/case_study_library.csv` |
| Competitor | `competitor_library` | `domains/business_development/competitor_library.csv` |
| Opportunity | `opportunity_analysis` | `domains/business_development/opportunity_analysis.csv` |
| Business Signal | `business_signal_library` | `domains/business_development/business_signal_library.csv` |
| Discovery Question | `discovery_question_library` | `domains/business_development/discovery_question_library.csv` |
| Buyer Persona | `buyer_persona_library` | Dedicated store when created; until then persona fields / discovery |
| Decision Maker | `decision_maker_library` | Dedicated store when created; until then industry/company role fields |
| Regulation | `regulation_library` | Dedicated store when created; until then industry regulation fields |
| Risk / Trend | `_default` or future keys | Industry (and company) fields until libraries exist |

Schema freeze: do **not** invent new columns without versioned migration ([DATASET_SCHEMA.md](../DATASET_SCHEMA.md)).

---

## 8. Related documents

| Document | Role |
|----------|------|
| [PRODUCTION_ORDER.md](./PRODUCTION_ORDER.md) | Manufacturing plan, targets, ETAs, dashboard fields |
| [PRODUCTION_BATCH_LIBRARY.md](./PRODUCTION_BATCH_LIBRARY.md) | Batch catalog Batch-001… |
| [DATASET_PRODUCTION_STANDARD.md](./DATASET_PRODUCTION_STANDARD.md) | DPS operating procedure |
| [KPI.md](../KPI.md) | Product vs sprint KPIs |
| [MISSION_LIBRARY.md](../MISSION_LIBRARY.md) | Mission definitions |

---

**End of Dataset Dependency Matrix v1.0**
