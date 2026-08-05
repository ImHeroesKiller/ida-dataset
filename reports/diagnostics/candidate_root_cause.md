# Candidate Root Cause

**Generated:** 2026-08-05T18:00:44+00:00
**Session:** `SESSION-20260805-250009`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001432`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260805-250009`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001432': 1, 'duplicate_id:SIG-001433': 1, 'duplicate_id:SIG-001430': 1, 'duplicate_id:SIG-001434': 1, 'duplicate_id:SIG-001431': 1}`
- `candidate CAND-58907B298F2A entity_id=SIG-001432 reason=duplicate_id:SIG-001432 conf=0.88`
- `candidate CAND-82F5AD3EFADC entity_id=SIG-001433 reason=duplicate_id:SIG-001433 conf=0.9`
- `candidate CAND-B9FC6A0B4D63 entity_id=SIG-001430 reason=duplicate_id:SIG-001430 conf=0.9`
- `candidate CAND-B4EEC47BF780 entity_id=SIG-001434 reason=duplicate_id:SIG-001434 conf=0.92`
- `candidate CAND-10D4A32984F4 entity_id=SIG-001431 reason=duplicate_id:SIG-001431 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-58907B298F2A | business_signal_library | 0.88 | False | duplicate_id:SIG-001432 | Rejected |
| CAND-82F5AD3EFADC | business_signal_library | 0.9 | False | duplicate_id:SIG-001433 | Rejected |
| CAND-B9FC6A0B4D63 | business_signal_library | 0.9 | False | duplicate_id:SIG-001430 | Rejected |
| CAND-B4EEC47BF780 | business_signal_library | 0.92 | False | duplicate_id:SIG-001434 | Rejected |
| CAND-10D4A32984F4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001431 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001432` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
