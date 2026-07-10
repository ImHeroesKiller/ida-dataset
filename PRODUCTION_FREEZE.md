# IDA Dataset Factory v2.0

## Production Freeze Declaration

| Field | Value |
|-------|--------|
| **Version** | 2.0 |
| **Effective Date** | 2026-07-11 |
| **Status** | **ACTIVE** |
| **Repository** | IDA Dataset Factory |
| **Approved by** | Project Owner — Ary Wibowo |

---

# Purpose

IDA Dataset Factory is a production system dedicated to automatically collecting, validating, normalizing, and publishing trusted datasets for future LLM fine-tuning.

The objective of this repository is **NOT** to build an AI model.

The objective is **NOT** to build an AI Agent.

The objective is **NOT** to build a Decision Engine.

This repository is **ONLY** responsible for producing high-quality datasets.

---

# Product Vision

```text
Trusted Sources
      ↓
Knowledge Acquisition
      ↓
Validation
      ↓
Normalization
      ↓
Append-only Dataset
      ↓
Dataset Export
      ↓
Future Fine-Tuning
```

---

# Repository Freeze

The following components are considered production stable.

## Architecture

**Status: FROZEN**

No redesign permitted.

---

## Folder Structure

**Status: FROZEN**

No restructuring.

---

## Queue System

**Status: FROZEN**

Document Queue, Candidate Queue, and Publish Queue must remain compatible.

---

## Mission Engine

**Status: FROZEN**

Mission scheduling, mission dispatch, and mission lifecycle must remain stable.

---

## Acquisition Engine

**Status: FROZEN**

Collectors, downloaders, normalization, extraction, and pipeline must remain compatible.

---

## Connector Framework

**Status: FROZEN**

Connector interface is stable.

Future work **adds connectors only**.

---

## Source Registry

**Status: FROZEN**

New sources are added through **configuration only**.

No engine modification required.

---

## Validation Engine (DPS)

**Status: FROZEN**

[Dataset Production Standard](./docs/DATASET_PRODUCTION_STANDARD.md) is the canonical validation policy.

---

## Dashboard

**Status: FROZEN**

Dashboard evolves only through **additional metrics**.

No redesign.

---

## Export Engine

**Status: FROZEN**

Export formats remain stable.

---

# Allowed Changes

The following commit types are allowed.

## New Connector

```text
feat(connector): add ILO connector
```

---

## Dataset Expansion

```text
feat(dataset): expand Buyer Persona dataset
```

---

## Trusted Source Expansion

```text
feat(source): add UNDP registry
```

---

## Production Bug Fix

```text
fix(factory): resolve duplicate candidate detection
```

---

## Documentation

Production documentation only.

---

# Forbidden Changes

The following are **NOT** allowed:

| Forbidden | Reason |
|-----------|--------|
| Repository restructuring | Frozen layout |
| Architecture redesign | Frozen core |
| Queue redesign | Compatibility contract |
| Schema redesign | Append-only datasets |
| Folder movement | Frozen structure |
| Dashboard rewrite | Metrics-only evolution |
| Mission rewrite | Frozen mission engine |
| Scheduler rewrite | Frozen lifecycle |
| Validation rewrite | DPS is canonical |
| Export rewrite | Stable formats |
| RAG integration | Out of scope |
| Vector database | Out of scope |
| AI Agent | Other repository |
| Decision Engine | Other repository |
| Reasoning engine | Other repository |

These belong in the **IDA Intelligent Decision Automation** repository.

---

# Repository Scope

## IDA Dataset Factory owns

- Trusted Sources  
- Collectors  
- Connectors  
- Document Pipeline  
- Extraction  
- Validation  
- Dataset  
- Export  
- Monitoring  
- Production Reports  

## IDA Dataset Factory does **NOT** own

- LLM inference  
- Decision automation  
- Memory  
- Agent orchestration  
- Planning  
- Reasoning  

---

# Production KPIs

Success is measured by:

- Trusted Sources  
- Documents collected  
- Candidates extracted  
- Dataset rows  
- Dataset quality  
- Freshness  
- Confidence  
- Coverage  
- Duplicate rate  
- Export quality  

**Not** by:

- UI changes  
- New architecture  
- New frameworks  
- More features  

See [KPI.md](./KPI.md) for operational definitions.

---

# Product Lifecycle

Future releases focus **ONLY** on:

1. New trusted connectors  
2. New datasets  
3. Coverage expansion  
4. Quality improvement  
5. Production bug fixes  

**No architectural evolution is planned.**

---

# Governance

Any proposal affecting:

- Architecture  
- Schema  
- Mission Engine  
- Queues  
- Validation  
- Exports  

must be treated as a **new major version proposal**.

**Default decision: REJECT** unless explicitly approved by the Project Owner.

---

# Repository Maturity

| Dimension | Value |
|-----------|--------|
| **Stage** | Production Stable |
| **Status** | Frozen Core |
| **Growth Strategy** | Knowledge Expansion |
| | **Not** Software Expansion |

---

# Related documents

- [VISION.md](./VISION.md) — product vision  
- [ARCHITECTURE.md](./ARCHITECTURE.md) — frozen architecture  
- [docs/DATASET_PRODUCTION_STANDARD.md](./docs/DATASET_PRODUCTION_STANDARD.md) — DPS  
- [SOURCE_POLICY.md](./SOURCE_POLICY.md) — trusted sources  
- [KPI.md](./KPI.md) — factory KPIs  
- [CONTRIBUTING.md](./CONTRIBUTING.md) — contribution rules  

---

**End of Production Freeze Declaration — IDA Dataset Factory v2.0**
