# UI Simplification

**Generated:** 2026-07-11  
**Sprint:** IDA Dataset Factory Simplification v2.0

## Operator nav (kept)

| Route | Role |
|-------|------|
| `/` Dashboard | Mission · scheduler · learning · KPIs · graphs · live console |
| `/missions` Mission | Current · queue · history · create · pause/resume/stop/retry |
| `/sources` Sources | Preferred · Trusted · Random Discovery |
| `/exports` Export | GitHub · HF · JSONL · Parquet · CSV · OpenAI monitor |
| `/settings` Settings | Cadence · discovery · production knobs |

## Merged / redirected

| Old | Action |
|-----|--------|
| `/datasets` | redirect → `/exports` |
| `/quality` | redirect → `/` |
| `/logs` | redirect → `/` (bottom console) |

## Dashboard surface

Top cards: current mission, scheduler, learning status, today's rows, knowledge growth, current dataset/source/connector/stage/document/throughput/queue.

Graphs: knowledge growth, rows/hour, rows/day, dataset distribution, source distribution (existing executive metrics retained).

Bottom console filters: search · extraction · validation · publishing · **github** · **huggingface** · **export** · errors · warnings.

## Sources

Sections:

- **Preferred Sources** — mission usage / yield weighted  
- **Trusted Sources** — registry allowlist  
- **Random Discovery** — healthy pool  

Enable / disable / prioritize remains configuration-driven (`source_registry` / SOURCE_POLICY) per production freeze (no engine rewrite).

## Export monitor

Shows GitHub (append-only push path), Hugging Face status/version/rows, and artifact readiness for JSONL · Parquet · CSV · OpenAI.

## Freeze compliance

- No folder restructuring  
- No schema / queue / mission engine rewrite  
- Dashboard metrics surface retained; nav reduced to production operator paths  
- Old bookmarks preserved via redirects
