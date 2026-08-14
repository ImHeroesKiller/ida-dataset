# Accessibility Compliance Report

**Product:** IDA Dataset Factory v2.0  
**Sprint:** Production UI Sprint  
**Standard:** WCAG 2.1 Level AA  
**Date:** 2026-07-11  
**Scope:** UI only (no backend / API / workflow changes)

---

## Summary

The Production UI Sprint establishes a centralized design token system and refactors all primary surfaces so default text, interactive controls, badges, tables, and forms meet WCAG AA contrast targets in **light** and **dark** mode.

| Area | Status | Notes |
|------|--------|--------|
| Color contrast (body text) | Pass | Primary ≥4.5:1; muted tokens raised to AA-safe slate |
| Large text | Pass | Page/section titles use high-contrast primary text |
| Buttons | Pass | Solid primary/danger/success with white fg; outline/ghost use text tokens |
| Badges | Pass | Role badges use tinted bg + strong fg pairs |
| Forms / inputs | Pass | Border + focus ring; placeholder via muted (readable) |
| Tables | Pass | Sticky headers, secondary text (not faint gray) |
| Focus visibility | Pass | Global `:focus-visible` blue outline 2px |
| Dark mode | Pass | Dedicated dark palette; no pure black text on black |
| Light mode | Pass | Slate-50 bg, white surfaces, slate-900 text |

---

## Contrast targets

| Element | Minimum | Implementation |
|---------|---------|----------------|
| Body / small text | 4.5:1 | `--text` / `--text-secondary` / `--text-muted` |
| Large text (24px+ bold) | 3:1 | `.text-page-title`, `.text-section-title` on `--text` |
| UI components (icons, borders) | 3:1 | `--border` against `--bg` / `--panel` |
| Disabled text | Exempt (informational) | `--text-disabled` — not used as sole means of info |

### Light mode pairs (spec)

| Token | Value | Role |
|-------|-------|------|
| Background | `#F8FAFC` | Page |
| Surface | `#FFFFFF` | Cards |
| Primary text | `#0F172A` | Titles, body |
| Secondary text | `#334155` | Supporting |
| Muted text | `#64748B` | Labels (AA on white/surface) |
| Blue / Green / Orange / Red | Spec palette | Actions & status |

### Dark mode pairs (spec)

| Token | Value | Role |
|-------|-------|------|
| Background | `#020617` | Page |
| Card | `#0F172A` | Surfaces |
| Primary text | `#F8FAFC` | Titles, body |
| Secondary | `#CBD5E1` | Supporting |
| Muted | `#94A3B8` | Labels on dark surfaces |
| Semantic blues/greens/etc. | Spec palette | Actions & status |

**Removed:** Sub-4.5 “faint gray” used as primary copy. `--text-faint` now aliases the AA-safe muted token.

---

## Component checklist

### Buttons (`components/ui/button.tsx`)

- [x] Primary filled blue, white label  
- [x] Secondary / outline with visible border  
- [x] Danger red  
- [x] Ghost transparent  
- [x] Hover brightness / surface change  
- [x] Focus-visible outline  
- [x] Disabled opacity + `disabled` attribute  
- [x] Loading spinner + `aria-busy`

### Badges (`components/ui/badge.tsx`)

- [x] Healthy (green)  
- [x] Warning (orange)  
- [x] Error (red)  
- [x] Idle (gray)  
- [x] Running (blue)  
- [x] Publishing (purple)  
- [x] Completed (green)  
- [x] Light + dark token pairs for each role  

### Tables (`.ds-table` in `styles/globals.css`)

- [x] Sticky header  
- [x] Readable 14px body, 12px header labels  
- [x] Adequate cell padding  
- [x] Hover row highlight  
- [x] No tiny low-contrast gray as sole content  

### Forms

- [x] Input borders from `--border`  
- [x] Focus ring via design system  
- [x] 16px vertical spacing rhythm on settings / missions  

### Navigation

- [x] Active state + selected indicator bar  
- [x] Hover background  
- [x] `aria-label` on primary nav  

---

## Keyboard & structure

- Global `:focus-visible` ring on interactive elements  
- Semantic headings via typography utilities (`text-page-title`, etc.)  
- Collapsible log groups use button disclosure pattern  
- Theme toggle remains keyboard-accessible  

---

## Known residual risks (non-blocking)

1. **Third-party / legacy charts** — if any chart library uses its own palette, re-theme on next chart sprint.  
2. **Emoji / mono micro-labels** — some dashboards still use 10–11px mono for IDs; contrast is OK; size is secondary content.  
3. **Automated axe/Lighthouse CI** — not wired in this sprint; recommend adding as follow-up gate.  

---

## Verification method

1. Design tokens audited against sprint palette (`lib/design-tokens.ts`, `styles/globals.css`).  
2. Hardcoded `zinc-*` / raw hex UI colors removed from app components.  
3. TypeScript compile: `npx tsc --noEmit` clean.  
4. Manual pass of light/dark on Dashboard, Datasets, Missions, Sources, Logs, Quality, Exports, Settings.  

---

## Verdict

**WCAG AA contrast and control accessibility targets for the Production UI Sprint: met.**  
Automated a11y CI is recommended as a follow-up, not a blocker for this design-system land.
