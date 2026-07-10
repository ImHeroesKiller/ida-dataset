# Factory KPIs — IDA Dataset Factory

Official metrics for product success.  
A sprint is **DONE** only if it improves at least one KPI family.

---

## KPI families

| Family | Question answered |
|--------|-------------------|
| **Coverage** | How much verified knowledge do we have? |
| **Quality** | How good is the knowledge? |
| **Freshness** | How current is the knowledge? |
| **Automation** | How reliably does the factory run itself? |
| **Export** | How ready is data for LLM training? |

---

## Official dashboard KPIs

| KPI | Definition | Source of truth |
|-----|------------|-----------------|
| **Rows Added Today** | Sum of knowledge_added + knowledge_updated (daily counters) | `automation/learning/state/daily_*.json` |
| **Rows Added This Week** | Rolling 7-day sum of daily counters | daily_*.json |
| **Rows Added This Month** | Rolling 30-day sum | daily_*.json |
| **Dataset Coverage** | Catalog progress and/or populated datasets ratio | datasets + industry catalog target |
| **Dataset Quality (score)** | Composite from completeness, confidence, verified sources, pending queue | `lib/factory-kpis.ts` |
| **Average Confidence** | Mean confidence of industry (or dataset) rows with scores | dataset Notes / Data Sources |
| **Duplicate Rate** | Fraction of near-duplicate entities in new batch / library | validator |
| **Schema Completeness** | % of schema fields non-empty (avg per row) | CSV vs metadata/schema |
| **Source Freshness** | % rows with Last Updated / retrieved within window (e.g. 90d) | dataset dates |
| **Mission Success Rate** | Successful/active missions ÷ total missions | `automation/missions/missions/` |
| **Exports Generated** | Count of artifacts under `exports/**` | filesystem |
| **Verified Sources / Active Sources** | Rows with trusted provenance; registry active+allowed | CSV + source_registry |

---

## Quality metric details

### Duplicate Rate
- **Exact:** same Industry ID / Company ID  
- **Fuzzy:** normalized name collision (future E3-03)  
- Target: ≤2% (90 days), ≤1% (12 months) on new batches  

### Freshness
- Windows: 30 days (hot), 90 days (standard)  
- Target: ≥80% of active library rows within 90 days by M2  

### Completeness
- Per-row: filled_fields / schema_fields  
- Library average reported as Schema Completeness %  

### Confidence
- Extractor/validator score 0–1, calibrated with source trust  
- Target: ≥0.85 new rows (30d), ≥0.88 (12m)  

### Source Diversity
- Distinct source_ids used in published rows  
- Target: ≥6 (30d), ≥12 (6m)  

### Coverage
- **Catalog coverage:** e.g. industries_count / target (25 → 50 → …)  
- **Dataset coverage:** populated datasets / total domain datasets  

---

## Composite Quality Score (current formula direction)

```text
quality ≈ completeness*0.35 + confidence*30 + verified_bonus + pending_clear_bonus + volume_bonus
```

Documented in code (`lib/factory-kpis.ts`). Changes to formula require a KPI changelog note—not an architecture project.

---

## Sprint DoD checklist

- [ ] Named KPI(s) improved (before/after numbers)  
- [ ] No architecture change  
- [ ] Provenance intact on new rows  
- [ ] Dashboard reflects real numbers  
- [ ] CI still green  

---

## Non-KPIs (do not optimize)

- Lines of code  
- Number of microservices  
- Model “intelligence”  
- Chat response quality  
- Decision accuracy (other product)  
