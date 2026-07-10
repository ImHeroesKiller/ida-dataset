# Production Order — IDA Dataset Factory

**Status:** Official long-term manufacturing plan  
**Version:** 1.0  
**Mode:** Permanent production batches (not software feature sprints)  
**Architecture / Dashboard / Automation / KPI platform:** Frozen  

---

## 1. Product goal

The factory has **one responsibility**:

> Continuously produce high-quality structured datasets for future LLM training and fine-tuning.

Every batch must improve one or more of:

| Family | Meaning |
|--------|---------|
| **Coverage** | More verified rows toward product targets |
| **Quality** | Confidence, completeness, duplicates, validation |
| **Freshness** | Current retrieved / last-updated dates |
| **Automation** | Reliable mission execution |
| **Export readiness** | Training packages stay current |

Nothing else.

---

## 2. Permanent production sequence

Authoritative graph: [DATASET_DEPENDENCY_MATRIX.md](./DATASET_DEPENDENCY_MATRIX.md)  
Batch catalog: [PRODUCTION_BATCH_LIBRARY.md](./PRODUCTION_BATCH_LIBRARY.md)  
Operating procedure: [DATASET_PRODUCTION_STANDARD.md](./DATASET_PRODUCTION_STANDARD.md)

```text
Batch-001 Industry          ✅ baseline (continuous → product target)
Batch-002 Service           ← NEXT
Batch-003 Product
Batch-004 Company
Batch-005 Pain Point
Batch-006 Solution
Batch-007 Framework
Batch-008 Case Study
Batch-009 Buyer Persona
Batch-010 Decision Maker
Batch-011 Regulation        (may interleave after Industry)
Batch-012 Opportunity
Batch-013 Risk
Batch-014 Trend             (may interleave after Industry)
Batch-015 Competitor
Batch-016 Business Signal
Batch-017 Discovery Question
```

After this plan, **no further planning documents are required**.  
Future work = execute batches + raise verified coverage under DPS.

---

## 3. Production targets snapshot

### Method (no hardcoding in runtime)

| Input | Source |
|-------|--------|
| **Current rows** | Domain CSV row counts (`listDatasets` / factory KPIs) |
| **Target rows** | `automation/config/product_targets.yaml` via `lib/product-targets.ts` |
| **Coverage** | `current_rows / product_target` ([KPI.md](../KPI.md)) |
| **Estimated production time** | `(target − current) / average_rows_per_day` from factory capacity |
| **Priority** | Dependency matrix + batch library |
| **Readiness** | Factory dataset readiness score 0–100 where computed |

**Capacity baseline used for ETA (informational):**  
Average rows/day ≈ **2.1** (factory capacity lookback at plan time).  
Throughput will change as automation improves — recompute from live capacity; do not treat ETAs as SLAs.

### Master table (Business Development product classes)

Snapshot date: **2026-07-10**. Recompute before each batch kickoff.

| Dataset | Current | Target | Coverage | Remaining | Est. time @ 2.1 rows/day | Priority | Readiness | Batch |
|---------|--------:|-------:|---------:|----------:|--------------------------:|----------|----------:|-------|
| Industry | 50 | 250 | **20%** | 200 | ~95 days (~3 mo) | P0 continuous | ~77 (live KPI) | 001 |
| Service | 0* | 2_000 | **0%** | 2_000 | ~952 days | P0 next | 0 | 002 |
| Product | 20 | 5_000 | **0.4%** | 4_980 | ~2_371 days | P0 | low / seed | 003 |
| Company | 25 | 10_000 | **0.3%** | 9_975 | ~4_750 days | P0 | low / seed | 004 |
| Pain Point | 0 | 3_000 | **0%** | 3_000 | ~1_429 days | P0 | 0 | 005 |
| Solution | 0 | 3_000 | **0%** | 3_000 | ~1_429 days | P0 | 0 | 006 |
| Framework | 0 | 500 | **0%** | 500 | ~238 days | P1 | 0 | 007 |
| Case Study | 0 | 1_000 | **0%** | 1_000 | ~476 days | P1 | 0 | 008 |
| Buyer Persona | 0 | 500 | **0%** | 500 | ~238 days | P1 | 0 | 009 |
| Decision Maker | 0 | 500 | **0%** | 500 | ~238 days | P1 | 0 | 010 |
| Regulation | 0 | 1_000 | **0%** | 1_000 | ~476 days | P1 | 0 | 011 |
| Opportunity | 25 | 2_000 | **1.3%** | 1_975 | ~940 days | P1 | low / seed | 012 |
| Competitor | 0 | 1_000 | **0%** | 1_000 | ~476 days | P1 | 0 | 015 |
| Business Signal | 0 | 1_000 | **0%** | 1_000 | ~476 days | P2 | 0 | 016 |
| Discovery Question | 0 | 500 | **0%** | 500 | ~238 days | P2 | 0 | 017 |
| Risk | field-level | config later | — | — | continuous with Industry/Company | P2 | — | 013 |
| Trend | field-level | config later | — | — | continuous with Industry | P2 | — | 014 |

\* Service: no dedicated CSV yet — produce as verified `product_catalog` service-type rows counting toward `service_library` target until a dedicated store is schema-approved.

### Interpretation

- Long ETAs at current throughput are **expected** at 10k-scale targets.  
- Success is continuous coverage growth, not a single calendar deadline.  
- Raising `average_rows_per_day` (automation, sources, parallel missions) is the legitimate way to shrink ETAs — not relaxing DPS.

---

## 4. Current factory production focus

| Field | Value (plan time) |
|-------|-------------------|
| **Current production batch** | Batch-001 continuous + **Batch-002 planned next** |
| **Current dataset** | Industry (active growth) → Service (next primary) |
| **Coverage (primary)** | Industry 50 / 250 (**20%**) |
| **Rows produced (industry baseline)** | 50 verified |
| **Rows remaining (industry product target)** | 200 |
| **Estimated completion (industry)** | ~3–4 months at current capacity (live KPI may say ~4 months) |
| **Current mission theme** | Expand / Produce Industry Dataset until Batch-002 starts |
| **Current source** | Trusted registry (e.g. World Bank, BPS, OECD, OJK — live activity) |
| **Current activity** | Factory learn / idle as per `live_activity.json` |

---

## 5. Dashboard field map (no redesign)

**Do not redesign the dashboard.**  
The frozen Factory dashboard already (or via existing KPI/activity feeds) exposes manufacturing signals. Map production concepts to **existing** surfaces only — no new widgets, no engineering metrics, no AI metrics.

| Production concept | Existing surface |
|--------------------|------------------|
| Current Production Batch | Documented in this plan + mission title; show via **Current mission** text (e.g. `Batch-002 · Service`) when missions are named |
| Current Dataset | Coverage label / dataset readiness list / mission target |
| Coverage | **Dataset coverage** metric + `coverage_label` (product target denominator) |
| Rows Produced | **Rows added today / week / month** |
| Rows Remaining | Implicit: product target − current (industry target on KPI; full table in this doc) |
| Estimated Completion | **Factory capacity → Estimated completion** |
| Current Mission | **Current mission** metric |
| Current Source | Activity / sources feed (`current_source` in learning activity when running) |
| Current Activity | Header activity + **Factory status** hint |

No additional widgets. No architecture change.

---

## 6. Factory rules (every batch)

1. Follow **DPS v1.0**  
2. Use only **trusted sources**  
3. **Append-only** datasets  
4. **Validation** must pass  
5. **KPIs** must update  
6. **Exports** must update when in scope  
7. **Production report** required  

No exceptions.

---

## 7. Definition of manufacturing success

The factory now has:

1. ✅ Permanent production sequence  
2. ✅ Dependency matrix  
3. ✅ Production batch library  
4. ✅ Long-term manufacturing plan (this document)  

**Next work is execution only:** run Batch-002 (Service), then subsequent batches, increasing verified coverage under frozen architecture.

---

## 8. Document index

| Document | Role |
|----------|------|
| [DATASET_DEPENDENCY_MATRIX.md](./DATASET_DEPENDENCY_MATRIX.md) | Why datasets depend on each other |
| [PRODUCTION_BATCH_LIBRARY.md](./PRODUCTION_BATCH_LIBRARY.md) | Batch-001…017 catalog |
| [DATASET_PRODUCTION_STANDARD.md](./DATASET_PRODUCTION_STANDARD.md) | How to produce (DPS) |
| [KPI.md](../KPI.md) | How to measure |
| [MISSION_LIBRARY.md](../MISSION_LIBRARY.md) | Mission definitions |
| [BACKLOG.md](../BACKLOG.md) | Epic backlog (execution backlog only) |
| [ROADMAP.md](../ROADMAP.md) | Pointers to production mode |

---

**End of Production Order v1.0**
