# Code Cleanup

**Generated:** 2026-07-11  
**Sprint:** IDA Dataset Factory Simplification v2.0

## Approach

1. Audit first (`unused_modules.md`, `unused_env.md`).  
2. Remove only **100% unused** non-production surface.  
3. Never remove CI entrypoints, connectors, pipeline stages, or frozen packages.

## Actions this sprint

| Action | Detail |
|--------|--------|
| Config disable | Paid secondary discovery providers `enabled: false` |
| Logic simplify | Discovery layer no longer multiplies queries × all paid APIs |
| Cap enforcement | Max 10 live primary (Tavily) searches per session |
| UI redirect | Datasets / Quality / Logs pages → operator surfaces |
| Cadence align | GHA hourly + UI/settings/next-run hints |
| Dead re-export | Removed `lib/use-learning-sessions.ts` (zero importers; superseded by `hooks/learning-provider`) |
| Docs align | ARCHITECTURE UI list · Settings cadence |

## Not removed (still production or opt-in)

| Area | Why kept |
|------|----------|
| CI scripts under `automation/ci/*` | Invoked by GitHub Actions CLI |
| Secondary provider adapters | Operator opt-in without code restore |
| Fulltext acquisition framework | Active production path |
| Mission / queue / manufacturing engines | Frozen production core |
| `components/shared/datasets-client.tsx` | Orphaned by redirect but retained for possible Export dataset browser; referenced by repo-health |
| `lib/api/deprecated.ts` | Required by repo-health + deprecation contract |

## Safety rule

If a module has zero static imports but is invoked via `python -m`, GHA step, or health check — **keep**.
