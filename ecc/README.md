# ECC location note

The Executive Control Center Next.js app was moved to the **repository root**
so Vercel auto-detects Next.js without a subdirectory Root Directory setting.

Build output uses the default **`.next`** directory (not `ecc/.next`).
Do **not** set Output Directory in Vercel project settings.

Run from repo root:

```bash
npm install
npm run dev
```

Deploy: import this repo on Vercel with **Root Directory empty** (repository root).

See [docs/vercel.md](../docs/vercel.md) and [docs/ecc.md](../docs/ecc.md).
