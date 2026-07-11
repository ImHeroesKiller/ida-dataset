# Before / After Screenshot Summary

**Product:** IDA Dataset Factory v2.0  
**Sprint:** Production UI Sprint  
**Date:** 2026-07-11  

Screenshots are not committed (binary noise). Use this checklist to capture before/after pairs in local review or design QA.

---

## How to capture

1. Run the app (`npm run dev`).  
2. Toggle light and dark theme.  
3. Capture full viewport at **1440×900** and **390×844** (mobile).  
4. Store privately under `reports/ui-sprint/` if needed (gitignored preferred).

---

## Surface-by-surface summary

| Surface | Before (problems) | After (improvements) |
|---------|-------------------|----------------------|
| **Global shell** | Mixed zinc hardcodes, weak borders, inconsistent type | Token-driven `--bg` / `--panel` / `--border`; Inter + type scale |
| **Sidebar** | Empty dark rectangle placeholder; weak active state | Quick Factory Status card; active bar + hover; AA labels |
| **Topbar** | Flat, low hierarchy | Clear page title slot, token colors |
| **Dashboard (CEO)** | Harder to scan KPIs; mixed grays | Strong hierarchy; KPI cards with shadow + border; stage indicators use tokens |
| **Datasets** | CSV explorer feel | Product catalog: Name, Rows, Coverage, Target, Gap, Readiness, Progress, Health, Last updated, Sources/Missions |
| **Missions** | Small dispatch input | Large textarea, helpful placeholder, suggested mission chips, clearer history |
| **Sources** | Sparse operational fields | Health, Coverage, Rows, Documents, Yield, Latency, Success, Last Sync, Connector, Mission usage |
| **Logs** | Flat stream | Collapsible groups: Mission, Discovery, Download, Extraction, Validation, Publish, Git, Reports |
| **Quality** | Minimal indicators | Confidence / progress / freshness / duplicate / schema / validation visual indicators |
| **Exports** | Empty placeholders | Last export, rows, generated, target, status, format, pending jobs; empty-state *why* copy |
| **Settings** | Too minimal | Sections: Factory, Production, Scheduler, Discovery, Sources, Validation, Publishing, LLM, Export, Diagnostics, Observability |
| **Inspector** | Black zinc panel | Token surfaces matching product chrome |
| **Bottom console** | Status dot zinc | Token green / disabled |
| **Buttons / badges** | Inconsistent | Primary / outline / danger / ghost; RoleBadge set |

---

## Visual goals achieved

- Cards separate from page background (`rounded-xl`, shadow, border, 24px padding).  
- 8px spacing grid (`--space-1` … `--space-4`).  
- No oversized pure-black dead zones.  
- One product language vs mixed admin template parts.  

---

## Comparable products (target feel)

GitHub Enterprise · Linear · Vercel · Datadog · Grafana Cloud · Stripe Dashboard · OpenAI Platform
