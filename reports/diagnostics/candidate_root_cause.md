# Candidate Root Cause

**Generated:** 2026-08-09T19:54:31+00:00
**Session:** `SESSION-20260809-E3E2B9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001758`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260809-E3E2B9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001758': 1, 'duplicate_id:SIG-001756': 1, 'duplicate_id:SIG-001757': 1, 'duplicate_id:SIG-001759': 1, 'duplicate_id:SIG-001755': 1}`
- `candidate CAND-5DB9B017C53B entity_id=SIG-001758 reason=duplicate_id:SIG-001758 conf=0.9`
- `candidate CAND-9BEFCBCADDEC entity_id=SIG-001756 reason=duplicate_id:SIG-001756 conf=0.92`
- `candidate CAND-2135647006D0 entity_id=SIG-001757 reason=duplicate_id:SIG-001757 conf=0.88`
- `candidate CAND-142B89C6238A entity_id=SIG-001759 reason=duplicate_id:SIG-001759 conf=0.92`
- `candidate CAND-6F3370071C00 entity_id=SIG-001755 reason=duplicate_id:SIG-001755 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5DB9B017C53B | business_signal_library | 0.9 | False | duplicate_id:SIG-001758 | Rejected |
| CAND-9BEFCBCADDEC | business_signal_library | 0.92 | False | duplicate_id:SIG-001756 | Rejected |
| CAND-2135647006D0 | business_signal_library | 0.88 | False | duplicate_id:SIG-001757 | Rejected |
| CAND-142B89C6238A | business_signal_library | 0.92 | False | duplicate_id:SIG-001759 | Rejected |
| CAND-6F3370071C00 | business_signal_library | 0.9 | False | duplicate_id:SIG-001755 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001758` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
