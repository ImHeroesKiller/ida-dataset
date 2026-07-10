# IDA Executive Control Center (ECC)

Human-controlled operational cockpit for the IDA Knowledge Acquisition System.

## Philosophy

```text
Planner proposes → Policy governs → Human decides → Pipeline executes → Publisher publishes
```

IDA is **not autonomous**. ECC never bypasses Planner, Policy, Review, or Publisher.

## Stack

- Next.js (App Router)
- React
- Tailwind CSS v4
- Lightweight UI primitives (shadcn-style)
- Lucide icons

## Run (local)

From repository root:

```bash
cd ecc
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

Optional:

```bash
export IDA_REPO_ROOT=/absolute/path/to/ida-dataset
```

## Deploy (Vercel)

1. Import `ida-dataset` on Vercel  
2. Set **Root Directory** to `ecc`  
3. Framework: Next.js · Node 20+  
4. Deploy  

Details: [`docs/vercel.md`](../docs/vercel.md)

On Vercel, Python orchestration is skipped (use GitHub Actions). Read-only knowledge browsing stays fully available.

## Architecture

ECC is an **orchestration UI only**.

It reuses:

- `automation/ci/planner.py`
- `automation/ci/validate_repo.py`
- `automation/ci/review_summary.py`
- `automation/ci/publish_ci.py` (dry-run from UI)
- `automation/config/policies.yaml`
- `metadata/ontology/*`
- `domains/**`
- `reports/**`
- queue folders under `automation/queue/`

It does **not**:

- crawl
- run browser automation
- call LLMs
- open Neo4j
- edit production datasets directly
- live-publish without CI/policy gates

## Modules

| Route | Purpose |
| --- | --- |
| `/` | Status cockpit |
| `/planner` | Gaps, priorities, plan approve/reject |
| `/policies` | Policy matrix + draft edits |
| `/ontology` | CSV entity/relationship browser + SVG graph |
| `/datasets` | Read-only CSV browser |
| `/review` | Human review queue |
| `/publisher` | Dry-run publish controls |
| `/reports` | Report browser + download |
| `/settings` | Env + plugins |
| `/system` | Runtime / git / safe actions |

## Layout

- Left sidebar navigation
- Main workspace
- Right inspector
- Bottom streaming console
- Global progress strip

## Plugins

Future modules register in `lib/plugins.ts` without redesigning the shell:

- Knowledge Connectors
- Crawler
- Browser
- LLM Extraction
- Knowledge Graph
- RAG
- Fine Tuning
- Executive Agent

All plugins must set `respectsControlFlow: true`.

## Status colors

| Color | Meaning |
| --- | --- |
| Green | Healthy |
| Yellow | Waiting |
| Blue | Running |
| Red | Error |
| Grey | Disabled |
