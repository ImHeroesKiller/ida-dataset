# Final Route Map (post-consolidation)

## Public executive surface

| Path | Page | Feature |
|------|------|---------|
| `/` | `app/page.tsx` | `features/dashboard` |
| `/knowledge` | `app/knowledge/page.tsx` | `features/knowledge` |
| `/missions` | `app/missions/page.tsx` | `features/missions` |
| `/review` | `app/review/page.tsx` | `features/review` |
| `/reports` | `app/reports/page.tsx` | `features/reports` |
| `/settings` | `app/settings/page.tsx` | settings (inline) |

Nav source of truth: `lib/nav.ts`.

## Redirects

| Path | Destination |
|------|-------------|
| `/learning` | `/` |
| `/publisher` | `/review` |
| `/queue` | `/documents` |
| `/search` | `/network` |
| `/connectors` | (existing redirect) |
| `/connector-logs` | (existing redirect) |
| `/network-health` | (existing redirect) |

## Internal (operator, not in nav)

`/datasets` · `/documents` · `/network` · `/ontology` · `/planner` · `/policies` · `/sources` · `/system`
