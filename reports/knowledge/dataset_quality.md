# Dataset Quality Engine

**Sprint:** Dataset Quality + Knowledge Graph Manufacturing  
**Commit series:** additive foundation  
**Status:** Implemented (engine) — pipeline wiring deferred to next commits  
**Date:** 2026-07-12

## Problem

Production rows often ship with empty business fields. Completeness is not scored, so incomplete knowledge can reach publish.

## Solution (additive)

`automation/knowledge/quality.py` scores each candidate **before** publish:

| Score | Meaning |
|-------|---------|
| **completeness** | filled scored fields / total scored fields (0–1) |
| **confidence** | from provenance (existing) |
| **enrichment_status** | `complete` \| `needs_enrichment` \| … |
| **validation_status** | `pass` \| `fail_mandatory` \| `fail_completeness` \| `fail_confidence` |
| **disposition** | `publish` \| `enrichment_queue` \| `reject` |

Quality metadata is stored on `CandidateRecord.metadata["quality"]` — **not** as new CSV columns.

## Completeness example

Company row:

| Field | Present |
|-------|---------|
| Company Name | ✓ |
| Industry | ✓ |
| Website | ✗ |
| Email | ✗ |
| Phone | ✗ |
| Address / HQ | ✓ |

Completeness depends on the full scored header set for `company_profile`.  
Mandatory subset (Name, Industry, Country) gates enrichment vs publish.

## Config

`automation/config/knowledge_quality.yaml`

```yaml
thresholds:
  min_completeness_to_publish: 0.70
  min_confidence_to_publish: 0.80
```

## API

```python
from automation.knowledge import assess_row, may_publish_directly

qa = assess_row(
    "company_profile",
    {"Company Name": "Acme", "Industry": "Banking", "Country": "Indonesia"},
    confidence=0.9,
)
assert may_publish_directly(qa)  # mandatory filled + thresholds
```

## Compatibility

| Frozen surface | Impact |
|----------------|--------|
| CSV schema | None |
| Dataset IDs | Unchanged |
| Pipeline stages | Not modified in this commit |
| Publish queue | Unchanged (enrichment routing next) |
| Scheduler / Mission / UI | Unchanged |

## Next commits

1. Wire disposition → enrichment queue  
2. Enrichment engine  
3. Knowledge atoms + multi-entity manufacturing  
