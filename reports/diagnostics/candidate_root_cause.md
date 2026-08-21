# Candidate Root Cause

**Generated:** 2026-08-21T10:50:34+00:00
**Session:** `SESSION-20260821-D786DB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000887`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260821-D786DB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000887': 1, 'duplicate_id:SIG-000886': 1, 'duplicate_id:SIG-000890': 1, 'duplicate_id:SIG-000888': 1, 'duplicate_id:SIG-000889': 1}`
- `candidate CAND-3553491B42F0 entity_id=SIG-000887 reason=duplicate_id:SIG-000887 conf=0.9`
- `candidate CAND-C59D310FC1BB entity_id=SIG-000886 reason=duplicate_id:SIG-000886 conf=0.92`
- `candidate CAND-00E4B7F2863E entity_id=SIG-000890 reason=duplicate_id:SIG-000890 conf=0.9`
- `candidate CAND-3F4EBA60C241 entity_id=SIG-000888 reason=duplicate_id:SIG-000888 conf=0.9`
- `candidate CAND-A3DF4C5D5035 entity_id=SIG-000889 reason=duplicate_id:SIG-000889 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3553491B42F0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000887 | Rejected |
| CAND-C59D310FC1BB | business_signal_library | 0.92 | False | duplicate_id:SIG-000886 | Rejected |
| CAND-00E4B7F2863E | business_signal_library | 0.9 | False | duplicate_id:SIG-000890 | Rejected |
| CAND-3F4EBA60C241 | business_signal_library | 0.9 | False | duplicate_id:SIG-000888 | Rejected |
| CAND-A3DF4C5D5035 | business_signal_library | 0.9 | False | duplicate_id:SIG-000889 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000887` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
