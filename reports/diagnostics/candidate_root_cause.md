# Candidate Root Cause

**Generated:** 2026-08-12T05:07:55+00:00
**Session:** `SESSION-20260812-C5FB00`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001946`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-C5FB00`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001946': 1, 'duplicate_id:SIG-001945': 1, 'duplicate_id:SIG-001949': 1, 'duplicate_id:SIG-001948': 1, 'duplicate_id:SIG-001947': 1}`
- `candidate CAND-240682538B19 entity_id=SIG-001946 reason=duplicate_id:SIG-001946 conf=0.92`
- `candidate CAND-3FAE1DF83DA2 entity_id=SIG-001945 reason=duplicate_id:SIG-001945 conf=0.9`
- `candidate CAND-7155E6FE26AC entity_id=SIG-001949 reason=duplicate_id:SIG-001949 conf=0.92`
- `candidate CAND-257E51F49F03 entity_id=SIG-001948 reason=duplicate_id:SIG-001948 conf=0.9`
- `candidate CAND-B4FC156E9B91 entity_id=SIG-001947 reason=duplicate_id:SIG-001947 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-240682538B19 | business_signal_library | 0.92 | False | duplicate_id:SIG-001946 | Rejected |
| CAND-3FAE1DF83DA2 | business_signal_library | 0.9 | False | duplicate_id:SIG-001945 | Rejected |
| CAND-7155E6FE26AC | business_signal_library | 0.92 | False | duplicate_id:SIG-001949 | Rejected |
| CAND-257E51F49F03 | business_signal_library | 0.9 | False | duplicate_id:SIG-001948 | Rejected |
| CAND-B4FC156E9B91 | business_signal_library | 0.88 | False | duplicate_id:SIG-001947 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001946` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
