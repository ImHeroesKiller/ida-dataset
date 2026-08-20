# Candidate Root Cause

**Generated:** 2026-08-20T01:37:14+00:00
**Session:** `SESSION-20260820-413D79`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000734`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-413D79`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000734': 1, 'duplicate_id:SIG-000735': 1, 'duplicate_id:SIG-000732': 1, 'duplicate_id:SIG-000731': 1, 'duplicate_id:SIG-000733': 1}`
- `candidate CAND-80F4B972DE28 entity_id=SIG-000734 reason=duplicate_id:SIG-000734 conf=0.9`
- `candidate CAND-8BAA5806870F entity_id=SIG-000735 reason=duplicate_id:SIG-000735 conf=0.9`
- `candidate CAND-12EB7EDBD892 entity_id=SIG-000732 reason=duplicate_id:SIG-000732 conf=0.9`
- `candidate CAND-3B1E3EC10F79 entity_id=SIG-000731 reason=duplicate_id:SIG-000731 conf=0.92`
- `candidate CAND-60A5252A5842 entity_id=SIG-000733 reason=duplicate_id:SIG-000733 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-80F4B972DE28 | business_signal_library | 0.9 | False | duplicate_id:SIG-000734 | Rejected |
| CAND-8BAA5806870F | business_signal_library | 0.9 | False | duplicate_id:SIG-000735 | Rejected |
| CAND-12EB7EDBD892 | business_signal_library | 0.9 | False | duplicate_id:SIG-000732 | Rejected |
| CAND-3B1E3EC10F79 | business_signal_library | 0.92 | False | duplicate_id:SIG-000731 | Rejected |
| CAND-60A5252A5842 | business_signal_library | 0.9 | False | duplicate_id:SIG-000733 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000734` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
