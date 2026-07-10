# Deploy IDA ECC to Vercel

## Purpose

Ship the Executive Control Center as a Vercel web app. Learning execution lives on **GitHub Actions**, not on Vercel.

## Status: Active

**Production:** https://ida-brain-monitor-eight.vercel.app  
**Project:** `ida-brain-monitor` (repo `ImHeroesKiller/ida-dataset`)

## Project settings (required)

Import GitHub repo: `ImHeroesKiller/ida-dataset`

| Setting | Value |
| --- | --- |
| Framework Preset | **Next.js** |
| **Root Directory** | **empty** (repository root) |
| Build Command | `npm run build` (default) |
| Install Command | `npm install` (default) |
| **Output Directory** | **leave empty / auto** (do **not** set `ecc/.next`) |
| Node.js Version | 20.x or 22.x |
| Region | `sin1` (see `vercel.json`) |

### Why Output Directory must be empty

Next.js on Vercel uses the framework builder, which publishes `.next/static/chunks`
and serverless functions automatically. A custom Output Directory
(`ecc/.next` leftover from the monorepo layout) can mis-align HTML build IDs
with uploaded chunks and surface as intermittent `ChunkLoadError` / 404.

`next.config.ts` uses the default `distDir` (`.next`).

### Ignored Build Step (critical)

`vercel.json` → `ignoreCommand`: `bash scripts/vercel-ignore-build.sh`

Learning sessions commit under `automation/sessions/**` frequently. Without
skipping those deploys, every session push redeploys production, rotates
chunk hashes, and breaks open browser tabs.

The ignore script **skips** deploys when only knowledge/session artifacts change
and **builds** when app/config/source files change.

## Environment variables (**required for Start Learning on Vercel**)

| Name | Purpose |
| --- | --- |
| `IDA_GITHUB_TOKEN` | PAT with `actions:write` + `actions:read` — Start Learning + run status |
| `GITHUB_REPOSITORY` | `owner/repo` (optional if `VERCEL_GIT_REPO_*` present) |
| `IDA_LEARNING_MODE` | Optional. On Vercel defaults to **production** (no auto-publish FS writes) |

Without the token:

- Dashboard still **reads committed sessions** from the deployment  
- **Start Learning** returns `422 GITHUB_NOT_CONFIGURED` (not a silent 503)  
- Local `npm run dev` falls back to one-shot `learning_session.py`  

Create a fine-grained or classic PAT → Vercel → Project → Settings → Environment Variables → Production (+ Preview if needed) → Redeploy.

## Deployment integrity controls

| Control | Implementation |
| --- | --- |
| Build ID | `generateBuildId` → `VERCEL_GIT_COMMIT_SHA` (12 chars) |
| Document cache | `Cache-Control: private, no-cache, no-store` via `next.config.ts` headers |
| Static chunks | `public, max-age=31536000, immutable` (Vercel + config) |
| basePath / assetPrefix | empty / unset |
| trailingSlash | `false` |
| ChunkLoadError recovery | `components/chunk-error-recovery.tsx` — one automatic reload |
| File tracing | `outputFileTracingIncludes` for knowledge assets |
| Publish queue GET | read-only safe on Vercel (no `publish_state.json` writes) |

See [audit/deployment_integrity_report.md](./audit/deployment_integrity_report.md).

## What works on Vercel

- Full Learning Sessions dashboard (file-based sessions)  
- Learning history, replay, knowledge KPIs  
- Ontology, datasets, policies, review, reports, search  
- Git metadata from `VERCEL_GIT_*`  
- **Start Learning** when `IDA_GITHUB_TOKEN` is set  

## What does not run on Vercel

| Feature | Where it runs |
| --- | --- |
| Continuous learning sessions | GitHub Actions `learning.yml` |
| Progressive publish writes | Local / GHA (read-only FS on Vercel) |
| Review / publish jobs | GitHub Actions |
| Local Python spawn | Removed |

## Local

```bash
npm install
npm run dev
```

Open http://localhost:3000

Simulate a session without GHA:

```bash
python automation/ci/learning_session.py --environment development --dry-run
```
