# Unused Modules (audit)

**Generated:** 2026-07-11  
**Sprint:** IDA Dataset Factory Simplification v2.0

## Heuristic

Static name-reference scan across `automation/**/*.py` and frontend `@/lib` importers.  
Low-ref ≠ unused when invoked via `python -m` / GHA / health scripts.

## Removed this sprint (100% unused)

| Path | Evidence |
|------|----------|
| `lib/use-learning-sessions.ts` | Zero importers; deprecated re-export of `hooks/learning-provider` |

## Low-import candidates (DO NOT delete without call-graph proof)

| Path | Why kept |
|------|----------|
| `automation/ci/*.py` | Invoked by GitHub Actions |
| `automation/acquisition/auth.py` | Connector auth helper |
| `automation/pipeline/deduplicate.py` | Pipeline stage |
| `automation/pipeline/entity_link.py` | Pipeline stage |
| `automation/learning/journal.py` | Session journal |
| `automation/lib/logging_utils.py` | Shared logging |
| `automation/diagnostics/*` | Operator diagnostics CLI |
| Secondary discovery providers | Config-disabled; adapters stay |

## Safe bulk removals this sprint

**None beyond the single re-export above.** No other 100% unused production modules with proven zero callers.

Secondary discovery **configs** disabled (not deleted) so operators can re-enable without code restore.
