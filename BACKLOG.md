# Product Backlog — IDA Dataset Factory v2.0

**Status:** Official  
**Architecture:** Frozen (v2.0)  
**Horizon:** 2026–2027  

## Product goal

Automatically produce high-quality datasets for future LLM fine-tuning and knowledge corpus.

Every backlog item must improve at least one KPI:

| KPI family | Examples |
|------------|----------|
| **Coverage** | More rows, more datasets, more fields filled |
| **Quality** | Confidence, completeness, duplicates, validation |
| **Freshness** | Newer retrieved dates, source recrawl |
| **Automation** | Missions, scheduling, retries, CI jobs |
| **Export** | Formats, packaging, versioning |

## Product rules (non-negotiable)

- No architectural redesign  
- No repository restructure  
- No AI reasoning / decision engine  
- No RAG  
- No chatbot / agent product work  

Those belong to **IDA Intelligent Decision Automation**.

## Definition of Done (sprint)

A sprint is **DONE** only if it improves ≥1 official KPI (see [KPI.md](./KPI.md)).

---

## Epic index

| Epic | Title | Priority theme |
|------|-------|----------------|
| E1 | Trusted Source Expansion | Coverage + Freshness |
| E2 | Dataset Expansion | Coverage |
| E3 | Extraction Quality | Quality |
| E4 | Dataset Quality | Quality + Monitoring |
| E5 | Dataset Export | Export |
| E6 | Factory Monitoring | Automation + Visibility |
| E7 | Mission System | Automation |
| E8 | Quality Assurance | Quality + Automation |
| E9 | Documentation | Enablement |

---

# EPIC 1 — Trusted Source Expansion

### Objective

Increase the number of **trusted, healthy, allow-listed** sources that the factory can collect from—without random crawling.

### Business value

More legitimate provenance → higher training-data trust → fewer placeholder/low-trust rows.

### User story

> As a factory operator, I want more production-ready trusted sources so that learn missions can acquire verified public knowledge continuously.

### Acceptance criteria

- [ ] Each source registered in `metadata/source_registry.csv` with trust score, category, status, allowed  
- [ ] Source mirrored in `automation/config/sources.yaml` when active  
- [ ] Health status available (reachable / last success / error)  
- [ ] No `example.com` / `example.invalid` as active allowed sources  
- [ ] At least one successful collection path proven per new connector  

### Priority

**P0** (foundation for coverage growth)

### Dependencies

Source policy ([SOURCE_POLICY.md](./SOURCE_POLICY.md)); collector package

### Estimated complexity

**M–L** (per connector batch)

### Backlog items

| ID | Item | Priority | Complexity | KPI |
|----|------|----------|------------|-----|
| E1-01 | BPS collector: official statistics documents | P0 | M | Coverage, Freshness |
| E1-02 | World Bank collector: Indonesia country + IEP reports | P0 | M | Coverage |
| E1-03 | OECD collector: Indonesia surveys / digital chapter | P1 | M | Coverage |
| E1-04 | OJK collector: regulatory publications (banking/finance) | P0 | M | Coverage |
| E1-05 | Kemenperin collector: industry policy/public data | P1 | M | Coverage |
| E1-06 | Kemnaker collector: labor/employment publications | P2 | S | Coverage |
| E1-07 | BKPM / Investment ministry collector | P1 | M | Coverage |
| E1-08 | LKPP collector: public procurement references | P2 | M | Coverage |
| E1-09 | IFC collector: sector briefs (TMT, private sector) | P2 | S | Coverage |
| E1-10 | ADB collector: Indonesia country knowledge | P2 | S | Coverage |
| E1-11 | APINDO association collector | P2 | S | Coverage |
| E1-12 | KADIN association collector | P2 | S | Coverage |
| E1-13 | Source health monitor (status, last_ok, latency) | P0 | M | Automation, Freshness |
| E1-14 | robots.txt / rate-limit compliance checks | P0 | S | Quality |
| E1-15 | Source diversity score on Quality dashboard | P1 | S | Quality |

### Epic success

Every active source has **health status**; factory never depends on a single source for a dataset class.

---

# EPIC 2 — Dataset Expansion

### Objective

Increase **dataset coverage** across Business Development (then other domains) with verified, schema-complete rows.

### Business value

Richer corpus for fine-tuning; measurable coverage growth on the dashboard.

### User story

> As a factory operator, I want missions that fill empty or thin libraries so that each sprint raises row counts and field completeness.

### Acceptance criteria

- [ ] Append-only writes to existing schemas (no header changes without versioned migration)  
- [ ] Every new row has provenance (source, retrieved, confidence, version)  
- [ ] Coverage KPI moves (library rows and/or field completeness)  
- [ ] No fabricated placeholder URLs  

### Priority

**P0**

### Dependencies

E1 sources; E3 extraction; E8 QA gates

### Estimated complexity

**L** (ongoing)

### Priority dataset order

1. Industry  
2. Company  
3. Product  
4. Service  
5. Pain Point  
6. Solution  
7. Framework  
8. Case Study  
9. Buyer Persona  
10. Regulation  
11. Decision Maker  
12. KPI  
13. Opportunity  
14. Risk  
15. Trend  
16. Competitor  

### Backlog items

| ID | Item | Priority | Complexity | KPI |
|----|------|----------|------------|-----|
| E2-01 | Expand Industry Library (lowest field coverage first) | P0 | M | Coverage |
| E2-02 | Company Profile growth from trusted reports | P0 | L | Coverage |
| E2-03 | Product Catalog verified rows | P1 | M | Coverage |
| E2-04 | Service inventory dataset (or product subtype rules) | P1 | M | Coverage |
| E2-05 | Pain Point Library fill from industry docs | P0 | M | Coverage |
| E2-06 | Solution Library linked to pain points | P1 | M | Coverage |
| E2-07 | Framework Library entries with sources | P2 | S | Coverage |
| E2-08 | Case Study Library from public annual/sustainability reports | P1 | M | Coverage |
| E2-09 | Buyer Persona structured rows | P2 | M | Coverage |
| E2-10 | Regulation knowledge rows (OJK / industrial / labor) | P1 | L | Coverage |
| E2-11 | Decision Maker role patterns per industry | P2 | M | Coverage |
| E2-12 | KPI library per industry | P2 | M | Coverage |
| E2-13 | Opportunity patterns (not CRM pipeline) | P2 | M | Coverage |
| E2-14 | Risk library with source citations | P2 | M | Coverage |
| E2-15 | Trend library (dated, sourced) | P2 | M | Coverage |
| E2-16 | Competitor Library verified rows | P1 | M | Coverage |
| E2-17 | Domain stubs → first real rows (finance/legal/ops) | P2 | L | Coverage |
| E2-18 | Coverage target ladder (e.g. 25 → 50 industries) | P1 | S | Coverage |

### Epic success

Industry library and at least two adjacent libraries show **measurable row growth** per release train.

---

# EPIC 3 — Extraction Quality

### Objective

Improve extraction so published rows are more complete, consistent, and correctly matched to schema.

### Business value

Higher confidence training data; less human rework in quality queue.

### User story

> As a factory operator, I want extraction to normalize and score fields reliably so that published datasets meet quality policy without manual cleanup.

### Acceptance criteria

- [ ] Normalization rules documented and applied  
- [ ] Field-level validation before publish  
- [ ] Duplicate detection on entity id / canonical name  
- [ ] Entity matching across related libraries where applicable  
- [ ] Confidence calibration evidence (score distribution)  
- [ ] Schema completeness % increases or holds under growth  

### Priority

**P0**

### Dependencies

Existing `extractor` / `validator` packages; schemas

### Estimated complexity

**M–L**

### Backlog items

| ID | Item | Priority | Complexity | KPI |
|----|------|----------|------------|-----|
| E3-01 | Field normalization rules (dates, currency, enums) | P0 | M | Quality |
| E3-02 | Required-field validation per schema | P0 | M | Quality |
| E3-03 | Duplicate detection (exact + fuzzy name) | P0 | M | Quality |
| E3-04 | Entity matching industry↔company | P1 | L | Quality |
| E3-05 | Confidence calibration against source trust | P1 | M | Quality |
| E3-06 | Reject placeholder / blocked domain URLs | P0 | S | Quality |
| E3-07 | Multi-source merge with provenance trail | P1 | L | Quality |
| E3-08 | Extraction version stamps on all rows | P0 | S | Quality, Export |
| E3-09 | Schema completeness report per dataset | P1 | S | Quality |
| E3-10 | Extraction golden fixtures (regression set) | P1 | M | Automation |

---

# EPIC 4 — Dataset Quality

### Objective

Make quality **visible and actionable** on the factory Quality surface and KPIs.

### Business value

Operators can see quality degradation early and prioritize missions.

### User story

> As a factory operator, I want a quality dashboard with standard metrics so that I can decide which mission to run next.

### Acceptance criteria

- [ ] Metrics live: Duplicate Rate, Freshness, Completeness, Confidence, Source Diversity, Coverage  
- [ ] Quality page shows trends (today / week where possible)  
- [ ] Metrics computed from real datasets + journal—not placeholders  
- [ ] Quality score formula documented in [KPI.md](./KPI.md)  

### Priority

**P0**

### Dependencies

E3 validators; existing Quality page

### Estimated complexity

**M**

### Backlog items

| ID | Item | Priority | Complexity | KPI |
|----|------|----------|------------|-----|
| E4-01 | Duplicate rate KPI (per dataset + global) | P0 | M | Quality |
| E4-02 | Freshness KPI (≤30/90 day windows) | P0 | S | Freshness |
| E4-03 | Completeness KPI (schema field fill) | P0 | S | Quality |
| E4-04 | Average confidence KPI | P0 | S | Quality |
| E4-05 | Source diversity KPI (# distinct sources used) | P1 | S | Quality |
| E4-06 | Coverage KPI (catalog + field) | P0 | S | Coverage |
| E4-07 | Quality trend sparkline / week comparison | P2 | M | Monitoring |
| E4-08 | Dataset-level quality cards | P1 | M | Quality |
| E4-09 | Quality alert thresholds in CI | P1 | M | Automation |

---

# EPIC 5 — Dataset Export

### Objective

Produce reliable training packages in all required formats, with versions.

### Business value

Downstream LLM training can consume factory outputs without manual conversion.

### User story

> As a training pipeline consumer, I want versioned exports (CSV/JSON/JSONL/Parquet/OpenAI/HF/ShareGPT/Alpaca) so that I can fine-tune models on factory data.

### Acceptance criteria

- [ ] Export job produces artifacts under `exports/`  
- [ ] Dashboard Export status reflects real files  
- [ ] Version tag on each package  
- [ ] Formats: CSV (domains), JSON, JSONL, Parquet, OpenAI FT, Hugging Face, ShareGPT, Alpaca  
- [ ] CI workflow `export.yml` remains green  

### Priority

**P0–P1**

### Dependencies

Stable published datasets; quality gates optional but preferred

### Estimated complexity

**M–L**

### Backlog items

| ID | Item | Priority | Complexity | KPI |
|----|------|----------|------------|-----|
| E5-01 | Harden JSONL export (all domain CSVs) | P0 | S | Export |
| E5-02 | Parquet export with typed columns | P0 | M | Export |
| E5-03 | OpenAI fine-tuning format (messages) | P0 | S | Export |
| E5-04 | Hugging Face dataset package layout | P0 | M | Export |
| E5-05 | ShareGPT conversation export | P1 | M | Export |
| E5-06 | Alpaca instruction export | P1 | M | Export |
| E5-07 | Versioned package manifests (`version`, `hash`, `row_count`) | P0 | M | Export |
| E5-08 | Multi-dataset export matrix | P1 | M | Export |
| E5-09 | Export status API + dashboard badge | P1 | S | Export, Monitoring |
| E5-10 | Optional HF Hub publish (tokenized, opt-in) | P2 | L | Export |

---

# EPIC 6 — Factory Monitoring

### Objective

Improve the factory dashboard so operators see production health at a glance.

### Business value

Faster diagnosis; less reliance on raw logs.

### User story

> As a factory operator, I want factory health, mission status, coverage, quality, rows added, activity, history, and export status so that I can run the factory without reading code.

### Acceptance criteria

- [ ] Dashboard shows only factory metrics (no AI/engineering vanity metrics)  
- [ ] Factory Health, Mission Status, Dataset Progress, Coverage, Quality, Rows Added, Latest Activity, Mission History, Export Status  
- [ ] Polls real APIs / state files  
- [ ] No legacy branding (Executive / Brain / ECC)  

### Priority

**P1**

### Dependencies

KPI module; missions/sessions APIs

### Estimated complexity

**M**

### Backlog items

| ID | Item | Priority | Complexity | KPI |
|----|------|----------|------------|-----|
| E6-01 | Factory Health indicator (idle/running/error) | P0 | S | Automation |
| E6-02 | Mission status panel (active + last success) | P0 | S | Automation |
| E6-03 | Dataset progress (populated vs total) | P0 | S | Coverage |
| E6-04 | Rows added today/week/month panels | P0 | S | Coverage |
| E6-05 | Mission history list | P1 | M | Automation |
| E6-06 | Export status widget | P1 | S | Export |
| E6-07 | Latest activity stream polish | P1 | S | Monitoring |
| E6-08 | Coverage progress target vs actual | P1 | S | Coverage |
| E6-09 | Zero legacy labels audit | P0 | S | — |

---

# EPIC 7 — Mission System

### Objective

Make missions the primary way to drive production (what to produce, when, with priority and retry).

### Business value

Predictable dataset growth via scheduled, prioritizable factory jobs.

### User story

> As a factory operator, I want production missions (Industry, Company, Regulation, Banking, Outsourcing, …) with schedule, priority, and retry so that coverage grows without manual ad-hoc runs.

### Acceptance criteria

- [ ] Mission templates for each production dataset class  
- [ ] Scheduler prioritizes lowest coverage / highest priority  
- [ ] Retry on recoverable failure  
- [ ] Mission success rate KPI updates  
- [ ] Dashboard shows current + history  

### Priority

**P0–P1**

### Dependencies

Scheduler; learn workflow; source health (E1)

### Estimated complexity

**L**

### Backlog items

| ID | Item | Priority | Complexity | KPI |
|----|------|----------|------------|-----|
| E7-01 | Mission: Produce Industry Dataset | P0 | M | Coverage, Automation |
| E7-02 | Mission: Produce Company Dataset | P0 | M | Coverage |
| E7-03 | Mission: Produce Regulation Dataset | P1 | M | Coverage |
| E7-04 | Mission: Produce Banking Dataset | P1 | M | Coverage |
| E7-05 | Mission: Produce Outsourcing / BPO Dataset | P2 | M | Coverage |
| E7-06 | Mission: Produce Pain Point Dataset | P1 | M | Coverage |
| E7-07 | Mission: Produce Competitor Dataset | P1 | M | Coverage |
| E7-08 | Mission scheduling (cron + GHA alignment) | P0 | M | Automation |
| E7-09 | Mission retry with backoff | P1 | M | Automation |
| E7-10 | Mission priority (P0–P4) enforcement | P0 | S | Automation |
| E7-11 | Lowest-coverage industry prioritization | P0 | M | Coverage |
| E7-12 | Mission library catalog UI (read-only) | P2 | S | Monitoring |
| E7-13 | Mission success rate KPI | P1 | S | Automation |

See also [MISSION_LIBRARY.md](./MISSION_LIBRARY.md).

---

# EPIC 8 — Quality Assurance

### Objective

Automate QA so bad data cannot silently ship.

### Business value

Protects corpus integrity; CI becomes the quality gate.

### User story

> As a factory operator, I want automated schema/source/confidence/duplicate/coverage validation so that publish/export fails when quality drops.

### Acceptance criteria

- [ ] CI job validates schema, sources, confidence, duplicates, coverage thresholds  
- [ ] Failures are actionable in logs  
- [ ] Quality workflow (`quality.yml`) runs on schedule + dispatch  
- [ ] No publish of rows failing hard gates  

### Priority

**P0**

### Dependencies

E3, E4

### Estimated complexity

**M**

### Backlog items

| ID | Item | Priority | Complexity | KPI |
|----|------|----------|------------|-----|
| E8-01 | Schema validation CI | P0 | M | Quality, Automation |
| E8-02 | Source allow-list validation | P0 | S | Quality |
| E8-03 | Confidence minimum gate | P0 | S | Quality |
| E8-04 | Duplicate validation gate | P0 | M | Quality |
| E8-05 | Coverage regression gate (no silent drop) | P1 | M | Coverage |
| E8-06 | Placeholder URL ban in CI | P0 | S | Quality |
| E8-07 | Quality report artifact (JSON/MD) | P1 | S | Quality |
| E8-08 | Pre-export QA gate | P1 | M | Export, Quality |

---

# EPIC 9 — Documentation

### Objective

Keep product docs synchronized with factory behavior—never reintroduce architecture churn docs as product work.

### Business value

Contributors and operators stay aligned on factory-only goals.

### User story

> As a contributor, I want current Architecture, Schema, Roadmap, Source Policy, and Contribution guides so that I only ship factory-improving work.

### Acceptance criteria

- [ ] Living docs match v2.0 surfaces  
- [ ] Backlog/roadmap/milestones/KPI/mission library current  
- [ ] No new decision-engine / RAG docs in this repo  

### Priority

**P1**

### Dependencies

None

### Estimated complexity

**S–M**

### Backlog items

| ID | Item | Priority | Complexity | KPI |
|----|------|----------|------------|-----|
| E9-01 | Sync ARCHITECTURE with factory packages | P1 | S | — |
| E9-02 | Sync DATASET_SCHEMA with metadata/schema | P1 | S | — |
| E9-03 | Quarterly roadmap refresh | P1 | S | — |
| E9-04 | Source policy updates per new connector | P1 | S | — |
| E9-05 | CONTRIBUTING checklist for KPI impact | P1 | S | — |
| E9-06 | Mission library updates per new mission | P1 | S | — |
| E9-07 | Archive only—never resurrect ECC docs as product | P0 | S | — |

---

## Cross-epic sequencing (summary)

```text
E1 Sources ──┐
             ├──▶ E2 Dataset Expansion ──▶ E5 Export
E3 Extract ──┤              ▲
E8 QA ───────┴──────────────┘
E4 Quality visibility + E6 Monitoring (parallel)
E7 Missions (drives E2 continuously)
E9 Docs (continuous)
```

---

## Out of backlog (rejected themes)

| Theme | Why rejected |
|-------|----------------|
| RAG / retrieval product | Other product |
| Decision / reasoning engine | Other product |
| Chatbot / agent framework | Other product |
| Knowledge graph UI | Other product |
| Architecture redesign sprints | Frozen architecture |

---

*Backlog ownership: IDA Dataset Factory product only.*
