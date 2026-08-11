# Candidate Root Cause

**Generated:** 2026-08-11T10:23:49+00:00
**Session:** `SESSION-20260811-078099`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001886`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-078099`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001886': 1, 'duplicate_id:SIG-001887': 1, 'duplicate_id:SIG-001888': 1, 'duplicate_id:SIG-001885': 1, 'duplicate_id:SIG-001889': 1}`
- `candidate CAND-AA448FCF3FD0 entity_id=SIG-001886 reason=duplicate_id:SIG-001886 conf=0.92`
- `candidate CAND-EA280E50B576 entity_id=SIG-001887 reason=duplicate_id:SIG-001887 conf=0.88`
- `candidate CAND-094F9D70A2AC entity_id=SIG-001888 reason=duplicate_id:SIG-001888 conf=0.9`
- `candidate CAND-24F3EBEECD76 entity_id=SIG-001885 reason=duplicate_id:SIG-001885 conf=0.9`
- `candidate CAND-3332DEE4117C entity_id=SIG-001889 reason=duplicate_id:SIG-001889 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AA448FCF3FD0 | business_signal_library | 0.92 | False | duplicate_id:SIG-001886 | Rejected |
| CAND-EA280E50B576 | business_signal_library | 0.88 | False | duplicate_id:SIG-001887 | Rejected |
| CAND-094F9D70A2AC | business_signal_library | 0.9 | False | duplicate_id:SIG-001888 | Rejected |
| CAND-24F3EBEECD76 | business_signal_library | 0.9 | False | duplicate_id:SIG-001885 | Rejected |
| CAND-3332DEE4117C | business_signal_library | 0.92 | False | duplicate_id:SIG-001889 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001886` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
