# Candidate Root Cause

**Generated:** 2026-07-12T23:10:05+00:00
**Session:** `SESSION-20260712-75F9FB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000132`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-75F9FB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000132': 1, 'duplicate_id:SIG-000133': 1, 'duplicate_id:SIG-000134': 1, 'duplicate_id:SIG-000131': 1, 'duplicate_id:SIG-000130': 1}`
- `candidate CAND-04491DF02914 entity_id=SIG-000132 reason=duplicate_id:SIG-000132 conf=0.9`
- `candidate CAND-8E5A6A0C789D entity_id=SIG-000133 reason=duplicate_id:SIG-000133 conf=0.92`
- `candidate CAND-474BB1F8935A entity_id=SIG-000134 reason=duplicate_id:SIG-000134 conf=0.85`
- `candidate CAND-289F50BD8B9A entity_id=SIG-000131 reason=duplicate_id:SIG-000131 conf=0.92`
- `candidate CAND-09B740BB67FC entity_id=SIG-000130 reason=duplicate_id:SIG-000130 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-04491DF02914 | business_signal_library | 0.9 | False | duplicate_id:SIG-000132 | Rejected |
| CAND-8E5A6A0C789D | business_signal_library | 0.92 | False | duplicate_id:SIG-000133 | Rejected |
| CAND-474BB1F8935A | business_signal_library | 0.85 | False | duplicate_id:SIG-000134 | Rejected |
| CAND-289F50BD8B9A | business_signal_library | 0.92 | False | duplicate_id:SIG-000131 | Rejected |
| CAND-09B740BB67FC | business_signal_library | 0.9 | False | duplicate_id:SIG-000130 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000132` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
