# Candidate Root Cause

**Generated:** 2026-07-22T10:45:11+00:00
**Session:** `SESSION-20260722-45150D`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000679`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-45150D`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000679': 1, 'duplicate_id:SIG-000676': 1, 'duplicate_id:SIG-000678': 1, 'duplicate_id:SIG-000677': 1, 'duplicate_id:SIG-000675': 1}`
- `candidate CAND-C0D1EB49AEA7 entity_id=SIG-000679 reason=duplicate_id:SIG-000679 conf=0.92`
- `candidate CAND-160C8D564E36 entity_id=SIG-000676 reason=duplicate_id:SIG-000676 conf=0.92`
- `candidate CAND-77B5DDCD57DC entity_id=SIG-000678 reason=duplicate_id:SIG-000678 conf=0.9`
- `candidate CAND-C05900938D52 entity_id=SIG-000677 reason=duplicate_id:SIG-000677 conf=0.88`
- `candidate CAND-0C1DA2019826 entity_id=SIG-000675 reason=duplicate_id:SIG-000675 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C0D1EB49AEA7 | business_signal_library | 0.92 | False | duplicate_id:SIG-000679 | Rejected |
| CAND-160C8D564E36 | business_signal_library | 0.92 | False | duplicate_id:SIG-000676 | Rejected |
| CAND-77B5DDCD57DC | business_signal_library | 0.9 | False | duplicate_id:SIG-000678 | Rejected |
| CAND-C05900938D52 | business_signal_library | 0.88 | False | duplicate_id:SIG-000677 | Rejected |
| CAND-0C1DA2019826 | business_signal_library | 0.9 | False | duplicate_id:SIG-000675 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000679` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
