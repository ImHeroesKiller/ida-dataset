# Candidate Root Cause

**Generated:** 2026-08-01T23:16:34+00:00
**Session:** `SESSION-20260801-7F0B78`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001236`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260801-7F0B78`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001236': 1, 'duplicate_id:SIG-001239': 1, 'duplicate_id:SIG-001237': 1, 'duplicate_id:SIG-001235': 1, 'duplicate_id:SIG-001238': 1}`
- `candidate CAND-CED1E0520595 entity_id=SIG-001236 reason=duplicate_id:SIG-001236 conf=0.92`
- `candidate CAND-B22A6870DD24 entity_id=SIG-001239 reason=duplicate_id:SIG-001239 conf=0.92`
- `candidate CAND-63A15678FC47 entity_id=SIG-001237 reason=duplicate_id:SIG-001237 conf=0.88`
- `candidate CAND-7971EB637565 entity_id=SIG-001235 reason=duplicate_id:SIG-001235 conf=0.9`
- `candidate CAND-4EBE29601559 entity_id=SIG-001238 reason=duplicate_id:SIG-001238 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-CED1E0520595 | business_signal_library | 0.92 | False | duplicate_id:SIG-001236 | Rejected |
| CAND-B22A6870DD24 | business_signal_library | 0.92 | False | duplicate_id:SIG-001239 | Rejected |
| CAND-63A15678FC47 | business_signal_library | 0.88 | False | duplicate_id:SIG-001237 | Rejected |
| CAND-7971EB637565 | business_signal_library | 0.9 | False | duplicate_id:SIG-001235 | Rejected |
| CAND-4EBE29601559 | business_signal_library | 0.9 | False | duplicate_id:SIG-001238 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001236` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
