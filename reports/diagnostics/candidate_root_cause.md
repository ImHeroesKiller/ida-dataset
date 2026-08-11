# Candidate Root Cause

**Generated:** 2026-08-11T23:02:08+00:00
**Session:** `SESSION-20260811-E82957`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001934`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-E82957`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001934': 1, 'duplicate_id:SIG-001930': 1, 'duplicate_id:SIG-001933': 1, 'duplicate_id:SIG-001932': 1, 'duplicate_id:SIG-001931': 1}`
- `candidate CAND-76091B1B4C72 entity_id=SIG-001934 reason=duplicate_id:SIG-001934 conf=0.92`
- `candidate CAND-3C02F798BC8D entity_id=SIG-001930 reason=duplicate_id:SIG-001930 conf=0.9`
- `candidate CAND-873AA1FE62C2 entity_id=SIG-001933 reason=duplicate_id:SIG-001933 conf=0.9`
- `candidate CAND-2D4B5762723D entity_id=SIG-001932 reason=duplicate_id:SIG-001932 conf=0.88`
- `candidate CAND-E6C1511634E8 entity_id=SIG-001931 reason=duplicate_id:SIG-001931 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-76091B1B4C72 | business_signal_library | 0.92 | False | duplicate_id:SIG-001934 | Rejected |
| CAND-3C02F798BC8D | business_signal_library | 0.9 | False | duplicate_id:SIG-001930 | Rejected |
| CAND-873AA1FE62C2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001933 | Rejected |
| CAND-2D4B5762723D | business_signal_library | 0.88 | False | duplicate_id:SIG-001932 | Rejected |
| CAND-E6C1511634E8 | business_signal_library | 0.92 | False | duplicate_id:SIG-001931 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001934` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
