# UI Consistency Audit

**Product:** IDA Dataset Factory v2.0  
**Sprint:** Production UI Sprint  
**Date:** 2026-07-11  

---

## Design system sources of truth

| Layer | Path | Role |
|-------|------|------|
| JS tokens | `lib/design-tokens.ts` | Colors, type scale, spacing, radii, badge roles |
| CSS variables | `styles/globals.css` | Runtime theme (light + `.dark`) |
| Buttons | `components/ui/button.tsx` | Primary / secondary / outline / danger / ghost / loading |
| Cards | `components/ui/card.tsx` | Border, shadow, radius-xl, 24px padding |
| Badges | `components/ui/badge.tsx` | RoleBadge + StatusBadge |
| Inputs | `components/ui/input.tsx` | Token borders / focus |
| Progress | `components/ui/progress.tsx` | Token track/fill |
| Status map | `lib/status.ts` | Module status → badge colors |

**Rule:** No new hardcoded colors in app UI. Use `var(--*)` or token imports.

---

## Typography scale (enforced)

| Role | Size | Weight | Utility |
|------|------|--------|---------|
| Page title | 36 | 700 | `.text-page-title` |
| Section title | 24 | 700 | `.text-section-title` |
| Card title | 18 | 600 | `.text-card-title` |
| Body | 16 | 400 | `.text-body` |
| Small | 14 | 400 | `.text-small` |
| Caption | 12 | 500 | `.text-caption` |

---

## Spacing grid (8px)

| Token | px | Use |
|-------|-----|-----|
| `--space-1` | 8 | Tight gaps |
| `--space-2` | 16 | Input vertical rhythm, nav |
| `--space-3` | 24 | Card padding, card gaps |
| `--space-4` | 32 | Section spacing |

---

## Page audit

| Route | Hierarchy | Tokens | Cards | Tables/Lists | Empty states | Notes |
|-------|-----------|--------|-------|--------------|--------------|-------|
| `/` Dashboard | Strong KPI stack | Yes | Yes | Feed lists | Yes | CEO priority surface |
| `/datasets` | Catalog | Yes | Catalog cards | Progress bars | Search empty | Product catalog |
| `/missions` | Dispatch first | Yes | Yes | History | Suggested chips | Large input |
| `/sources` | Ops monitoring | Yes |/table rows | Metrics | — | Health + yield |
| `/logs` | Grouped console | Yes | Yes | Expandable groups | Empty group copy | 8 stage groups |
| `/quality` | Indicators | Yes | Yes | Metrics | — | Visual health |
| `/exports` | Jobs + last | Yes | Yes | Status | Explains *why* empty | No blank boxes |
| `/settings` | Sectioned | Yes | Section cards | Forms | — | 11 sections |
| Shell / sidebar | Nav + status | Yes | Quick status | — | — | No empty dark rect |
| Inspector | Detail | Yes | Meta blocks | — | Select prompt | Tokenized |

---

## Removed anti-patterns

| Anti-pattern | Resolution |
|--------------|------------|
| Tiny unreadable gray text | Muted raised to AA; captions 12/500 |
| Invisible borders | `--border` on all cards |
| Flat cards | Shadow + radius-xl |
| Black placeholder rectangles | Sidebar Quick Status; exports empty *why* |
| Mixed typography | Global type utilities |
| Mixed spacing | 8px grid variables |
| Inconsistent icons | Lucide at consistent 16–20px in nav |
| Hardcoded zinc / hex in components | Grep-clean for `zinc-*` in app TSX |

---

## Freeze compliance

| Constraint | Met |
|------------|-----|
| No workflow redesign | Yes |
| No route changes | Yes |
| No API changes | Yes |
| No backend / scheduler / manufacturing engine changes | Yes |
| UI refactor only | Yes |

---

## Residual follow-ups (out of sprint)

1. Wire automated contrast / axe in CI.  
2. Chart library palette pass if charts expand.  
3. Optional Storybook for Button / Badge / Card.  
