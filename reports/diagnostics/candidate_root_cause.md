# Candidate Root Cause

**Generated:** 2026-07-25T07:43:08+00:00
**Session:** `SESSION-20260725-2CF440`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000821`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-2CF440`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000821': 1, 'duplicate_id:SIG-000823': 1, 'duplicate_id:SIG-000822': 1, 'duplicate_id:SIG-000820': 1, 'duplicate_id:SIG-000824': 1}`
- `candidate CAND-B13060909358 entity_id=SIG-000821 reason=duplicate_id:SIG-000821 conf=0.92`
- `candidate CAND-D7BA3C0C127D entity_id=SIG-000823 reason=duplicate_id:SIG-000823 conf=0.9`
- `candidate CAND-339425DFA9A2 entity_id=SIG-000822 reason=duplicate_id:SIG-000822 conf=0.88`
- `candidate CAND-81E339D36DC3 entity_id=SIG-000820 reason=duplicate_id:SIG-000820 conf=0.9`
- `candidate CAND-C600A656B4C4 entity_id=SIG-000824 reason=duplicate_id:SIG-000824 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-B13060909358 | business_signal_library | 0.92 | False | duplicate_id:SIG-000821 | Rejected |
| CAND-D7BA3C0C127D | business_signal_library | 0.9 | False | duplicate_id:SIG-000823 | Rejected |
| CAND-339425DFA9A2 | business_signal_library | 0.88 | False | duplicate_id:SIG-000822 | Rejected |
| CAND-81E339D36DC3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000820 | Rejected |
| CAND-C600A656B4C4 | business_signal_library | 0.92 | False | duplicate_id:SIG-000824 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000821` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
