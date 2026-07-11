# Consistency Audit — Operator UI v1.0

## Shared components

| Component | Radius | Padding | Type |
|-----------|--------|---------|------|
| Card | `--radius-lg` (8px) | header `px-3 py-2.5`, body `px-3 py-3` | card title 12px |
| Button | `--radius-md` | sm `h-7`, md `h-8` | 11–12px |
| Badge / RoleBadge | full / md | compact | 10px |
| Input | `--radius-md` | `h-8` | 12px |
| Table `.ds-table` | — | th/td dense | 10–12px |
| Sidebar | 200px | nav `py-1.5` | 12px |
| Topbar | 44px | — | 12px |

## Page layout

All operator pages use:

- `.op-page` max-width + gap  
- `.op-page-header` + `.text-page-title`  
- Same card chrome  
- Bottom console for live events  

## Status colors

| Role | Use |
|------|-----|
| healthy / completed | green |
| running | blue |
| warning / waiting | amber |
| error | red |
| idle | slate |
| publishing | purple |

## Gaps closed this sprint

- Oversized page titles → 18px  
- Export card sprawl → channel strip + latest + queue  
- Mission diagnostics → current / queue / history / controls  
- Settings prose blocks → grouped parameter rows  
- Mixed status strings → operator language  
