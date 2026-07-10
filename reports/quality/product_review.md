# Product Review — Final Gate

**Generated:** 2026-07-10T15:51:42.662478+00:00  
**Charter:** Continuously produce high-quality structured datasets for LLM fine-tuning  
**Mode:** Recommendations only — no deletes, no schema changes  

---

## Dataset value matrix

| Dataset | Rows | Target | Why it exists | Who depends on it | Replaceable? | Roadmap verdict | Recommendation |
|---------|-----:|-------:|---------------|-------------------|--------------|-----------------|----------------|
| industry_library | 50 | 250 | Taxonomy root for all BD knowledge | All industry-linked datasets | No | KEEP — critical | Continue expansion to 250 |
| company_profile | 86 | 10000 | Entity instances for commercial spine | Case study, opportunity, persona, competitor | No | KEEP — critical | Expand; fix seed Industry ID links via append hygiene |
| product_catalog | 123 | 5000 | Offer catalog (products + services) | Company soft-links, solutions | Service logical class coexists | KEEP — critical | Split service counting remains logical |
| service_library (logical) | 65 | 2000 | Service offerings via Product Type | Company soft-links | Mapped into product_catalog | KEEP as logical class | Do not invent schema; expand service-type rows |
| pain_point_library | 58 | 3000 | Demand-side problems by industry | Solutions | No | KEEP — critical | Expand with trusted sector docs |
| solution_library | 58 | 3000 | Response patterns linked to pains | Frameworks, cases | No | KEEP — critical | Populate Supporting Framework |
| framework_library | 40 | 500 | Method/process scaffolds | Discovery, solutions | Partially replaceable by docs | KEEP | Link from solutions; avoid copyrighted full standards |
| case_study_library | 40 | 1000 | Illustrative company×solution patterns | Training examples | Weak without outcomes | KEEP with caution | Only public evidence; no fabricated ROI |
| opportunity_analysis | 25 | 2000 | Commercial opportunity patterns | Downstream BD consumers | Not CRM | KEEP after FK hygiene | Repair broken Company IDs before scale |
| competitor_library | 0 | 1000 | Competitive landscape | Company/product strategy | No | KEEP empty until Batch-015 | Do not fill with low-trust blogs |
| business_signal_library | 0 | 1000 | Market signals | Opportunity timing | Trend fields partially | KEEP empty for now | Produce after industry/company depth |
| discovery_question_library | 0 | 500 | Discovery questions | Persona/solution paths | No | KEEP empty until spine richer | Depends on framework+pain+solution |
| guidance.csv | 249 | — | Meta sheet documentation (not knowledge product) | Operators only | Docs | RECONSIDER as product KPI input | Exclude from coverage KPIs; not a training entity set |
| buyer_persona_library | 0 | 500 | Buyer personas | Decision makers, GTM | No | KEEP — next Batch-009 | Highest priority empty class |
| decision_maker_library | 0 | 500 | Decision-maker patterns | Sales/GTM training | No | KEEP — Batch-010 | After personas |
| regulation_library | 0 | 1000 | Regulatory knowledge | Industry compliance | Industry regulation fields partial | KEEP — Batch-011 | High-trust OJK/Kemenperin path |

---

## Flags BEFORE large-scale production

### 1. `guidance.csv` — not a knowledge product
Meta documentation of sheets/columns. **Should not drive product coverage KPIs.**  
Verdict: keep file; exclude from training export defaults and coverage denominators.

### 2. `opportunity_analysis` seed quality
Broken Company ID references (Batch-Q1). Scaling before FK hygiene pollutes connectivity.  
Verdict: keep dataset; **hygiene before mass expansion**.

### 3. `case_study_library` illustrative patterns
Useful for structure, weak as factual case outcomes without public evidence.  
Verdict: keep; **strict DPS** — no fabricated ROI at scale.

### 4. Empty libraries (persona, regulation, competitor, signals, discovery)
Deserve roadmap slots; **do not fill with low-trust content** overnight just to raise counts.

### 5. Service as logical class inside `product_catalog`
Correct under frozen schema. Do not restructure; continue `Product Type=Service` counting toward `service_library` target.

---

## Charter alignment

Every **produced** knowledge library (industry → case spine) contributes to Coverage / Quality / Freshness / Export.  
Empty libraries are intentional backlog, not waste.

**No dataset should be deleted before overnight operation.**  
**Reconsider guidance as KPI input only.**
