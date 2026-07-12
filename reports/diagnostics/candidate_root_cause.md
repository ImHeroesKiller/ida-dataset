# Candidate Root Cause

**Generated:** 2026-07-12T15:17:23+00:00
**Session:** `SESSION-20260712-9CE858`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000106`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-9CE858`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000106': 1, 'duplicate_id:SIG-000107': 1, 'duplicate_id:SIG-000108': 1, 'duplicate_id:SIG-000109': 1, 'duplicate_id:SIG-000105': 1}`
- `candidate CAND-ADC3EDDC466E entity_id=SIG-000106 reason=duplicate_id:SIG-000106 conf=0.92`
- `candidate CAND-D3B42975D0FF entity_id=SIG-000107 reason=duplicate_id:SIG-000107 conf=0.88`
- `candidate CAND-23A292F64415 entity_id=SIG-000108 reason=duplicate_id:SIG-000108 conf=0.85`
- `candidate CAND-2C377B36CB5C entity_id=SIG-000109 reason=duplicate_id:SIG-000109 conf=0.9`
- `candidate CAND-B7628E118C61 entity_id=SIG-000105 reason=duplicate_id:SIG-000105 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-ADC3EDDC466E | business_signal_library | 0.92 | False | duplicate_id:SIG-000106 | Rejected |
| CAND-D3B42975D0FF | business_signal_library | 0.88 | False | duplicate_id:SIG-000107 | Rejected |
| CAND-23A292F64415 | business_signal_library | 0.85 | False | duplicate_id:SIG-000108 | Rejected |
| CAND-2C377B36CB5C | business_signal_library | 0.9 | False | duplicate_id:SIG-000109 | Rejected |
| CAND-B7628E118C61 | business_signal_library | 0.9 | False | duplicate_id:SIG-000105 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000106` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
