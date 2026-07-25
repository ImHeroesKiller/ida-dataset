# Candidate Root Cause

**Generated:** 2026-07-25T15:23:04+00:00
**Session:** `SESSION-20260725-C12F69`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000845`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-C12F69`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000845': 1, 'duplicate_id:SIG-000849': 1, 'duplicate_id:SIG-000846': 1, 'duplicate_id:SIG-000848': 1, 'duplicate_id:SIG-000847': 1}`
- `candidate CAND-0EA64FEDB179 entity_id=SIG-000845 reason=duplicate_id:SIG-000845 conf=0.9`
- `candidate CAND-B2E5924C2CFE entity_id=SIG-000849 reason=duplicate_id:SIG-000849 conf=0.92`
- `candidate CAND-98D90CC250BA entity_id=SIG-000846 reason=duplicate_id:SIG-000846 conf=0.92`
- `candidate CAND-5EBC5E009E8B entity_id=SIG-000848 reason=duplicate_id:SIG-000848 conf=0.9`
- `candidate CAND-D06F270EA1DE entity_id=SIG-000847 reason=duplicate_id:SIG-000847 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-0EA64FEDB179 | business_signal_library | 0.9 | False | duplicate_id:SIG-000845 | Rejected |
| CAND-B2E5924C2CFE | business_signal_library | 0.92 | False | duplicate_id:SIG-000849 | Rejected |
| CAND-98D90CC250BA | business_signal_library | 0.92 | False | duplicate_id:SIG-000846 | Rejected |
| CAND-5EBC5E009E8B | business_signal_library | 0.9 | False | duplicate_id:SIG-000848 | Rejected |
| CAND-D06F270EA1DE | business_signal_library | 0.88 | False | duplicate_id:SIG-000847 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000845` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
