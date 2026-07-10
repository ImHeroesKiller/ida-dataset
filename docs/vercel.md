# Deploy IDA ECC to Vercel

## Purpose

Ship the Executive Control Center as a Vercel web app while keeping monorepo knowledge assets readable.

## Status: Active

## Critical setting (this fixes the build error)

In the Vercel project:

**Settings → General → Root Directory → `ecc` → Save**

Then **Redeploy**.

| Setting | Value |
| --- | --- |
| Framework Preset | Next.js |
| **Root Directory** | **`ecc`** |
| Build Command | `npm run build` (default) |
| Install Command | `npm install` (default) |
| Output Directory | *leave default* (do not set `ecc/.next` manually) |
| Node.js Version | 20.x or 22.x |

### Why this matters

`package.json` with the `next` dependency lives in `ecc/`, not the repo root.

If Root Directory is empty (repo root), Vercel looks for `next` in the root `package.json`, fails with:

```text
Error: No Next.js version detected
```

Do **not** use a root `installCommand` like `cd ecc && npm install` without Root Directory `ecc` — Vercel will still not detect Next.js correctly.

There is intentionally **no** root `vercel.json` build override for this reason. Config lives in `ecc/vercel.json`.

## Environment variables (optional)

| Name | Purpose |
| --- | --- |
| `IDA_REPO_ROOT` | Absolute path override (usually unnecessary on Vercel) |
| `ECC_DISABLE_PYTHON` | Force-skip Python orchestration (`1`) |
| `ECC_ENABLE_GIT` | Attempt local git exec (not recommended on Vercel) |

Vercel provides automatically:

- `VERCEL=1`
- `VERCEL_GIT_COMMIT_SHA`
- `VERCEL_GIT_COMMIT_REF`
- `VERCEL_GIT_COMMIT_MESSAGE`

## What works on Vercel

- Dashboard status from live CSV/YAML inventory
- Ontology browser
- Dataset read-only browser
- Policy viewer
- Review queue viewer
- Report browser
- Global search
- Console / progress UI

## What is limited on Vercel

| Feature | Behavior |
| --- | --- |
| Python CI orchestration | Skipped; use GitHub Actions |
| Live publish | Blocked in UI; use `publish.yml` |
| Local git porcelain | Replaced by Vercel commit metadata |

## CLI deploy

```bash
# from repo, after: npm i -g vercel && vercel login
cd ecc
npx vercel        # preview
npx vercel --prod # production
```

When linking, set the project Root Directory to `ecc` if prompted.

## Production checklist

1. Push `main` to GitHub  
2. Vercel → Project → Settings → Root Directory = **`ecc`**  
3. Deploy / Redeploy  
4. Open `/` and confirm ontology + datasets load  
5. Keep acquisition jobs on GitHub Actions  

## Regions

Sample region in `ecc/vercel.json`: `sin1` (Singapore). Change in the Vercel project settings if needed.
