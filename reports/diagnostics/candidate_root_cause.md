# Candidate Root Cause

**Generated:** 2026-07-12T08:46:37+00:00
**Session:** `SESSION-20260712-4A4C95`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000086`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-4A4C95`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000086': 1, 'duplicate_id:SIG-000087': 1, 'duplicate_id:SIG-000088': 1, 'duplicate_id:SIG-000085': 1, 'duplicate_id:SIG-000089': 1}`
- `candidate CAND-0DFF3DDBE9C1 entity_id=SIG-000086 reason=duplicate_id:SIG-000086 conf=0.92`
- `candidate CAND-4F35253493A0 entity_id=SIG-000087 reason=duplicate_id:SIG-000087 conf=0.88`
- `candidate CAND-1B24B98A32CB entity_id=SIG-000088 reason=duplicate_id:SIG-000088 conf=0.9`
- `candidate CAND-B24E90E98544 entity_id=SIG-000085 reason=duplicate_id:SIG-000085 conf=0.9`
- `candidate CAND-5C2786315F1D entity_id=SIG-000089 reason=duplicate_id:SIG-000089 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0DFF3DDBE9C1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000086 | Rejected |
| CAND-4F35253493A0 | business_signal_library | 0.88 | False | duplicate_id:SIG-000087 | Rejected |
| CAND-1B24B98A32CB | business_signal_library | 0.9 | False | duplicate_id:SIG-000088 | Rejected |
| CAND-B24E90E98544 | business_signal_library | 0.9 | False | duplicate_id:SIG-000085 | Rejected |
| CAND-5C2786315F1D | business_signal_library | 0.92 | False | duplicate_id:SIG-000089 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000086` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
