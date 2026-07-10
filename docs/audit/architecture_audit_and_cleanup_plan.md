# Repository Architecture Audit & Cleanup Plan

**Status:** Audit only — no feature work, no UI redesign, no automatic deletions  
**Date:** 2026-07-10  
**Commit intent:** `docs(audit): complete repository architecture audit and cleanup plan`  
**Scope:** Entire `ida-dataset` repository (ECC + automation + knowledge assets)

---

## Executive summary

The repository implements a **frozen knowledge-learning architecture** (Scheduler → Planner → Policy → Connector → Pipeline → Review → Publisher → Telemetry) with an **Executive Control Center (ECC)** Next.js app at the repo root.

Multiple sprints layered:

1. KAS / CI foundations  
2. Continuous learning scheduler + live runtime  
3. GitHub Actions session execution  
4. Executive UX simplification + review fix  
5. Theme polish + development progressive auto-publish  

**Result:** Core learning path works, but the tree contains **legacy routes, orphaned modules, dual styling systems, and dead local-runtime APIs** from earlier layers. Navigation intentionally exposes only **6 executive routes**; ~15 additional pages remain reachable by URL as internal/legacy surfaces.

**This document is the reference architecture and the only allowed next step before further product work.**

---

# 1. Repository Architecture Report

## 1.1 Intended architecture (frozen)

```text
Human / Mission / Schedule
        ↓
Continuous Learning Scheduler
        ↓
Priority Engine → Planner → Policy
        ↓
Connector Manager / Search Orchestrator
        ↓
Document Queue → Pipeline (validate)
        ↓
Review Queue  ──(production)──► Human Review
        ↓ (development: review bypassed)
Publish Queue → Progressive Auto Publish (rate-limited)
        ↓
domains/*.csv (append-only knowledge)
        ↓
Sessions / Feed / Journal / Dashboard
```

**Execution model (current):**

```text
GitHub Actions (learning.yml)  →  learning_session.py  →  repo updates
Dashboard (Vercel / local)     →  monitor sessions + dispatch + review/publish UI
```

## 1.2 Top-level tree (authoritative)

| Path | Role | Notes |
|------|------|--------|
| `app/` | Next.js App Router (ECC) | Pages + API routes |
| `components/` | React UI | layout / shared / ui / console |
| `lib/` | ECC server/client utilities | No domain engines |
| `automation/` | Python KAS engines + CI | Frozen architecture body |
| `domains/` | Knowledge datasets (CSV) | Product knowledge |
| `metadata/` | Ontology, schema, enums | |
| `relationships/` | Entity relationship CSVs | |
| `config/environments/` | dev/staging/prod profiles | |
| `reports/` | CI / learning reports | Often gitignored partially |
| `docs/` | Product & architecture docs | |
| `.github/workflows/` | GHA learning/validate/publish | |
| `ecc/` | Legacy residual (`public/`, README) | **Obsolete root for app** — app moved to repo root |
| `plugins/` | Plugin registry metadata | Thin |
| `examples/`, `templates/`, `reasoning/`, `exports/` | Supporting assets | Low coupling to ECC |

## 1.3 Architecture layers

| Layer | Location | Mutates knowledge? |
|-------|----------|--------------------|
| Presentation | `app/`, `components/` | No (except review/publish APIs writing queue/CSV) |
| ECC bridge | `lib/*` | Queue / session / publish state only |
| Orchestration | `automation/scheduler/` | State under `automation/scheduler/state/` |
| Acquisition | `automation/connectors/`, `automation/search/` | Documents, cache |
| Pipeline | `automation/pipeline/` | Candidates, CSV append |
| Runtime (legacy) | `automation/runtime/`, `automation/learning/live_runtime.py` | Session/journal; GHA path preferred |
| CI | `automation/ci/` | Reports + learning sessions + progressive publish |

## 1.4 Complexity snapshot

| Metric | Approx. |
|--------|---------|
| Source files (ts/tsx/py/md/yaml, excl. node_modules) | ~335 tracked-relevant |
| App pages (`page.tsx`) | 21 |
| API routes (`route.ts`) | 27 |
| React components (tsx under `components/`) | 28 |
| `lib/*.ts` modules | 26 |
| Python modules under `automation/` | ~75 |
| GHA workflows | 5 |
| Executive nav items | 6 |
| Hidden / legacy pages still in tree | ~15 |

---

# 2. Route Map

## 2.1 Executive sidebar routes (KEEP — product surface)

| Route | Page | Primary client | Purpose |
|-------|------|----------------|---------|
| `/` | `app/page.tsx` | `executive-dashboard` | Executive home |
| `/knowledge` | `app/knowledge/page.tsx` | `knowledge-client` | Knowledge catalog |
| `/missions` | `app/missions/page.tsx` | `missions-client` | Learning missions |
| `/review` | `app/review/page.tsx` | `review-client` | Human review / approve |
| `/reports` | `app/reports/page.tsx` | `reports-client` | Session history stats |
| `/settings` | `app/settings/page.tsx` | (inline) | Mode + environment |

Defined in `lib/nav.ts` → `NAV_ITEMS`.

## 2.2 Internal / engineering pages (still mounted, not in nav)

| Route | Status | Recommendation |
|-------|--------|----------------|
| `/learning` | Learning Brain dashboard | **KEEP internal** or merge into `/` later |
| `/planner` | Gap planner UI | **KEEP internal** |
| `/policies` | Policy viewer | **KEEP internal** |
| `/publisher` | Publish controls | **KEEP internal** (overlaps progressive publish) |
| `/datasets` | Dataset browser | **MERGE** into `/knowledge` long-term |
| `/ontology` | Ontology browser | **KEEP internal** |
| `/network` | Knowledge network | **KEEP internal** |
| `/sources` | Sources list | **KEEP internal** |
| `/documents` | Document queue UI | **KEEP internal** |
| `/system` | Ops / run actions | **KEEP internal** |

## 2.3 Redirect-only routes

| Route | Redirects to | Recommendation |
|-------|--------------|----------------|
| `/queue` | `/documents` | **KEEP** redirect or **REMOVE** after link audit |
| `/connectors` | (redirect) | **KEEP** stub |
| `/connector-logs` | (redirect) | **KEEP** stub |
| `/network-health` | (redirect) | **KEEP** stub |
| `/search` | `/network` | **KEEP** stub (search lives in topbar) |

## 2.4 Missing product routes

| Concern | Finding |
|---------|---------|
| Dedicated `/404` | Default Next.js only — no custom `not-found.tsx` |
| Auth / multi-tenant | None (by design) |
| Nested App Router segments | Flat pages only (no route groups for executive vs internal) |

## 2.5 Route cleanup list (non-destructive)

| Action | Routes | Reason |
|--------|--------|--------|
| **KEEP** | 6 executive routes | Product surface |
| **KEEP** | Internal engineering pages | Needed for operators; not in nav |
| **KEEP** | Redirect stubs | Avoid broken bookmarks |
| **REMOVE (later)** | None until Phase cleanup sprint | Audit only |
| **ADD (later)** | `app/not-found.tsx` | Executive 404 |
| **REFACTOR (later)** | Route groups `(executive)` / `(internal)` | Clarity without changing architecture |

---

# 3. API Map

## 3.1 Active product APIs (used by executive surface)

| Endpoint | Methods | Consumers | Role |
|----------|---------|-----------|------|
| `GET/POST /api/sessions` | GET | `use-learning-sessions` | Session monitor |
| `POST /api/live/start` | POST | `use-learning-sessions` | GHA dispatch / local session |
| `GET /api/publish-queue` | GET, POST | executive-dashboard, bottom-console | Progressive publish |
| `GET/POST /api/review` | GET, POST | review-client | Approve/reject/publish |
| `GET /api/knowledge` | GET | knowledge-client | Category tables |
| `GET /api/journal` | GET | executive-dashboard | KPI refresh |
| `GET /api/learning` | GET, POST | missions-client, learning-client | Scheduler bridge |
| `GET /api/missions` | GET | missions-client | Mission list |
| `GET /api/search` | GET | topbar | Global search |

## 3.2 Legacy / dual-stack learning APIs

| Endpoint | Consumers | Status |
|----------|-----------|--------|
| `GET /api/live` | live-sse-bus, use-live-learning (orphaned chain) | **DEPRECATED** snapshot/SSE remnant |
| `GET /api/live/replay` | use-live-learning only | **DEPRECATED** (sessions supersede) |
| `GET /api/runtime/status` | use-live-learning only | **ORPHANED** after GHA migration |
| `GET /api/runtime/logs` | use-live-learning only | **ORPHANED** |
| `GET /api/runtime/session` | none | **ORPHANED** |
| `GET /api/runtime/debug` | api-contract string refs / dead clients | **ORPHANED** |

## 3.3 Internal page APIs

| Endpoint | Consumers | Recommendation |
|----------|-----------|----------------|
| `/api/datasets` | datasets-client | KEEP internal |
| `/api/network` | network-client | KEEP internal |
| `/api/run` | run-actions, publisher-client | KEEP internal |
| `/api/console` | progress-bar only | **ORPHAN** (progress-bar unused) |
| `/api/connectors` | none | **ORPHAN** |
| `/api/documents` | none | **ORPHAN** (page uses lib direct) |
| `/api/git` | none | **ORPHAN** |
| `/api/ontology` | none | **ORPHAN** (page uses lib) |
| `/api/planner` | none | **ORPHAN** (page uses lib) |
| `/api/policies` | none | **ORPHAN** (page uses lib) |
| `/api/reports` | none | **ORPHAN** (reports page uses sessions lib) |
| `/api/status` | none | **ORPHAN** |

## 3.4 API dependency map (simplified)

```text
executive-dashboard ─┬─ /api/sessions (via useLearningSessions)
                     ├─ /api/live/start
                     ├─ /api/journal
                     └─ /api/publish-queue

bottom-console ──────┬─ /api/sessions (via useLearningSessions)  [double poll]
                     └─ /api/publish-queue

review-client ───────── /api/review
knowledge-client ────── /api/knowledge
missions-client ─────── /api/learning, /api/missions
topbar ──────────────── /api/search
```

## 3.5 API cleanup recommendations

| Action | Items | Reason |
|--------|-------|--------|
| **KEEP** | sessions, live/start, publish-queue, review, knowledge, journal, learning, missions, search | Product |
| **DEPRECATE** | live (SSE), live/replay, runtime/* | Superseded by sessions + GHA |
| **REMOVE (later)** | console, status, connectors, git, unused ontology/planner/policies/reports APIs | Zero consumers |
| **MERGE (later)** | journal into sessions or publish-queue | Fewer poll endpoints |

---

# 4. Component Map

## 4.1 Component tree

```text
components/
  theme-provider.tsx          # light/dark
  console/
    bottom-console.tsx        # Learning Journal (global via Shell)
  layout/
    shell.tsx                 # Sidebar + Topbar + Main + Console
    sidebar.tsx
    topbar.tsx
    inspector.tsx             # NOT mounted in Shell anymore
    inspector-context.tsx     # still imported by internal clients
  dashboard/
    status-card.tsx           # ORPHAN
  shared/
    executive-dashboard.tsx   # HOME
    knowledge-client.tsx
    missions-client.tsx
    review-client.tsx
    reports-client.tsx
    learning-client.tsx       # /learning only
    live-dashboard.tsx        # ORPHAN (replaced by executive-dashboard)
    live-progress.tsx         # only live-dashboard
    progress-bar.tsx          # ORPHAN (removed from Shell)
    datasets-client.tsx
    network-client.tsx
    ontology-client.tsx
    planner-client.tsx
    policy-client.tsx
    publisher-client.tsx
    run-actions.tsx
  ui/
    button.tsx, card.tsx, input.tsx, badge.tsx
```

## 4.2 KEEP / MERGE / REMOVE / REFACTOR

| Component | Action | Reason |
|-----------|--------|--------|
| `executive-dashboard` | **KEEP** | Canonical home |
| `knowledge-client`, `missions-client`, `review-client`, `reports-client` | **KEEP** | Executive pages |
| `bottom-console`, `shell`, `sidebar`, `topbar`, `theme-provider` | **KEEP** | Shell chrome |
| `ui/*` | **KEEP** | Design primitives |
| `live-dashboard` | **REMOVE (later)** | Fully replaced; zero imports |
| `live-progress` | **REMOVE (later)** with live-dashboard | Only child of orphan |
| `progress-bar` | **REMOVE (later)** | Unmounted; only `/api/console` consumer |
| `status-card` | **REMOVE (later)** | Orphan |
| `learning-client` | **MERGE (later)** into executive or keep internal | Duplicates mission/brain metrics |
| Internal `*-client` pages | **KEEP** | Operator tools |
| `inspector` + context | **REFACTOR** | Clients call `useInspector` but Shell no longer provides provider → **runtime risk** on internal pages |

## 4.3 Duplication findings

| Concern | Instances | Recommendation |
|---------|-----------|----------------|
| Learning status polling | `useLearningSessions` in **dashboard + console** | **MERGE** to single provider |
| Knowledge metrics | knowledge-kpis + publish-queue + journal | **REFACTOR** single read model |
| Review vs Publisher UI | review-client + publisher-client | Keep both; document roles |
| Old live vs GHA sessions | live-dashboard vs executive-dashboard | Delete live path later |

---

# 5. Layout & Design System Audit

## 5.1 Shell composition (current)

```text
Shell
├── Sidebar (nav + theme toggle)
└── column
    ├── Topbar (title + search)
    ├── main (page content)
    └── BottomConsole (journal)
```

**Removed from Shell (vs earlier sprints):** `ProgressBar`, `InspectorPanel`, `InspectorProvider`.

## 5.2 Design tokens

| Source | Tokens |
|--------|--------|
| `app/globals.css` `:root` / `.dark` | `--bg`, `--panel`, `--text`, button colors, spacing vars |
| Tailwind utility classes | Many residual `zinc-*`, `sky-*`, `emerald-*` |
| Hardcoded hex | Sidebar/legacy cards still mix systems |

**Counts (approx.):**

- `zinc-*` utilities in components: **~330**  
- `var(--*)` usages in components: **~126**  
- `text-zinc-50` / `text-zinc-100` still common on internal pages  

## 5.3 Button variants (`components/ui/button.tsx`)

| Variant | Intent | Contrast |
|---------|--------|----------|
| primary/default | Blue solid | OK (white on blue) |
| secondary | Panel bg | OK via CSS vars |
| success / warning / danger | Solid | OK |
| ghost / outline | Border/text | OK if `--text` used |

**Debt:** Internal pages still may rely on old mental model of zinc-on-zinc; executive surfaces partially migrated to CSS variables.

## 5.4 Layout consistency checklist

| Item | Executive pages | Internal pages |
|------|-----------------|----------------|
| Shell | Yes | Yes (most) |
| Max width `max-w-6xl` | Mostly | Inconsistent |
| Card `rounded-2xl` + CSS vars | New pages | Often zinc borders |
| Inspector | N/A | Broken without provider |
| Empty states | Partial | Partial |

## 5.5 Design system recommendations (no implementation now)

1. **Single token layer** — all colors via CSS variables; ban new `zinc-*` in product pages.  
2. **Restore or remove inspector** — either remount `InspectorProvider` in Shell or strip `useInspector` from clients.  
3. **Shared metric card** — extract one `StatCard` used by dashboard/reports (today duplicated inline).  
4. **Typography scale** — document h1/h2/body/mono sizes (Inter already loaded).  

---

# 6. Import & Hook Audit

## 6.1 Orphaned lib modules

| Module | Action | Reason |
|--------|--------|--------|
| `lib/runtime-manager.ts` | **REMOVE (later)** or quarantine | No importers after GHA migration |
| `lib/sse-registry.ts` | **REMOVE (later)** | SSE listener bookkeeping unused |
| `lib/use-live-learning.ts` | **REMOVE (later)** | Superseded by `use-learning-sessions` |
| `lib/live-sse-bus.ts` | **REMOVE (later)** | Only used by use-live-learning |

## 6.2 Active lib modules (KEEP)

| Module | Role |
|--------|------|
| `sessions`, `github-actions`, `local-learning` | GHA learning model |
| `progressive-publish`, `learning-mode` | Dev auto publish |
| `review-actions` | Approve/reject/publish |
| `knowledge-kpis`, `knowledge-catalog` | Dashboard / knowledge |
| `learning`, `repo-data`, `paths`, `csv` | Core bridges |
| `safe-fetch`, `api-contract`, `utils`, `nav`, `status` | Shared |

## 6.3 Circular dependencies

Lib import graph is **acyclic** (tree-shaped):

```text
progressive-publish → learning-mode, paths, review-actions
review-actions → paths, repo-data
use-learning-sessions → safe-fetch
use-live-learning → live-sse-bus, safe-fetch  (dead branch)
```

No circular dependency detected in `lib/`.

## 6.4 Double-subscription risk

| Issue | Detail |
|-------|--------|
| `useLearningSessions` | Instantiated in **executive-dashboard** and **bottom-console** → dual 5s polling of `/api/sessions` |
| Publish polling | Dashboard and console both hit `/api/publish-queue` |

**REFACTOR (later):** `LearningSessionProvider` at Shell level.

---

# 7. Folder Audit

## 7.1 Keep as-is (frozen architecture)

- `automation/{scheduler,pipeline,connectors,search,learning,ci,lib,missions,queue}`  
- `domains/`, `metadata/`, `relationships/`  
- `config/environments/`  
- `app/`, `components/`, `lib/`  

## 7.2 Folder recommendations

| Path | Action | Reason |
|------|--------|--------|
| `ecc/` | **REMOVE (later)** or document as legacy | App lives at repo root; only residual public/README |
| `automation/runtime/` | **KEEP** (Python lifecycle for live_runtime/GHA) | Still used by learning session body |
| `automation/sessions/` | **KEEP** | GHA session storage |
| `automation/queue/publish/` | **KEEP** | Progressive publish |
| `components/dashboard/` | **REMOVE (later)** if status-card deleted | Near-empty |
| `hooks/` | N/A | Hooks live under `lib/use-*.ts` (no `hooks/` folder) |
| `styles/` | N/A | Only `app/globals.css` |

## 7.3 Proposed long-term app structure (optional, not now)

```text
app/
  (executive)/page, knowledge, missions, review, reports, settings
  (internal)/learning, planner, policies, publisher, datasets, ...
  api/...
```

---

# 8. Dashboard / Page Audit

## 8.1 Executive pages — design language

| Page | Design system | Notes |
|------|---------------|-------|
| Dashboard | CSS vars + cards | Source of truth for executive look |
| Knowledge | CSS vars | Empty states present |
| Missions | Mixed zinc utilities | **Inconsistent** with dashboard |
| Review | Partial vars + zinc | Slide-over works; styling drift |
| Reports | Mixed | Tabs OK |
| Settings | CSS vars | Mode display OK |

## 8.2 Duplicated product concepts

| Concept | Locations |
|---------|-----------|
| Knowledge coverage / growth | Dashboard KPIs, reports history, learning-client |
| Mission status | Dashboard, missions, learning brain |
| Publish progress | Dashboard publish-queue only (good) |
| Review queue | Review page + dashboard “waiting review” |

---

# 9. Functional Audit (visible interactions)

## 9.1 Executive interactions

| Interaction | Works? | Feedback | Notes |
|-------------|--------|----------|-------|
| Sidebar navigation (6 items) | Yes | Active state | |
| Theme toggle | Yes | Persists localStorage | |
| Topbar search | Yes | Dropdown results | Maps some hrefs to executive routes |
| Start Learning | Yes* | Message string | *Needs GHA token on Vercel; local oneshot fallback |
| Publish queue progress | Yes | Poll-driven | Backend rate limit on GET |
| Review approve/reject | Yes | Message + queue refresh | FS write; fails on Vercel RO |
| Knowledge category open | Yes | Table load | |
| Reports tabs | Yes | Client filter | |
| Learning journal console | Yes | Live poll | Human verbs |

## 9.2 Broken / risky interactions

| Interaction | Issue | Severity |
|-------------|-------|----------|
| Inspector `inspect()` on missions/datasets/planner/ontology | Shell no longer wraps `InspectorProvider` — context default may no-op or throw | **High** on internal pages |
| `/api/runtime/*` if any old client remains | Dead local runtime model | Medium |
| Progress bar | Removed from UI; API still exists | Low |
| Publisher page vs progressive publish | Two mental models for publish | Medium (UX debt) |
| Production mode review path | Config exists; less exercised than development | Medium |

## 9.3 Silent failure patterns observed in code

- Many `catch { /* ignore */ }` in dashboard polls — intentional resilience, but can hide misconfiguration.  
- Start Learning returns structured errors when GHA missing — good.  
- Review on read-only FS returns error codes — good.

---

# 10. Dependency Graphs

## 10.1 Route tree

```text
/                     → ExecutiveDashboard
/knowledge            → KnowledgeClient
/missions             → MissionsClient
/review               → ReviewClient
/reports              → ReportsClient
/settings             → Settings (static + mode)
/learning             → LearningClient          [hidden]
/planner              → PlannerClient           [hidden]
/policies             → PolicyClient            [hidden]
/publisher            → PublisherClient         [hidden]
/datasets             → DatasetsClient          [hidden]
/ontology             → OntologyClient          [hidden]
/network              → NetworkClient           [hidden]
/sources, /documents, /system                   [hidden]
/queue → /documents
/search → /network
/connectors, /connector-logs, /network-health   [redirects]
```

## 10.2 Component dependency (executive)

```text
layout.tsx → ThemeProvider
Shell → Sidebar, Topbar, BottomConsole
  Sidebar → nav, useTheme
  Topbar → /api/search
  BottomConsole → useLearningSessions, /api/publish-queue
page.tsx → ExecutiveDashboard
  → useLearningSessions, /api/journal, /api/publish-queue
```

## 10.3 Automation dependency (learning run)

```text
learning.yml
  → automation/ci/learning_session.py
      → live_runtime.run_live_session
          → scheduler, search, pipeline pieces, journal
      → progressive_publish.py (if not dry-run)
          → queue/publish → domains CSV + feed + journal
```

## 10.4 Import graph (ECC product path)

```text
app/page → executive-dashboard → use-learning-sessions → safe-fetch
                              → publish-queue API → progressive-publish
                                                   → learning-mode
                                                   → review-actions → repo-data
app/review → review-client → /api/review → review-actions
app/knowledge → knowledge-client → /api/knowledge → knowledge-catalog → repo-data
```

---

# 11. Technical Debt Report

| ID | Debt | Impact | Effort |
|----|------|--------|--------|
| TD-01 | Dual design systems (CSS vars vs zinc utilities) | Visual inconsistency | M |
| TD-02 | Orphan live-runtime UI stack | Confusion, bundle noise | S |
| TD-03 | Orphan runtime APIs | False sense of local runtime | S |
| TD-04 | Inspector detached from Shell | Broken internal inspect | S |
| TD-05 | Double session/publish polling | Extra load, racey state | M |
| TD-06 | ~15 hidden pages without IA grouping | Hard onboarding | M |
| TD-07 | `ecc/` leftover directory | Deploy confusion historically | S |
| TD-08 | API endpoints with zero consumers | Maintenance cost | S |
| TD-09 | Journal/feed/session state scattered | Hard to reason about “source of truth” | M |
| TD-10 | Vercel read-only vs local write review/publish | Env-specific failures | Known constraint |
| TD-11 | missions UI style lagging executive theme | Looks unfinished | S |
| TD-12 | No custom `not-found` / error boundaries | Poor executive empty errors | S |

---

# 12. Cleanup Plan (non-destructive recommendations)

## 12.1 KEEP

- Frozen Python architecture under `automation/`  
- Executive 6 routes + their clients  
- GHA workflows + `learning_session` + `progressive_publish`  
- Session storage `automation/sessions/`  
- Review queue paths + `review-actions`  
- Design tokens in `globals.css` (extend, don’t replace)  
- Internal operator pages until product explicitly drops them  

## 12.2 MERGE

| Merge | Into | Reason |
|-------|------|--------|
| live-dashboard concepts | executive-dashboard | Already done; delete leftover files later |
| learning-client metrics | dashboard/reports | Avoid second “brain” home |
| datasets browser | knowledge | Single knowledge entry |
| journal + sessions poll | one provider | Single subscription |
| Duplicate StatCard implementations | `components/ui/stat-card.tsx` | Consistency |

## 12.3 RENAME

| Current | Suggested | Reason |
|---------|-----------|--------|
| `use-learning-sessions` | `useLearningMonitor` | Not only sessions |
| `/api/live/start` | `/api/learning/start` (later) | “live” implies local runtime |
| `live_runtime.py` | keep name | Used by GHA; rename risk high |

## 12.4 REMOVE (later sprint only — do not delete now)

| Target | Reason |
|--------|--------|
| `components/shared/live-dashboard.tsx` | Orphan |
| `components/shared/live-progress.tsx` | Orphan dependency |
| `components/shared/progress-bar.tsx` | Orphan |
| `components/dashboard/status-card.tsx` | Orphan |
| `lib/use-live-learning.ts` | Orphan |
| `lib/live-sse-bus.ts` | Orphan |
| `lib/runtime-manager.ts` | Orphan |
| `lib/sse-registry.ts` | Orphan |
| Unused APIs: console, status, git, connectors, … | Zero consumers |
| `ecc/` residual (after confirming Vercel config) | Legacy |

## 12.5 REFACTOR (later)

1. Remount or remove Inspector cleanly.  
2. `LearningDataProvider` at Shell.  
3. Route groups `(executive)` / `(internal)`.  
4. Token-only styling on missions/review/reports.  
5. Collapse obsolete runtime API surface behind 410 Gone with message.  
6. Add `not-found.tsx` + error boundary.  

## 12.6 Suggested cleanup PR order

1. **Docs only** (this audit) — current commit  
2. **Safe deletes** of proven orphans (live-dashboard stack, progress-bar)  
3. **Inspector fix** (provider or strip)  
4. **API deprecation** (runtime/*, unused GET APIs)  
5. **Style convergence** (missions/review to tokens)  
6. **Poll consolidation**  

---

# 13. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Deleting “unused” API still hit by external tools | Med | Med | 410 + changelog before hard delete |
| Inspector fix breaks internal workflows | Low | Med | Fix provider first |
| Aggressive style rewrite | Med | Low | Token migration page-by-page |
| Confusing live_runtime vs GHA | High | Med | Docs + remove UI remnants |
| Vercel RO FS for review/publish | High | High | Already documented; keep GHA write path |
| Double poll races | Med | Low | Provider consolidation |

**Overall risk of current state:** Medium — product path works; technical debt is mostly **dead surface area** and **style/IA inconsistency**, not core pipeline failure.

---

# 14. Complexity Report

| Area | Complexity | Trend |
|------|------------|-------|
| Python learning architecture | High | Stable (frozen) |
| ECC executive surface | Medium | Improving |
| ECC legacy surface | High | Should shrink |
| State files (journal, sessions, feed, publish_state, runtime) | High | Needs single map |
| Config surfaces (learning.yaml, policies, environments) | Medium | OK |
| Theming | Medium | Dual systems |

**Hotspots for accidental complexity:**

1. Learning execution: local oneshot + GHA + progressive publish + review  
2. Multiple queue directories: pending / approved / rejected / publish  
3. Parallel “publish” UIs: review approve, publisher page, progressive auto  

---

# 15. Reference architecture (post-audit)

## 15.1 Product surface (canonical)

```text
Dashboard → Knowledge → Missions → Review → Reports → Settings
     │                      │          │
     │                      │          └─ /api/review
     │                      └─ /api/learning, /api/missions
     └─ /api/sessions, /api/live/start, /api/publish-queue, /api/journal
```

## 15.2 Knowledge write path (canonical)

```text
Learning session (GHA/local)
  → candidates in automation/queue/pending
  → [dev] publish queue + progressive publish
  → [prod] human review → approved → publish
  → domains/**/*.csv
  → knowledge_feed.jsonl + learning_journal.jsonl + sessions/
```

## 15.3 What is NOT canonical anymore

- Local long-lived Python spawned by Next.js (`runtime-manager` start path)  
- Dashboard-as-runtime host  
- SSE journal tail as primary UX  
- Engineering modules in primary nav  

---

# 16. Deliverables checklist

| Deliverable | Location |
|-------------|----------|
| Repository Architecture Report | §1 |
| Route Map | §2 |
| Component Map | §4 |
| API Map | §3 |
| Dependency Map / Graphs | §10 |
| Design System Audit | §5 |
| Technical Debt Report | §11 |
| Cleanup Plan | §12 |
| Risk Assessment | §13 |
| Complexity Report | §14 |
| Functional Audit | §9 |
| Import Audit | §6 |
| Folder Audit | §7 |

---

# 17. Rules for next sprints

1. **No new features** until cleanup PR series is scheduled.  
2. **No silent deletes** — use KEEP/MERGE/REMOVE lists above.  
3. **Respect frozen architecture** — only execution and presentation cleanup.  
4. Prefer **deleting dead ECC surface** over adding wrappers.  
5. Any UI work must use **CSS variables**, not new ad-hoc zinc palettes.  

---

*End of audit. Implementation of cleanup requires a separate, explicit sprint.*
