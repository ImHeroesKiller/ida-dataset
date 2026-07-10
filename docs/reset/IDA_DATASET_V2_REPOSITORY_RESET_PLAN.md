# IDA Dataset v2.0 — Repository Reset Plan

**Phase:** 1 of 2 — Plan only (**no execution**)  
**Status:** Awaiting approval before Phase 2  
**Date:** 2026-07-10  
**Phase 1 commit:** `docs(reset): prepare repository reset plan for IDA Dataset v2.0`  
**Phase 2 commit (later):** `refactor(core): reset repository into IDA Dataset Knowledge Factory`

---

## 0. Product charter (binding)

| Field | Value |
|-------|--------|
| **Repository** | `ida-dataset` |
| **Product name** | **IDA Dataset Factory** |
| **Purpose** | Automatically produce high-quality structured datasets for LLM fine-tuning and knowledge corpus |
| **Inputs** | Mission · Trusted sources · Documents · Reports · Public data |
| **Outputs** | CSV · JSON · JSONL · Parquet · HuggingFace Dataset · OpenAI Fine-tuning Dataset |
| **Consumer** | IDA Intelligent Decision Automation (external product) |

### Non-goals (must leave this repository)

Decision Engine · Reasoning · Chatbot · Knowledge Graph · Business Intelligence · Executive AI · Agent Framework · Workflow Automation · Ontology browser · Network / Brain monitor · Learning “brain” UX

### Quality rule

Every remaining file must answer **yes** to:

> Does this file **directly** contribute to automatic dataset generation, factory monitoring, quality, or export?

If **no** → **DELETE** or **MOVE** out of `ida-dataset`.

---

## 1. Diagnosis: how the repo drifted

| Drift | Evidence today |
|-------|----------------|
| Product naming | Executive Control Center, Brain Monitor, Learning Brain |
| Frontend | **21** pages; public nav is 6 items + many operator/architecture pages |
| APIs | **27** route handlers (including deprecated 410 museum) |
| Concepts | Runtime SSE, ontology UI, planner UI, network, policies, ECC plugins |
| Docs | **~33** docs spanning ECC, runtime, ontology, knowledge network |
| Automation | Correct pipeline core buried under runtime / search / orchestrator bloat |

**Root cause:** Platform/ECC ambitions were built *inside* the dataset repo.  
**v2.0 correction:** This repo is **only** the automatic knowledge factory.

---

## 2. Repository tree — BEFORE (current)

```text
ida-dataset/
├── app/                 # 21 pages + 27 API routes (ECC + learning + factory mix)
├── components/          # shell, console, shared operator clients, UI
├── features/            # executive-dashboard, knowledge, missions, review, reports
├── hooks/               # learning-provider, use-learning-monitor
├── lib/                 # ~23 TS modules (kpis, sessions, network, orchestration, …)
├── plugins/             # ECC plugin residue
├── styles/ public/
├── automation/          # pipeline gold + runtime/search/missions/sessions bloat
│   ├── pipeline/        # discover → publish (KEEP core)
│   ├── connectors/      # collectors (KEEP, rename)
│   ├── scheduler/ missions/ ci/ config/
│   ├── learning/ sessions/ documents/ queue/
│   ├── runtime/         # DELETE (local runtime)
│   └── search/          # MERGE slim into collector
├── domains/             # KEEP — product datasets
├── metadata/            # KEEP schema/sources; slim ontology graph assets
├── exports/             # KEEP structure; implement real exporters
├── relationships/       # KEEP if training joins; else MOVE
├── reasoning/           # DELETE (non-goal)
├── templates/ examples/ # DELETE or MOVE
├── docs/                # REPLACE with charter set
├── reports/
├── .github/workflows/   # learning, planner, publish, review, validate
└── scripts/ package.* next.* vercel.json
```

### Approximate inventory (excl. `node_modules` / `.git`)

| Area | Files (approx.) |
|------|----------------:|
| `app/` | ~50 |
| UI (`components`/`features`/`hooks`) | ~28 |
| `lib/` | ~23 |
| `automation/` (incl. sessions/docs/queues) | ~200+ |
| `domains/` + `metadata/` | ~60 |
| `docs/` | ~33 |
| Other | ~40 |
| **Meaningful source** | **~400–500** |

---

## 3. Repository tree — AFTER (target)

```text
ida-dataset/
├── README.md                 # IDA Dataset Factory
├── VISION.md
├── PROJECT_CHARTER.md
├── ROADMAP.md
├── LICENSE · VERSION
├── package.json              # description: Automatic Knowledge Factory
├── next.config.ts · vercel.json · tsconfig.json
│
├── app/                      # Factory UI only
│   ├── page.tsx              # Dashboard
│   ├── datasets/ missions/ sources/ quality/
│   ├── exports/ logs/ settings/
│   └── api/
│       ├── factory/status/
│       ├── datasets/ missions/ sources/ quality/
│       ├── exports/ logs/ run/
│
├── components/
│   ├── layout/ ui/ factory/ theme-provider · chunk-error-recovery
│
├── lib/
│   ├── paths · csv · utils · safe-fetch · api-contract · simple-yaml
│   ├── nav · datasets · quality · missions · sources · exports
│   ├── factory-kpis · github-actions
│
├── automation/
│   ├── collector/            # was connectors + document queue
│   ├── extractor/            # extract + normalize
│   ├── validator/            # validate + dedupe + quality gate
│   ├── publisher/            # write datasets
│   ├── missions/             # templates + active missions
│   ├── quality/              # coverage, confidence, freshness, duplicates
│   ├── scheduler/            # mission prioritization
│   ├── export/               # CSV/JSON/JSONL/Parquet/HF/OpenAI
│   ├── logs/                 # factory activity (was journal/sessions UX)
│   ├── config/               # sources, quality, scheduler, export
│   ├── ci/                   # validate, learn, quality, publish, export
│   └── lib/                  # models, provenance, io, paths
│
├── domains/                  # append-only datasets
├── metadata/schema/ · source_registry · enums · taxonomy
├── exports/{csv,json,jsonl,parquet,huggingface,openai}/
├── reports/{quality,publish,export}/
├── docs/                     # 9 charter docs only (+ this reset plan)
├── .github/workflows/
│   ├── validate.yml · learn.yml · quality.yml · publish.yml · export.yml
└── scripts/factory-health.mjs
```

---

## 4. Classification legend

| Code | Meaning |
|------|---------|
| **KEEP** | Remains; may rename in place |
| **MOVE** | Leave ida-dataset (other product repo) or archive |
| **DELETE** | Remove; no long-term replacement |
| **MERGE** | Fold into another module; source removed |
| **RENAME** | Same role, factory naming |

Each decision includes: **Reason · Owner · Replacement · Impact**

---

## 5. Frontend classification

### 5.1 Pages

| Path | Decision | Reason | Owner | Replacement | Impact |
|------|----------|--------|-------|-------------|--------|
| `/` | **RENAME** content | Factory monitor, not executive learning | Frontend | Factory dashboard | High UX |
| `/datasets` | **KEEP** | Core product | Frontend | Dataset browser | — |
| `/missions` | **KEEP** | Mission = factory job | Frontend | Mission monitor | — |
| `/sources` | **KEEP** | Trusted source registry | Frontend | Source policy UI | — |
| `/settings` | **KEEP** | Factory config | Frontend | Settings | — |
| `/quality` | **RENAME** (new) | Quality first-class | Frontend | From review/reports | Medium |
| `/exports` | **RENAME** (new) | Export status | Frontend | From publisher | Medium |
| `/logs` | **RENAME** (new) | Factory activity | Frontend | From journal/console | Medium |
| `/knowledge` | **DELETE** | “Knowledge brain” UX | Frontend | `/datasets` | Nav shrink |
| `/review` | **MERGE** | Human gate = Quality | Frontend | `/quality` | Medium |
| `/reports` | **MERGE** | Artifacts = Quality/Exports | Frontend | `/quality`, `/exports` | Low |
| `/learning` `/publisher` `/queue` `/search` | **DELETE** | Redirect residue | Frontend | `/` or `/exports` | Low |
| `/ontology` `/planner` `/network` `/network-health` | **DELETE** | Non-goals | Frontend | — | High |
| `/connectors` `/connector-logs` | **DELETE** | ECC operator | Frontend | `/sources`, `/logs` | Medium |
| `/policies` `/system` `/documents` | **DELETE/MERGE** | Config/logs only | Frontend | config + logs | Medium |

**Pages after:** **8** · **Removed:** ~**13** (−62%)

### 5.2 API routes

| Path | Decision | Replacement |
|------|----------|-------------|
| `/api/datasets` | **KEEP** | — |
| `/api/missions` | **KEEP** | — |
| `/api/run` | **KEEP** slim | GHA dispatch only |
| `/api/sources` | **RENAME** (new) | From connectors/network |
| `/api/quality` | **MERGE** (new) | review + metrics |
| `/api/exports` | **RENAME** (new) | publish-queue role |
| `/api/logs` | **MERGE** (new) | journal + sessions tail |
| `/api/factory/status` | **MERGE** (new) | sessions + activity |
| `/api/sessions` | **MERGE** | logs/status |
| `/api/live/*` `/api/runtime/*` | **DELETE** | GHA only |
| `/api/console` `/status` `/git` | **DELETE** | — |
| `/api/ontology` `/planner` `/policies` | **DELETE** | — |
| `/api/network` `/connectors` `/documents` `/search` | **DELETE** | sources/logs |
| `/api/knowledge` `/learning` `/reports` | **MERGE** | datasets/quality |
| `/api/review` `/publish-queue` | **MERGE** | quality + publisher |

**APIs after:** **~8** · **Removed/merged:** **~20** (−70%)

### 5.3 Components / features / hooks

| Path | Decision | Replacement |
|------|----------|-------------|
| `features/dashboard/executive-dashboard.tsx` | **RENAME** | `components/factory/dashboard.tsx` |
| `features/missions/*` | **KEEP** slim | factory missions |
| `features/knowledge/*` | **DELETE** | Datasets |
| `features/review/*` | **MERGE** | Quality |
| `features/reports/*` | **MERGE** | Quality/Exports |
| `components/shared/ontology|planner|network|policy-client` | **DELETE** | — |
| `components/shared/datasets-client.tsx` | **KEEP** | — |
| `components/console/bottom-console.tsx` | **RENAME** | factory log strip (optional) |
| `components/layout/*` `ui/*` `chunk-error-recovery` | **KEEP** | Rebrand |
| `hooks/learning-provider` `use-learning-monitor` | **RENAME** | factory-provider / use-factory-monitor |

---

## 6. `lib/*` classification

| Path | Decision | Replacement |
|------|----------|-------------|
| `paths.ts` `csv.ts` `utils.ts` `safe-fetch.ts` `simple-yaml.ts` | **KEEP** | — |
| `nav.ts` | **RENAME** items | 8 factory routes |
| `github-actions.ts` | **KEEP** slim | learn/export dispatch |
| `api-contract.ts` | **KEEP** slim | — |
| `knowledge-kpis.ts` | **RENAME** | `factory-kpis.ts` |
| `repo-data.ts` `knowledge-catalog.ts` | **MERGE** | `datasets.ts` |
| `sessions.ts` | **MERGE** | missions/logs |
| `progressive-publish.ts` `review-actions.ts` | **MERGE** | automation publisher/quality |
| `learning.ts` `learning-mode.ts` `local-learning.ts` | **MERGE/DELETE** | factory mode + GHA |
| `network.ts` `plugins.ts` `orchestration.ts` | **DELETE** | — |
| `api/deprecated.ts` | **DELETE** after purge | No 410 museum |
| `status.ts` `use-learning-sessions.ts` | **MERGE/DELETE** | factory status |

---

## 7. Automation (Python) classification

| Path | Decision | Replacement |
|------|----------|-------------|
| `pipeline/*` (core stages) | **KEEP** + **RENAME** layout | collector/extractor/validator/publisher |
| `pipeline/entity_link.py` | **DELETE/MOVE** | KG non-goal (optional id resolve only) |
| `pipeline/reviewer.py` | **MERGE** | validator + quality queue |
| `connectors/*` | **RENAME** | `collector/` |
| `connectors/builtin/stubs.py` | **DELETE** | No fake data |
| `scheduler/*` `missions/*` `config/*` | **KEEP** slim | Mission factory |
| `ci/learning_session.py` | **RENAME** | `ci/learn.py` |
| `ci/industry_knowledge_cycle.py` | **KEEP** | Real generation job |
| `ci/publish_ci.py` `progressive_publish.py` `validate_repo.py` | **KEEP** | — |
| `ci/validate_ontology.py` | **DELETE** | Schema validate only |
| `ci/planner.py` `review_summary.py` | **MERGE** | learn/quality jobs |
| `learning/*` (journal, growth) | **MERGE** | quality + logs |
| `learning/live_runtime.py` `first_cycle.py` | **DELETE** | GHA learn only |
| `runtime/*` | **DELETE** | Local runtime dead |
| `search/*` | **MERGE** slim | Inside collector |
| `orchestrator.py` | **DELETE/MERGE** | scheduler + learn |
| `sessions/*` `documents/*` `queue/*` | **KEEP** as logs/state | gitignore noise |
| `lib/*` (models, provenance) | **KEEP** | — |

---

## 8. Domains, metadata, exports, other

| Path | Decision | Reason |
|------|----------|--------|
| `domains/**/*.csv` | **KEEP** | Product (append-only) |
| `metadata/schema/*` `source_registry.csv` | **KEEP** | Schema + sources |
| `metadata/enums/*` `taxonomy.csv` | **KEEP** if validation uses | Controlled vocab |
| `metadata/ontology/**` | **DELETE/MOVE** | KG non-goal |
| `metadata/connectors/*` | **MERGE** | Collector registry |
| `metadata/entity_relationship.csv` | **DELETE/MOVE** | Graph |
| `exports/*` | **KEEP** + expand | HF/OpenAI dirs |
| `relationships/*` | **KEEP** if training joins else **MOVE** | Evaluate |
| `reasoning/*` | **DELETE** | Non-goal |
| `templates/*` `examples/*` `plugins/*` | **DELETE/MOVE** | Not factory |

---

## 9. Documentation

### Living docs after reset (only)

| New doc | Built from |
|---------|------------|
| `VISION.md` | Rewrite `docs/vision.md` (factory only) |
| `PROJECT_CHARTER.md` | This charter |
| `ROADMAP.md` | Slim `docs/roadmap.md` |
| `ARCHITECTURE.md` | Factory pipeline only |
| `DATASET_SCHEMA.md` | `metadata/schema/*` + data dictionary |
| `SOURCE_POLICY.md` | sources.yaml + source_registry |
| `QUALITY_POLICY.md` | New |
| `EXPORT_GUIDE.md` | New |
| `CONTRIBUTING.md` | `docs/contribution.md` |

### Existing docs

| Path | Decision |
|------|----------|
| `docs/vision|architecture|roadmap|contribution|data_dictionary|github_actions|vercel` | **MERGE** into charter set |
| `docs/ecc|runtime*|ontology/**|knowledge_network|search_orchestrator|learning_dashboard` | **DELETE** |
| `docs/connector_*|mission_system|learning_scheduler|document_queue` | **MERGE** slim → ARCHITECTURE |
| `docs/kas|learning_contract|resource_allocation` | **DELETE/MERGE** |
| `docs/audit/**` | **KEEP** optional archive or DELETE after Phase 2 |
| `docs/reset/**` | **KEEP** (this plan) |

---

## 10. GitHub Actions

| Workflow | Decision | Replacement |
|----------|----------|-------------|
| `validate.yml` | **KEEP** | — |
| `learning.yml` | **RENAME** | `learn.yml` |
| `publish.yml` | **KEEP** | — |
| `review.yml` | **RENAME** | `quality.yml` |
| `planner.yml` | **DELETE/MERGE** into learn | learn step |

**Target only:** `validate` · `learn` · `quality` · `publish` · `export`

---

## 11. Migration plan (Phase 2 — do not start until approved)

### Stage A — Freeze
1. Branch `reset/v2-knowledge-factory`  
2. Tag `pre-reset-v1`  
3. Optional: quiet noisy non-factory workflows  

### Stage B — Backend layout
1. Create `automation/{collector,extractor,validator,publisher,quality,export,logs}/`  
2. Move/rename pipeline + connectors (thin shims if needed)  
3. Delete runtime, live_runtime, ontology CI, search product surface  
4. Add export packagers (JSONL/Parquet/HF/OpenAI)  

### Stage C — Data & metadata
1. Freeze domain schemas (append-only)  
2. Remove unused ontology graph assets after import audit  
3. Enforce provenance on every publish  

### Stage D — Frontend cutover
1. Nav = 8 factory routes only  
2. Factory dashboard metrics only  
3. Delete non-goal pages/APIs/components  
4. Rebrand to **IDA Dataset Factory**  

### Stage E — Docs & CI
1. Write 9 charter docs; remove/archive rest  
2. Align workflows to 5 factory jobs  
3. Update README + Vercel description  

### Stage F — Verify
1. `npm run build` green  
2. learn → publish → export path green  
3. Quality metrics compute  
4. No ontology/network/planner/brain routes  

### Stage G — Merge
PR with: `refactor(core): reset repository into IDA Dataset Knowledge Factory`

---

## 12. Architecture diagram (target)

```text
                 ┌──────────────────────┐
                 │  Mission + Scheduler │
                 └──────────┬───────────┘
                            │
                            ▼
┌──────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐
│Collector │─▶│ Extractor │─▶│ Validator │─▶│ Publisher │
└──────────┘  └───────────┘  └───────────┘  └─────┬─────┘
                                                  │
                         domains/*.csv  ◀─────────┘
                                  │
                                  ▼
                            ┌──────────┐
                            │  Export  │──▶ JSONL / Parquet / HF / OpenAI
                            └──────────┘
                                  │
                                  ▼
                     Dataset Factory Dashboard
                     (status · quality · logs)
```

No Decision Engine. No Reasoning. No Chatbot. No Knowledge Graph UI.

---

## 13. Statistics (planned impact)

| Metric | Before | After (target) | Δ |
|--------|-------:|---------------:|---|
| Page routes | 21 | **8** | **−62%** |
| API routes | 27 | **~8** | **−70%** |
| Public nav focus | ECC + learning mix | **Factory only** | Clarity |
| Living docs | ~33 | **9** | **−70%** |
| GHA workflows | 5 | **5** (realigned) | Clearer |
| TS surface (app+UI+lib) | ~100 files | **~40–50** | **~50%** |
| Non-goal dirs (reasoning, runtime, ontology UI, plugins) | Present | **Removed** | High |
| First Load JS | ~126 kB home | **−15–30% expected** | Drop heavy clients |
| Cognitive load | ECC + Factory | **Factory only** | Primary win |

### Classification roll-up (estimate)

| Decision | Est. files |
|----------|-----------:|
| KEEP | 120–150 |
| RENAME / MERGE | 80–100 |
| DELETE | 100–150 |
| MOVE out | 20–40 |

---

## 14. Risk analysis

| Risk | Sev | Mitigation |
|------|-----|------------|
| Break publish path | High | Shims in Stage B; dry-run publish; keep provenance tests |
| Vercel deploy break | High | Keep next/vercel; only slim routes |
| GHA learn regression | High | Careful workflow rename; update secrets/docs |
| Lose session history | Medium | Keep under `logs/missions/` |
| Ontology used by validators | Medium | Import audit before delete |
| External callers of old APIs | Medium | CHANGELOG breaking note |
| Re-adding ECC later | High | Charter check on every PR |

---

## 15. Impact analysis

| Stakeholder | Impact |
|-------------|--------|
| Dataset quality / LLM training | **Positive** — provenance, coverage, export focus |
| Current ECC / Brain UI users | **Breaking** rename/removal (intended) |
| IDA Decision product | Lives **elsewhere**; consumes exports only |
| Ops | Smaller surface, fewer routes |
| Contributors | Clearer onboarding via 9 docs |

---

## 16. Delete checklist (Phase 2)

**High confidence**

- Pages: ontology, planner, network*, policies, system, connectors*, knowledge, learning, publisher, queue, search  
- APIs: runtime/**, live/**, ontology, planner, policies, network, connectors, console, status, git, search  
- Components: ontology/planner/network/policy clients; features/knowledge  
- Python: `automation/runtime/**`, `learning/live_runtime.py`  
- Data/docs: `reasoning/**`, `examples/**`, `plugins/**`, ECC/runtime/ontology docs  

**Conditional (audit first)**

- `pipeline/entity_link.py`  
- `metadata/ontology/**`  
- `relationships/**`  
- `templates/**`  

---

## 17. Move checklist (out of ida-dataset)

| Asset | Destination concept |
|-------|---------------------|
| Decision / reasoning content | IDA Decision / Reasoning repo |
| Executive AI / ECC UX | IDA App / ECC repo |
| Knowledge Graph / ontology browser | Graph product repo |
| Agent / workflow frameworks | Orchestration repo |

---

## 18. Merge checklist

| From | Into |
|------|------|
| repo-data + knowledge-catalog | `lib/datasets.ts` |
| knowledge-kpis + journal metrics | `lib/factory-kpis.ts` |
| review-actions + validate | `automation/quality` + `/api/quality` |
| progressive-publish + pipeline publisher | `automation/publisher` |
| journal + sessions index | `automation/logs` |
| Overlapping docs | 9 charter docs |

---

## 19. Rename checklist

| From | To |
|------|-----|
| Executive Learning / Brain Monitor | **IDA Dataset Factory** |
| `learning.yml` | `learn.yml` |
| `review.yml` | `quality.yml` |
| `connectors/` | `collector/` |
| `executive-dashboard.tsx` | `factory-dashboard.tsx` |
| `learning-provider` | `factory-provider` |

---

## 20. Phase 2 acceptance criteria

- [ ] Nav only: Dashboard · Datasets · Missions · Sources · Quality · Exports · Logs · Settings  
- [ ] No ontology / network / planner / brain / executive AI surfaces  
- [ ] learn → publish → export green in CI  
- [ ] Every published row has provenance  
- [ ] Living docs = 9 charter files (+ optional archive)  
- [ ] Workflows = validate, learn, quality, publish, export  
- [ ] README describes Automatic Knowledge Factory only  
- [ ] Measurable route/component/doc reduction (§13)  

---

## 21. Phase 1 non-actions (confirmed)

| Action | Status |
|--------|--------|
| Delete / move / rename product code | **Not done** |
| Change workflows | **Not done** |
| Reset git history | **Not planned** |

**Phase 1 deliverable = this report only.**

---

## 22. Approval gate

Phase 2 starts only after explicit approval of:

1. Target tree (§3)  
2. Delete list (§16)  
3. Migration order (§11)  
4. Phase 2 commit message:  
   `refactor(core): reset repository into IDA Dataset Knowledge Factory`

---

## 23. Final goal

> **The Factory that continuously produces high-quality datasets for training future IDA language models.**

Nothing more.

---

*End of Phase 1 Repository Reset Plan.*
