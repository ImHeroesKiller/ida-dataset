# Executive Control Center (ECC)

## Purpose

Interactive operational cockpit for the IDA Knowledge Platform.

## Status: Active (Sprint 3)

## Location

The Next.js app lives at the **repository root**:

```text
app/           # App Router pages + API routes
components/    # UI shell, modules
lib/           # repo readers, orchestration, plugins
package.json
next.config.ts
```

Knowledge assets remain siblings: `domains/`, `metadata/`, `automation/`, `reports/`.

## Philosophy

```text
Dashboard → Planner → Policy Engine → Pipeline → Review → Publisher
```

Human-controlled. Not autonomous.

## Run

```bash
npm install
npm run dev
```

## Deploy

See [vercel.md](vercel.md). Root Directory must be the **repository root** (empty).
