# API Audit

**Generated:** 2026-07-10T16:19:42.965420+00:00

## Live endpoints (verified)

| Method | Path | Role |
|--------|------|------|
| GET | /api/sessions | Session monitor + GHA status |
| GET | /api/sessions?session_id= | Session events / replay |
| GET | /api/factory/status | KPIs + executive view |
| POST | /api/run | Dispatch learn/validate/quality/publish/export |
| GET/POST | /api/missions | List + create directed missions |
| GET | /api/search | Topbar knowledge search |
| GET | /api/datasets | Dataset list/preview |
| GET | /api/sources | Source health |
| GET/POST | /api/publish-queue | Queue + journal tail |
| GET | /api/journal | Learning journal KPI tail |

## Fixed this sprint

| Issue | Resolution |
|-------|------------|
| `POST /api/learning` (404) | Missions client → `POST /api/missions` |
| `GET /api/search` (404) | Implemented lightweight search over datasets/missions/sessions/sources |
| Topbar legacy href rewrites | Removed /knowledge /review rewrites; use factory routes |

## Deprecated registry

`lib/api/deprecated.ts` lists sunset paths including `/api/learning` and `/api/network`.

## Dead clients

No remaining production fetches to missing endpoints.
