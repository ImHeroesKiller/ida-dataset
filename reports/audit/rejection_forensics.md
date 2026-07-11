# Rejection Forensics

**Generated:** 2026-07-11T13:39:39+00:00

## Summary

| Metric | Value |
|--------|------:|
| Queue candidates with `rejection_reasons` | 0 / 106 |
| Trace `candidates_rejected` sum | 20 |
| Trace candidates with `reject_reason` field | 0 |

## Explicit rejection_reasons (queue)

| Candidate | Document | Dataset | Confidence | Reason | Evidence |
|-----------|----------|---------|------------|--------|----------|
| — | — | — | — | **no rejection_reasons on queue candidates** | — |

## Trace reject_reason

| Candidate | Document | Reason | Confidence | Dataset |
|-----------|----------|--------|------------|---------|
| — | — | none populated | — | — |

## Integrity / lifecycle (last snapshot)

- **Primary:** duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000026
- **Blocked:** None
- **Total candidates:** 3
- **dry_run blocked:** True

- session_id=SESSION-20260711-6BC023
- dry_run=True
- candidates_analyzed=3
- integrity_blocked=3
- top_family=duplicate_id count=3
- family_histogram={'duplicate_id': 3}
- reason_histogram={'duplicate_id:SIG-000026': 1, 'duplicate_id:SIG-000027': 1, 'duplicate_id:SIG-000025': 1}
- candidate CAND-F04B1DEAECD0 entity_id=SIG-000026 reason=duplicate_id:SIG-000026 conf=0.88
- candidate CAND-D03DE2F0A439 entity_id=SIG-000027 reason=duplicate_id:SIG-000027 conf=0.9
- candidate CAND-7528E4183942 entity_id=SIG-000025 reason=duplicate_id:SIG-000025 conf=0.92

## Checklist coverage

| Dimension | Observed? |
|-----------|-----------|
| Rule triggered | Partial (integrity + rare reject_reason) |
| Confidence | Yes |
| Evidence | Partial |
| Dataset | Yes |
| Duplicate / already exists | Yes (`duplicate_id`) |
| Schema / missing field / low evidence / unsupported relation | Not top measured causes |

## Finding

Validation rejects are **not** the main funnel killer (rejected=20 vs published=110). Late failures are dominated by **duplicate_id integrity** when they occur.
