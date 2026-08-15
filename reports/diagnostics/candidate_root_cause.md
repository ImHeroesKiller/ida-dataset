# Candidate Root Cause

**Generated:** 2026-08-15T08:44:15+00:00
**Session:** `SESSION-20260815-940788`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000205`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260815-940788`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000205': 1, 'duplicate_id:SIG-000202': 1, 'duplicate_id:SIG-000203': 1, 'duplicate_id:SIG-000201': 1, 'duplicate_id:SIG-000204': 1}`
- `candidate CAND-CF7406ECEF9B entity_id=SIG-000205 reason=duplicate_id:SIG-000205 conf=0.9`
- `candidate CAND-91C2FA74A42D entity_id=SIG-000202 reason=duplicate_id:SIG-000202 conf=0.9`
- `candidate CAND-36515859A74A entity_id=SIG-000203 reason=duplicate_id:SIG-000203 conf=0.9`
- `candidate CAND-920CD54B8C9D entity_id=SIG-000201 reason=duplicate_id:SIG-000201 conf=0.92`
- `candidate CAND-286FF35244AD entity_id=SIG-000204 reason=duplicate_id:SIG-000204 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CF7406ECEF9B | business_signal_library | 0.9 | False | duplicate_id:SIG-000205 | Rejected |
| CAND-91C2FA74A42D | business_signal_library | 0.9 | False | duplicate_id:SIG-000202 | Rejected |
| CAND-36515859A74A | business_signal_library | 0.9 | False | duplicate_id:SIG-000203 | Rejected |
| CAND-920CD54B8C9D | business_signal_library | 0.92 | False | duplicate_id:SIG-000201 | Rejected |
| CAND-286FF35244AD | business_signal_library | 0.9 | False | duplicate_id:SIG-000204 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000205` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
