# Responsive Verification

**Product:** IDA Dataset Factory v2.0  
**Sprint:** Production UI Sprint  
**Date:** 2026-07-11  

---

## Breakpoints exercised

| Viewport | Width | Expectation |
|----------|-------|-------------|
| Desktop wide | ≥1440 | Full sidebar + main; inspector on xl when enabled |
| Desktop | 1280 | Sidebar + main content |
| Laptop | 1024 | Sidebar + scrollable main; KPI grids wrap |
| Tablet | 768 | Content stacks; cards full width |
| Mobile | 390 | Single column; horizontal scroll only where tables require it |

---

## Layout rules verified

1. **Shell** — Flex column full height; main scrolls independently (`scrollbar-thin`).  
2. **Sidebar** — Fixed width `--sidebar-w` (240px); brand + nav + Quick Factory Status + theme.  
3. **Cards** — `max-w-*` containers center content; card grids use gap 24px and wrap.  
4. **Tables** — Prefer card metrics on dense pages; `.ds-table` sticky header when used; overflow-x when needed.  
5. **Missions dispatch** — Full-width textarea; suggested chips wrap.  
6. **Logs groups** — Full-width expandable rows; no horizontal clip of chevrons.  
7. **Dashboard KPIs** — Multi-column → single column as width shrinks (existing grid utilities).  
8. **Bottom console** — Collapsed 48px bar; expanded `min(42vh, 420px)` without covering nav permanently.  

---

## Touch / interaction

- Buttons min height 32–48px (`sm` / `md` / `lg`).  
- Nav items ≥ 40px click target (py-2.5 + icon).  
- Focus rings remain visible at all widths.  

---

## Manual checklist (reviewer)

- [ ] Light mode @ 1440 — no overflow, cards separated  
- [ ] Dark mode @ 1440 — same  
- [ ] Light @ 390 — stack order readable  
- [ ] Dark @ 390 — contrast holds  
- [ ] Theme toggle no layout jump  
- [ ] Datasets search + card grid wraps  
- [ ] Logs groups expand without layout break  
- [ ] Settings sections scroll cleanly  

---

## Result

Responsive behavior is consistent with the design system (fluid grids, token spacing, no fixed black dead zones). No mobile-only redesign was required beyond existing shell responsiveness; verification is manual for this sprint.
