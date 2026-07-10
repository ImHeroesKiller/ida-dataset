# Deploy IDA ECC to Vercel

## Purpose

Ship the Executive Control Center as a Vercel web app. Learning execution lives on **GitHub Actions**, not on Vercel.

## Status: Active

## Project settings (required)

Import GitHub repo: `ImHeroesKiller/ida-dataset`

| Setting | Value |
| --- | --- |
| Framework Preset | **Next.js** |
| **Root Directory** | **empty** (repository root) |
| Build Command | `npm run build` (default) |
| Install Command | `npm install` (default) |
| **Output Directory** | **`ecc/.next`** (matches `next.config.ts` → `distDir`) |
| Node.js Version | 20.x or 22.x |

## Environment variables (recommended)

| Name | Purpose |
| --- | --- |
| `IDA_GITHUB_TOKEN` | PAT with `actions:write` + `actions:read` — Start Learning + run status |
| `GITHUB_REPOSITORY` | `owner/repo` (optional if `VERCEL_GIT_REPO_*` present) |

Without the token, the dashboard still **reads committed sessions** from the deployment filesystem; only workflow dispatch and live Actions status are disabled.

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
