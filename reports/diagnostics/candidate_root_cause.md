# Candidate Root Cause

**Generated:** 2026-08-22T18:50:47+00:00
**Session:** `SESSION-20260822-C93EAB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001044`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-C93EAB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001044': 1, 'duplicate_id:SIG-001041': 1, 'duplicate_id:SIG-001045': 1, 'duplicate_id:SIG-001043': 1, 'duplicate_id:SIG-001042': 1}`
- `candidate CAND-61E60FA314A1 entity_id=SIG-001044 reason=duplicate_id:SIG-001044 conf=0.9`
- `candidate CAND-0BCEC9B8B565 entity_id=SIG-001041 reason=duplicate_id:SIG-001041 conf=0.92`
- `candidate CAND-4A288341C0B5 entity_id=SIG-001045 reason=duplicate_id:SIG-001045 conf=0.9`
- `candidate CAND-4620DB16AB0B entity_id=SIG-001043 reason=duplicate_id:SIG-001043 conf=0.9`
- `candidate CAND-CD27C1054F2D entity_id=SIG-001042 reason=duplicate_id:SIG-001042 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-61E60FA314A1 | business_signal_library | 0.9 | False | duplicate_id:SIG-001044 | Rejected |
| CAND-0BCEC9B8B565 | business_signal_library | 0.92 | False | duplicate_id:SIG-001041 | Rejected |
| CAND-4A288341C0B5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001045 | Rejected |
| CAND-4620DB16AB0B | business_signal_library | 0.9 | False | duplicate_id:SIG-001043 | Rejected |
| CAND-CD27C1054F2D | business_signal_library | 0.9 | False | duplicate_id:SIG-001042 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001044` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
