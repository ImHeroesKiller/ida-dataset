# Candidate Root Cause

**Generated:** 2026-08-24T11:48:43+00:00
**Session:** `SESSION-20260824-F8D419`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001224`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260824-F8D419`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001224': 1, 'duplicate_id:SIG-001223': 1, 'duplicate_id:SIG-001222': 1, 'duplicate_id:SIG-001225': 1, 'duplicate_id:SIG-001221': 1}`
- `candidate CAND-A94811DF593C entity_id=SIG-001224 reason=duplicate_id:SIG-001224 conf=0.9`
- `candidate CAND-5D9AD1490195 entity_id=SIG-001223 reason=duplicate_id:SIG-001223 conf=0.9`
- `candidate CAND-07E493DA1A2E entity_id=SIG-001222 reason=duplicate_id:SIG-001222 conf=0.9`
- `candidate CAND-82F6DDC2E14E entity_id=SIG-001225 reason=duplicate_id:SIG-001225 conf=0.9`
- `candidate CAND-33345CBE17A3 entity_id=SIG-001221 reason=duplicate_id:SIG-001221 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A94811DF593C | business_signal_library | 0.9 | False | duplicate_id:SIG-001224 | Rejected |
| CAND-5D9AD1490195 | business_signal_library | 0.9 | False | duplicate_id:SIG-001223 | Rejected |
| CAND-07E493DA1A2E | business_signal_library | 0.9 | False | duplicate_id:SIG-001222 | Rejected |
| CAND-82F6DDC2E14E | business_signal_library | 0.9 | False | duplicate_id:SIG-001225 | Rejected |
| CAND-33345CBE17A3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001221 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001224` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
