# Deploy IDA ECC to Vercel

## Purpose

Ship the Executive Control Center as a Vercel web app while keeping the monorepo knowledge assets readable.

## Status: Active

## Recommended project settings

Import the GitHub repo: `ImHeroesKiller/ida-dataset`

| Setting | Value |
| --- | --- |
| Framework Preset | Next.js |
| **Root Directory** | `ecc` |
| Build Command | `npm run build` (default) |
| Install Command | `npm install` (default) |
| Output Directory | default (`.next`) |
| Node.js Version | 20.x or 22.x |

> Prefer **Root Directory = `ecc`**. The Next.js config includes monorepo knowledge files via `outputFileTracingRoot` + `outputFileTracingIncludes`.

### Alternative (repo root)

If Root Directory is left empty (repo root), root `vercel.json` provides:

- `installCommand`: `cd ecc && npm install`
- `buildCommand`: `cd ecc && npm run build`
- `outputDirectory`: `ecc/.next`

## Environment variables (optional)

| Name | Purpose |
| --- | --- |
| `IDA_REPO_ROOT` | Absolute path override (usually unnecessary on Vercel) |
| `ECC_DISABLE_PYTHON` | Force-skip Python orchestration (`1`) |
| `ECC_ENABLE_GIT` | Attempt local git exec (not recommended on Vercel) |

Vercel automatically provides:

- `VERCEL=1`
- `VERCEL_GIT_COMMIT_SHA`
- `VERCEL_GIT_COMMIT_REF`
- `VERCEL_GIT_COMMIT_MESSAGE`

ECC uses these for Git status cards when `.git` is unavailable.

## What works on Vercel

- Dashboard status cards from live CSV/YAML inventory
- Ontology browser
- Dataset read-only browser
- Policy viewer
- Review queue viewer
- Report browser (if report files exist in the deploy)
- Global search
- Console / progress UI

## What is limited on Vercel

| Feature | Behavior |
| --- | --- |
| Python CI orchestration | Skipped; run via GitHub Actions |
| Live publish | Still blocked in UI; use `publish.yml` |
| Local git porcelain | Replaced by Vercel commit metadata |

Control flow remains:

```text
Planner → Policy → Pipeline → Review → Publisher
```

## CLI deploy (optional)

```bash
# from repo root, with Vercel CLI logged in
npx vercel link
# set Root Directory to ecc in the dashboard, or:
cd ecc && npx vercel --prod
```

## Production checklist

1. Push `main` to GitHub  
2. Import project in Vercel → Root Directory `ecc`  
3. Deploy production  
4. Open `/` and confirm ontology + datasets load  
5. Keep acquisition jobs on GitHub Actions (validate/planner/review/publish)  

## Regions

Default sample region in config: `sin1` (Singapore). Change in the Vercel project settings if needed.
