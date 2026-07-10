# Release Plan — IDA Dataset Factory

**Product:** IDA Dataset Factory v2.0+  
**Cadence:** Continuous learning + staged product releases  
**Rule:** Each release must move ≥1 KPI (Coverage, Quality, Freshness, Automation, Export)

---

## Release principles

1. **Architecture frozen** — no redesign in a release  
2. **Append-only data** — never delete verified knowledge  
3. **Provenance required** on every published row  
4. **CI green** — validate · learn · quality · publish · export  
5. **Docs in sync** when behavior changes  

---

## Release trains

### Release R2.0 — Factory baseline (shipped)

| | |
|--|--|
| **Scope** | Repository reset, 8 factory surfaces, KPIs, export packager, charter docs |
| **KPI** | Export + Automation baseline |
| **Exit** | Build green; datasets intact; factory dashboard live |

### Release R2.1 — Trusted growth (next 30 days)

| | |
|--|--|
| **Scope** | BPS/WB/OJK collectors + health; industry expansion mission; hard QA gates; versioned JSONL/OpenAI |
| **Backlog** | E1-01/02/04/13/14 · E2-01 · E3-01/02/03/06 · E5-01/03/07 · E7-01/11 · E8-01/02/03/06 · E6-01–04 |
| **KPI targets** | Industries ≥8; healthy sources ≥6; conf ≥0.85; 0 placeholders |
| **Exit** | Quality CI fails on bad rows; export artifacts versioned |

### Release R2.2 — Multi-library scale (by ~90 days)

| | |
|--|--|
| **Scope** | Company/pain/solution/case/regulation/competitor growth; Parquet+HF; mission schedule/retry; full quality metrics |
| **Backlog** | E2-02/05/06/08/10/16 · E1 diversity · E3-04/05/07 · E4 suite · E5-02/04/08 · E7-02–04/08–10 · E8-04/05/08 |
| **KPI targets** | Industries ≥25; ≥3 libraries growing; mission success ≥85%; dup ≤2% |
| **Exit** | Scheduled missions running; multi-format exports |

### Release R2.3 — Training package maturity (by ~6 months)

| | |
|--|--|
| **Scope** | ShareGPT/Alpaca; buyer/KPI/risk/trend libraries; first non-BD domain rows; mission library complete |
| **Backlog** | E2-09–E2-15/17 · E5-05/06/10 · E7 full library · E4-07/09 |
| **KPI targets** | ≥10 dataset classes with rows; full export matrix; quality ≥80 under growth |
| **Exit** | Monthly versioned package process documented and repeatable |

### Release R2.4 — Factory maturity (by ~12 months)

| | |
|--|--|
| **Scope** | Multi-domain production; ≥90% mission success; monthly training packages as default ops |
| **KPI targets** | Industry catalog ≥80% target; conf ≥0.88; dup ≤1%; monthly package |
| **Exit** | Factory runs with minimal manual intervention |

---

## Release checklist (every train)

- [ ] KPI delta recorded (before/after)  
- [ ] `npm run build` green  
- [ ] `npm run health` / factory-health green  
- [ ] Domain CSVs append-only integrity  
- [ ] No new architecture surface  
- [ ] CHANGELOG entry  
- [ ] Export sample for affected datasets  

---

## Hotfix policy

Hotfixes may only:

- Restore broken learn/publish/export  
- Block bad data (QA)  
- Fix dashboard incorrect KPI reads  

Hotfixes must not add features outside the active release train.
