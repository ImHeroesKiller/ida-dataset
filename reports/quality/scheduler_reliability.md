# Scheduler Reliability Report

**Generated:** 2026-07-10T15:57:32.871218+00:00

---

## P0-4 Dynamic mission selector

Module: `automation/scheduler/mission_selector.py`  
Entry: `automation/ci/learning_session.py` when instruction empty/default or trigger=schedule.

### Selection inputs
1. Lowest product coverage (`rows / product_target`)
2. Highest product priority (batch catalog)
3. Dependency matrix hard deps
4. Trusted source availability (≥6 active preferred)
5. Factory capacity (implicit via gap scoring)
6. Mission queue ranking output

### Hardcoded default removed
learn.yml schedule passes **empty** instruction.  
workflow_dispatch mission default is **empty** (optional override).

### Live selection snapshot

```json
{
  "batch_id": "Batch-009",
  "dataset": "buyer_persona_library",
  "title": "Produce Buyer Persona Dataset",
  "instruction": "Produce Buyer Persona Dataset \u2014 structured buyer personas (Batch-009)",
  "coverage_pct": 0.0,
  "current_rows": 0,
  "product_target": 500,
  "product_priority": 96,
  "score": 1442.0,
  "reason": "lowest_coverage=0.0% \u00b7 priority=96 \u00b7 deps_met \u00b7 sources=13"
}
```

Top ranking:
```json
[
  {
    "batch_id": "Batch-009",
    "dataset": "buyer_persona_library",
    "coverage_pct": 0.0,
    "score": 1442.0
  },
  {
    "batch_id": "Batch-011",
    "dataset": "regulation_library",
    "coverage_pct": 0.0,
    "score": 1226.0
  },
  {
    "batch_id": "Batch-015",
    "dataset": "competitor_library",
    "coverage_pct": 0.0,
    "score": 1190.0
  },
  {
    "batch_id": "Batch-004",
    "dataset": "company_profile",
    "coverage_pct": 0.9,
    "score": 1177.4
  },
  {
    "batch_id": "Batch-005",
    "dataset": "pain_point_library",
    "coverage_pct": 1.9,
    "score": 1164.67
  },
  {
    "batch_id": "Batch-003",
    "dataset": "product_catalog",
    "coverage_pct": 2.5,
    "score": 1163.4
  },
  {
    "batch_id": "Batch-006",
    "dataset": "solution_library",
    "coverage_pct": 1.9,
    "score": 1162.67
  },
  {
    "batch_id": "Batch-002",
    "dataset": "service_library",
    "coverage_pct": 3.2,
    "score": 1157.5
  }
]
```

Industry is **not** forced continuous — only selected when it wins the score.
