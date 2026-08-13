# Dataset Production Standard (DPS)

**Status:** Official · Mandatory  
**Applies to:** Every dataset produced by IDA Dataset Factory v2.0  
**Version:** 1.0  
**Effective:** 2026-07-10  

---

## 1. Purpose

This document is the **permanent operating manual** for dataset production.

Every future production mission — Industry, Company, Product, Service, Pain Point, Solution, Framework, Regulation, Case Study, Buyer Persona, Decision Maker, and any dataset class added later — **must** follow this standard.

| Rule | Statement |
|------|-----------|
| Scope | Production procedure only |
| Platform | Architecture, dashboard, KPIs, and automation are **frozen** |
| Authority | If a mission conflicts with DPS, **DPS wins** |
| Change control | Amend this document with a versioned docs change — not ad-hoc mission shortcuts |

Related policies (do not replace DPS):

| Document | Role |
|----------|------|
| [ARCHITECTURE.md](../ARCHITECTURE.md) | Frozen pipeline topology |
| [SOURCE_POLICY.md](../SOURCE_POLICY.md) | Trusted source registry rules |
| [QUALITY_POLICY.md](../QUALITY_POLICY.md) | Provenance & quality checks |
| [DATASET_SCHEMA.md](../DATASET_SCHEMA.md) | Schema locations & freeze rules |
| [KPI.md](../KPI.md) | Product KPIs vs sprint milestones |
| [EXPORT_GUIDE.md](../EXPORT_GUIDE.md) | Export format packaging |
| [MISSION_LIBRARY.md](../MISSION_LIBRARY.md) | Production mission catalog |

---

## 2. Dataset Lifecycle

Every production mission follows this pipeline **in order**. No stage may be skipped for “speed.”

```text
Mission
  ↓
Source Discovery
  ↓
Document Collection
  ↓
Extraction
  ↓
Normalization
  ↓
Validation
  ↓
Schema Mapping
  ↓
Append Dataset
  ↓
Quality Validation
  ↓
Export
  ↓
Release
```

### 2.1 Stage definitions

| Stage | What happens | Done when |
|-------|--------------|-----------|
| **Mission** | Select target dataset class, coverage goal, priority, and acceptance KPIs | Mission id + target dataset recorded |
| **Source Discovery** | Resolve allowed sources from registry / policy | Only active, allowed, trusted sources selected |
| **Document Collection** | Acquire documents / official statistics / publications | Artifacts stored with provenance metadata |
| **Extraction** | Extract candidate entities and attributes | Candidate rows with source pointers exist |
| **Normalization** | Apply naming, ID, unit, and language rules | Canonical fields ready for schema |
| **Validation** | Confidence, schema fields, duplicates, forbidden sources | Pass / reject decision per row |
| **Schema Mapping** | Map to frozen dataset columns | Row matches target schema headers |
| **Append Dataset** | Append-only write to domain CSV | New rows present; history not rewritten |
| **Quality Validation** | Post-append checks (completeness, dups, freshness, confidence) | Quality gates pass for the batch |
| **Export** | Package for training / corpus formats | Export artifacts updated as required |
| **Release** | Versioned release note for dataset expansion | Release tag / version recorded |

### 2.2 Non-negotiables

1. **Observe schemas** — do not change column headers without a versioned migration.  
2. **Append only** — never delete verified knowledge to “fix” production.  
3. **Provenance on every row** — no anonymous knowledge.  
4. **Trusted sources only** — see Source Policy.  
5. **Product coverage** — coverage uses product targets, not sprint milestones ([KPI.md](../KPI.md)).

---

## 3. Dataset Quality Requirements

Every published row **must** carry or satisfy the following.

### 3.1 Mandatory fields / attributes

| Requirement | Description | Typical encoding |
|-------------|-------------|------------------|
| **Source** | Trusted source id, name, and/or official URL | Data Sources, Notes, companion metadata |
| **Published Date** | When the source material was published (if known) | Notes / document metadata |
| **Retrieved Date** | When the factory acquired the material (ISO) | Notes / learning metadata |
| **Confidence** | Validator score 0–1 | Notes (`confidence=0.xx`) |
| **Freshness** | Row age vs product freshness window | Last Updated + KPI freshness |
| **Version** | Knowledge / extraction / dataset version | Notes or release train |
| **Validation Status** | Pass before publish | Validator result |
| **Schema Completeness** | Required columns filled | Completeness check |
| **Duplicate Check** | No exact entity-id collision; aliases merged | Duplicate policy |

### 3.2 Batch quality gates

A batch may not advance to **Release** if any of the following fail for the mission’s primary dataset:

- Schema validation fails on appended rows  
- Confidence below reject threshold remains in the published batch  
- Exact duplicate entity IDs introduced  
- Forbidden sources detected  
- Placeholder / fake URLs (`example.com`, `example.invalid`, localhost) present  
- Coverage does not increase (or is explained only by rejected-only runs — not DONE)

### 3.3 Placeholders

Header-only or empty domain files may exist as schema placeholders.  
They are **not** production knowledge. Production missions must populate real rows, not invent placeholders as verified data.

---

## 4. Source Policy

### 4.1 Allowed sources

| Category | Examples |
|----------|----------|
| **Government** | BPS, BKPM, Kemnaker, Kemenperin, OSS, LKPP, OJK, ministries, official regulators |
| **International organizations** | World Bank, OECD, IFC, ADB, UN agencies |
| **Official company publications** | Annual reports, sustainability reports, official product pages, filings |
| **Industry associations** | APINDO, KADIN, sector associations |
| **Official statistics** | National and international statistical releases |

Registry and runtime config:

- `metadata/source_registry.csv`  
- `automation/config/sources.yaml`  
- [SOURCE_POLICY.md](../SOURCE_POLICY.md)

### 4.2 Forbidden sources

| Forbidden | Rationale |
|-----------|-----------|
| **AI-generated content** as primary fact source | Circular / unverifiable provenance |
| **Random blogs** | Untrusted editorial content |
| **Unknown websites** | Not in registry / unassessed trust |
| **Forums** | Anecdotal, non-authoritative |
| **Unverified documents** | No publisher, date, or institutional authority |

### 4.3 Allow rules (operational)

1. Source must be `status=active` and `allowed=true` when registry-managed.  
2. Trust score must meet configured minimum.  
3. Respect robots.txt and terms of use.  
4. Blocklist: `example.com`, `example.invalid`, localhost, fabricated domains.  
5. Inactive placeholder sources must **never** produce published rows.

---

## 5. Confidence Rules

Confidence is a **0–1** score (or 0–100% equivalent) assigned by validation against source trust and extraction quality.

| Score band | Label | Production action |
|------------|-------|-------------------|
| **0.95 – 1.00** | Verified | Publish preferred |
| **0.90 – 0.95** | High | Publish allowed |
| **0.80 – 0.90** | Medium | Publish only with strong provenance; prefer re-verify |
| **Below 0.80** | Reject | **Do not publish** |

### 5.1 Rules

1. Below **0.80** → **reject** the row for production append.  
2. Medium band rows should not dominate a release without review.  
3. Target average confidence for new batches: **≥ 0.85** (30 days), **≥ 0.88** (12 months) — see [KPI.md](../KPI.md).  
4. Confidence must be recorded on the row (e.g. Notes / Data Sources convention `confidence=0.xx`).

---

## 6. Duplicate Policy

| Rule | Statement |
|------|-----------|
| **Never overwrite** | Do not replace a verified row in place to “update” without audit |
| **Append only** | New knowledge is appended; history is preserved |
| **Merge aliases** | Surface-name variants map to one canonical entity; do not create parallel IDs |
| **Reject duplicates** | Exact entity-id collisions and near-identical canonical names in the same batch are rejected |

### 6.1 Detection order

1. **Exact ID** — same Industry ID / Company ID / Product ID / Pain ID / Solution ID / etc.  
2. **Canonical name** — normalized name match (case, punctuation, legal suffix)  
3. **Alias registry** — known aliases resolve to existing entity  

### 6.2 Outcomes

| Case | Action |
|------|--------|
| Exact ID already exists | Reject new row (or controlled versioned update with audit — never silent overwrite) |
| New alias of existing entity | Record alias; do not create new primary row |
| True new entity | Append with new stable ID |
| Fuzzy conflict uncertain | Hold for review; do not auto-publish |

Target: duplicate rate **≤ 2%** on new batches (90 days), **≤ 1%** (12 months).

---

## 7. Naming Convention

### 7.1 Dataset files

| Rule | Example |
|------|---------|
| Lowercase snake_case filenames | `industry_library.csv` |
| UTF-8, LF line endings | — |
| Domain path | `domains/<domain>/<dataset>.csv` |
| Schema companion | `metadata/schema/<dataset>.md` |

### 7.2 Entity IDs

| Dataset class | ID pattern (stable) | Example |
|---------------|---------------------|---------|
| Industry | `IND-…` | `IND-FIN-001` |
| Company | `COM-…` | `COM-IDX-0001` |
| Product | `PRD-…` | `PRD-…` |
| Service | `SVC-…` | `SVC-…` |
| Pain Point | `PAIN-…` | `PAIN-…` |
| Solution | `SOL-…` | `SOL-…` |
| Framework | `FW-…` | `FW-…` |
| Case Study | `CASE-…` | `CASE-…` |
| Competitor | `CMP-…` | `CMP-…` |
| Opportunity | `OPP-…` | `OPP-…` |
| Signal | `SIG-…` | `SIG-…` |

Rules:

- IDs are **immutable** once published  
- Never reuse an ID for a different entity  
- Prefer append-only numbering  
- Deprecate rather than delete when possible  

### 7.3 Industry normalization

1. Prefer official statistical or regulatory industry labels when available.  
2. One industry = one Industry ID.  
3. Category taxonomy must be consistent with existing Industry Category values unless expanding intentionally.  
4. Names: Title Case, language-stable canonical English (or bilingual fields if schema supports).  
5. Do not invent industries without a trusted source.

### 7.4 Company normalization

1. Canonical name = legal name when known; brand as alias.  
2. Normalize case, punctuation, and legal suffixes (`PT`, `Tbk`, `Ltd`, `Inc`) for matching.  
3. One company = one Company ID.  
4. HQ country, industry link, and official website from official sources only.  
5. Listings / ticker symbols are attributes or aliases — not separate companies.

### 7.5 Product normalization

1. One product SKU / product line concept = one Product ID.  
2. Separate product from **service** and from **solution** (solution may reference products).  
3. Vendor name is not the product name.  
4. Prefer official product catalog names over marketing slogans.  
5. Version/edition may be attributes; do not fork IDs for trivial renames.

### 7.6 Service normalization

1. Service is a deliverable capability (implementation, managed service, advisory), not a physical SKU.  
2. One service offering = one Service ID (or schema-equivalent product_catalog subtype when service_library is not yet separate).  
3. Normalize delivery model language (on-prem, cloud, hybrid) as attributes.  
4. Do not duplicate the same service under multiple brand spellings.  
5. Link to industries / pain points / solutions via IDs when known — do not embed free-form invented links without sources.

### 7.7 General text rules

- Prefer business language over storage jargon  
- One concept per entity row  
- Synonyms map to one canonical class  
- Aliases do not create new entities  

---

## 8. Release Policy

Dataset releases are **versioned**. Platform architecture version (e.g. Factory v2.0) is separate from **dataset content** release trains.

### 8.1 Version scheme

```text
vMAJOR.MINOR

MAJOR — breaking schema migration or factory product line reset  
MINOR — dataset content expansion / quality improvement under frozen schema  
```

### 8.2 Example release train

| Version | Theme |
|---------|--------|
| **v2.1** | Industry expansion |
| **v2.2** | Company expansion |
| **v2.3** | Pain Point expansion |
| **v2.4** | Product / Service expansion |
| **v2.5** | Solution / Framework expansion |

(Exact numbers follow [RELEASE_PLAN.md](../RELEASE_PLAN.md); themes illustrate content focus, not architecture work.)

### 8.3 Release checklist

- [ ] Mission DoD satisfied (Section 10)  
- [ ] Domain CSV append integrity verified  
- [ ] Quality validation report available under `reports/` when produced  
- [ ] Exports updated for the release scope  
- [ ] CHANGELOG / release notes mention dataset classes expanded  
- [ ] Product coverage (not sprint %) recorded  

### 8.4 What is not a release

- Dashboard tweaks  
- Documentation-only commits (unless DPS itself is revised)  
- Failed missions that reject all rows  
- Dry-run / development sessions without publish  

---

## 9. Production Mission KPI Report

Every production mission **must** report the following after completion (in mission report, learning report, or release note):

| KPI | Definition |
|-----|------------|
| **Rows Added** | Count of new rows successfully appended |
| **Rows Rejected** | Count of candidates rejected (confidence, duplicate, source, schema) |
| **Coverage** | `current_rows / product_target` for the primary dataset (see product targets config) |
| **Confidence** | Average confidence of accepted rows |
| **Duplicates** | Duplicate rate for the batch / library check |
| **Freshness** | Share of rows within freshness window |
| **Sources Used** | Distinct trusted sources / source IDs used |
| **Mission Duration** | Start → end elapsed time |

### 9.1 Coverage rule (mandatory)

```text
Coverage = current_rows / product_target

Example: Industry 50 / 250 → 20%
Never use sprint milestones as the denominator.
```

Product targets are configured in `automation/config/product_targets.yaml` and documented in [KPI.md](../KPI.md).

### 9.2 Optional but recommended

- Schema completeness of accepted batch  
- Verified source count  
- Export artifact count generated  

---

## 10. Definition of Done

A production mission is **DONE** only if **all** of the following are true:

| # | Criterion |
|---|-----------|
| 1 | **Rows are appended** to the target domain dataset (append-only) |
| 2 | **Validation passes** for published rows |
| 3 | **Coverage increases** against the product target |
| 4 | **Quality maintained** (confidence, duplicates, freshness, completeness within policy) |
| 5 | **Exports updated** when the release/export step is in scope for the mission |

### 10.1 Not DONE

- Extraction only, no append  
- Append of rejected-quality rows  
- Coverage flat or down without approved exception  
- Silent schema changes  
- Using forbidden sources  
- Overwriting history  
- Dashboard-only activity with no dataset growth  

### 10.2 Sprint DoD vs production DoD

| Layer | Done means |
|-------|------------|
| **Factory sprint** | Improves ≥1 official KPI family without architecture change ([KPI.md](../KPI.md)) |
| **Production mission (this DPS)** | Rows appended + validation + coverage + quality + exports as above |

Both apply when a sprint executes production missions.

---

## 11. Future Compatibility (Export Formats)

Production rules in this standard are **format-agnostic**.

The factory may emit any of the following **without changing** lifecycle, quality, source, confidence, or duplicate rules:

| Format | Role |
|--------|------|
| **CSV** | Canonical domain store under `domains/` |
| **JSON** | Structured packages / HF prep |
| **JSONL** | Line-oriented training corpora |
| **Parquet** | Columnar analytics / training prep |
| **Hugging Face** | Hub-oriented packaging |
| **OpenAI fine-tuning** | Chat/completion JSONL packages |

### 11.1 Principles

1. **CSV (or schema-defined domain file) is the system of record** for knowledge rows.  
2. Exports are **derived** — never invent facts only in export formats.  
3. Export packaging may improve independently; it does **not** relax DPS quality gates.  
4. New export formats require packaging support only — not a rewrite of DPS stages.

See [EXPORT_GUIDE.md](../EXPORT_GUIDE.md).

---

## 12. Production Priority Order (Post-DPS)

After this standard is approved, dataset production priority is:

1. **Service Dataset**  
2. **Product Dataset**  
3. **Company Dataset**  
4. **Pain Point Dataset**  
5. **Solution Dataset**  
6. **Framework Dataset**  

No further platform work unless bugs are found.

Industry Dataset remains under continuous coverage growth toward its **product target** (not sprint target) alongside the ordered expansions above when missions allow.

---

## 13. Governance

| Topic | Rule |
|-------|------|
| Amendments | Version this document; note date and summary of change |
| Conflicts | DPS > informal mission notes > operator preference |
| Schema changes | Forbidden without versioned migration + explicit approval |
| Architecture | Frozen — DPS does not authorize redesign |
| UI / dashboard | Frozen — DPS does not authorize redesign |
| Automation | Observe-only procedure; no new frameworks via DPS |

---

## 14. Quick reference card

```text
TRUSTED SOURCE → EXTRACT → NORMALIZE → VALIDATE (≥0.80) →
MAP SCHEMA → APPEND ONLY → QUALITY GATE → EXPORT → VERSIONED RELEASE

Coverage = rows / product_target
Never overwrite. Reject duplicates. Merge aliases.
Forbidden: AI-as-fact, blogs, forums, unknown sites.
DONE = appended + validated + coverage↑ + quality OK + exports updated
```

---

**End of Dataset Production Standard (DPS) v1.0**
