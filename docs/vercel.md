# Deploy IDA ECC to Vercel

## Purpose

Ship the Executive Control Center as a Vercel web app.

## Status: Active

## Project settings (required)

Import GitHub repo: `ImHeroesKiller/ida-dataset`

| Setting | Value |
| --- | --- |
| Framework Preset | **Next.js** |
| **Root Directory** | **empty** (repository root) — do **not** set to `ecc` |
| Build Command | `npm run build` (default) |
| Install Command | `npm install` (default) |
| **Output Directory** | **`ecc/.next`** (matches `next.config.ts` → `distDir`) |
| Node.js Version | 20.x or 22.x |

> If build fails with `ecc/.next was not found`, either keep Output Directory = `ecc/.next`
> (repo default) **or** clear Output Directory and change `distDir` back to `.next`.

### If you previously set Root Directory to `ecc`

1. Vercel → Project → **Settings → General → Root Directory**  
2. Clear it / set to `.` / leave empty  
3. Framework → **Next.js**  
4. Save → **Redeploy**

### Why 404 NOT_FOUND happened

Deployment finished with `framework: null` (no Next.js runtime).  
That produces a READY deployment with no routes → `404: NOT_FOUND`.

Cause: app lived under `ecc/` while Root Directory was not configured, so Vercel never attached the Next.js builder.

**Fix applied in repo:** ECC app now lives at the repository root (`app/`, `package.json`, `next.config.ts`).

## Domains

Production project example: `ida-brain-monitor-eight.vercel.app`  
After a successful redeploy, `/` should render the ECC dashboard (not NOT_FOUND).

## What works on Vercel

- Dashboard, ontology, datasets, policies, review, reports, search  
- Git metadata from `VERCEL_GIT_*` env vars  

## Limited on Vercel

| Feature | Behavior |
| --- | --- |
| Python CI orchestration | Skipped; use GitHub Actions |
| Live publish from UI | Blocked; use `publish.yml` |

## Local

```bash
npm install
npm run dev
```

Open http://localhost:3000
