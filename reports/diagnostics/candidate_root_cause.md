# Candidate Root Cause

**Generated:** 2026-08-14T21:40:30+00:00
**Session:** `SESSION-20260814-DF36C9`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000153`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-DF36C9`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000153': 1, 'duplicate_id:SIG-000152': 1, 'duplicate_id:SIG-000154': 1, 'duplicate_id:SIG-000151': 1, 'duplicate_id:SIG-000155': 1}`
- `candidate CAND-ABCE2E52035A entity_id=SIG-000153 reason=duplicate_id:SIG-000153 conf=0.9`
- `candidate CAND-0DCC6D9CC60F entity_id=SIG-000152 reason=duplicate_id:SIG-000152 conf=0.9`
- `candidate CAND-20EF3CC73BD0 entity_id=SIG-000154 reason=duplicate_id:SIG-000154 conf=0.9`
- `candidate CAND-532009F67EB0 entity_id=SIG-000151 reason=duplicate_id:SIG-000151 conf=0.92`
- `candidate CAND-EFEE92F5221C entity_id=SIG-000155 reason=duplicate_id:SIG-000155 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-ABCE2E52035A | business_signal_library | 0.9 | False | duplicate_id:SIG-000153 | Rejected |
| CAND-0DCC6D9CC60F | business_signal_library | 0.9 | False | duplicate_id:SIG-000152 | Rejected |
| CAND-20EF3CC73BD0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000154 | Rejected |
| CAND-532009F67EB0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000151 | Rejected |
| CAND-EFEE92F5221C | business_signal_library | 0.9 | False | duplicate_id:SIG-000155 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000153` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
