# Candidate Root Cause

**Generated:** 2026-08-09T08:16:09+00:00
**Session:** `SESSION-20260809-21FB5D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001696`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-21FB5D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001696': 1, 'duplicate_id:SIG-001695': 1, 'duplicate_id:SIG-001699': 1, 'duplicate_id:SIG-001697': 1, 'duplicate_id:SIG-001698': 1}`
- `candidate CAND-83EE5E8F73B2 entity_id=SIG-001696 reason=duplicate_id:SIG-001696 conf=0.92`
- `candidate CAND-1693000F4C84 entity_id=SIG-001695 reason=duplicate_id:SIG-001695 conf=0.9`
- `candidate CAND-A9B8F7E5C3EF entity_id=SIG-001699 reason=duplicate_id:SIG-001699 conf=0.92`
- `candidate CAND-E26680DDCBBF entity_id=SIG-001697 reason=duplicate_id:SIG-001697 conf=0.88`
- `candidate CAND-8B2BB823BF24 entity_id=SIG-001698 reason=duplicate_id:SIG-001698 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-83EE5E8F73B2 | business_signal_library | 0.92 | False | duplicate_id:SIG-001696 | Rejected |
| CAND-1693000F4C84 | business_signal_library | 0.9 | False | duplicate_id:SIG-001695 | Rejected |
| CAND-A9B8F7E5C3EF | business_signal_library | 0.92 | False | duplicate_id:SIG-001699 | Rejected |
| CAND-E26680DDCBBF | business_signal_library | 0.88 | False | duplicate_id:SIG-001697 | Rejected |
| CAND-8B2BB823BF24 | business_signal_library | 0.9 | False | duplicate_id:SIG-001698 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001696` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
