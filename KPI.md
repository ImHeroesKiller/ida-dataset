# Factory KPIs — IDA Dataset Factory

Official metrics for product success.  
A sprint is **DONE** only if it improves at least one KPI family.

**Critical rule:** Product KPIs measure long-term factory growth.  
**Never** use sprint milestones as product coverage denominators.

---

## Product targets vs sprint milestones

| Concept | Purpose | Example |
|---------|---------|---------|
| **Product target** | Long-term ambition for each dataset class | Industry = **250** |
| **Sprint milestone** | Near-term delivery checkpoint (informational only) | Phase-1 industry = 50 |

Coverage is always:

```text
Coverage = current_rows / product_target
Example: Industry 50 / 250 → 20%
Never:   Industry 50 / 50  → 100%
```

### Configurable registry

Product targets live in:

```text
automation/config/product_targets.yaml
```

Loaded by `lib/product-targets.ts`. Edit the YAML to recalibrate ambition — **do not hardcode** targets in UI or KPI code.

Default product targets (see YAML for authority):

| Dataset class | Product target |
|---------------|----------------|
| Industry | 250 |
| Company | 10_000 |
| Product | 5_000 |
| Service | 2_000 |
| Pain Point | 3_000 |
| Solution | 3_000 |
| Framework | 500 |
| Regulation | 1_000 |
| Case Study | 1_000 |
| Buyer Persona | 500 |
| Decision Maker | 500 |

Sprint milestones under `sprint_milestones:` are **informational only**.

---

## KPI families

| Family | Question answered |
|--------|-------------------|
| **Coverage** | How much verified knowledge do we have vs product target? |
| **Quality / Readiness** | How good and complete is the knowledge? |
| **Freshness** | How current is the knowledge? |
| **Automation** | How reliably does the factory run itself? |
| **Export** | How ready is data for LLM training? |
| **Capacity** | How fast can we produce rows? (informational) |

---

## Official dashboard KPIs

Display **only** these factory metrics on the main dashboard:

| KPI | Definition | Source of truth |
|-----|------------|-----------------|
| **Factory Status** | idle / running / error | `live_activity.json` |
| **Current Mission** | Active mission title or id | activity / missions |
| **Current Activity** | Current pipeline task | activity |
| **Rows Added Today** | knowledge_added + knowledge_updated | `daily_*.json` |
| **Rows Added This Week** | Rolling 7-day sum | daily_*.json |
| **Rows Added This Month** | Rolling 30-day sum | daily_*.json |
| **Dataset Coverage** | `current / product_target` (primary: industry) | product_targets.yaml + CSV |
| **Dataset Readiness** | Composite 0–100 (see below) | `lib/factory-kpis.ts` |
| **Average Confidence** | Mean confidence on scored rows | Notes / Data Sources |
| **Duplicate Rate** | Fraction of duplicate entity IDs | CSV analysis |
| **Freshness** | % rows within product freshness window | Last Updated + config |
| **Mission Success Rate** | Successful/active ÷ total missions | `automation/missions/missions/` |
| **Exports Generated** | Count of artifacts under `exports/**` | filesystem |

Nothing more on the official Factory KPI strip.

---

## Dataset Readiness (0–100)

Displayed beside every dataset. Components:

| Input | Weight |
|-------|--------|
| Coverage % (product target) | 25% |
| Schema completeness | 25% |
| Average confidence (0–100 scale) | 20% |
| Inverse duplicate rate | 15% |
| Freshness % | 15% |

```text
readiness =
  coverage_pct * 0.25
  + schema_completeness * 0.25
  + confidence_pct * 0.2
  + (100 - dup_rate_pct) * 0.15
  + freshness_pct * 0.15
```

Implemented in `computeReadiness()` (`lib/factory-kpis.ts`). Formula changes require a KPI changelog note — not an architecture project.

Empty datasets score **0** readiness.

---

## Factory capacity (informational only)

Not product targets. Shown in a separate capacity panel:

| Metric | Definition |
|--------|------------|
| **Average Rows Per Day** | Month production ÷ lookback days |
| **Average Rows Per Session** | Month production ÷ session count |
| **Mission Throughput** | Missions per week (approx) |
| **Estimated Completion** | ETA to industry product target at current avg/day |

Lookback windows are configurable under `capacity:` in `product_targets.yaml`.

---

## Quality metric details

### Duplicate Rate
- **Exact:** same Industry ID / Company ID  
- **Fuzzy:** normalized name collision (future)  
- Target: ≤2% (90 days), ≤1% (12 months) on new batches  

### Freshness
- Window from `freshness_window_days` (default 90)  
- Target: ≥80% of active library rows within window by M2  

### Completeness
- Per-row: filled_fields / schema_fields  
- Library average reported as Schema Completeness %  

### Confidence
- Extractor/validator score 0–1, calibrated with source trust  
- Target: ≥0.85 new rows (30d), ≥0.88 (12m)  

### Coverage
- **Always product-target based:** `rows / product_target`  
- Sprint milestones never appear in the denominator  

---

## Sprint DoD checklist

- [ ] Named KPI(s) improved (before/after numbers)  
- [ ] Coverage still uses product targets (not sprint)  
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
- Sprint milestone % as a product success metric  
