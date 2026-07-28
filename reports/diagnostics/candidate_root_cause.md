# Candidate Root Cause

**Generated:** 2026-07-28T18:33:44+00:00
**Session:** `SESSION-20260728-A30AD2`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001006`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260728-A30AD2`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001006': 1, 'duplicate_id:SIG-001007': 1, 'duplicate_id:SIG-001009': 1, 'duplicate_id:SIG-001005': 1, 'duplicate_id:SIG-001008': 1}`
- `candidate CAND-4E6A69FB0384 entity_id=SIG-001006 reason=duplicate_id:SIG-001006 conf=0.92`
- `candidate CAND-4FF63D2827FE entity_id=SIG-001007 reason=duplicate_id:SIG-001007 conf=0.88`
- `candidate CAND-6DE996B29F40 entity_id=SIG-001009 reason=duplicate_id:SIG-001009 conf=0.92`
- `candidate CAND-C04A93F51C8C entity_id=SIG-001005 reason=duplicate_id:SIG-001005 conf=0.9`
- `candidate CAND-6CB2D4C5245C entity_id=SIG-001008 reason=duplicate_id:SIG-001008 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4E6A69FB0384 | business_signal_library | 0.92 | False | duplicate_id:SIG-001006 | Rejected |
| CAND-4FF63D2827FE | business_signal_library | 0.88 | False | duplicate_id:SIG-001007 | Rejected |
| CAND-6DE996B29F40 | business_signal_library | 0.92 | False | duplicate_id:SIG-001009 | Rejected |
| CAND-C04A93F51C8C | business_signal_library | 0.9 | False | duplicate_id:SIG-001005 | Rejected |
| CAND-6CB2D4C5245C | business_signal_library | 0.9 | False | duplicate_id:SIG-001008 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001006` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
