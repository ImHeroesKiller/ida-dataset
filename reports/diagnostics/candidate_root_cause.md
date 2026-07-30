# Candidate Root Cause

**Generated:** 2026-07-30T14:23:50+00:00
**Session:** `SESSION-20260730-813756`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001107`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-813756`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001107': 1, 'duplicate_id:SIG-001108': 1, 'duplicate_id:SIG-001105': 1, 'duplicate_id:SIG-001109': 1, 'duplicate_id:SIG-001106': 1}`
- `candidate CAND-7894A05829B2 entity_id=SIG-001107 reason=duplicate_id:SIG-001107 conf=0.88`
- `candidate CAND-6A7B3691C783 entity_id=SIG-001108 reason=duplicate_id:SIG-001108 conf=0.9`
- `candidate CAND-F93A8BDEE66C entity_id=SIG-001105 reason=duplicate_id:SIG-001105 conf=0.9`
- `candidate CAND-2D25536CEF93 entity_id=SIG-001109 reason=duplicate_id:SIG-001109 conf=0.92`
- `candidate CAND-658C1B69699A entity_id=SIG-001106 reason=duplicate_id:SIG-001106 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7894A05829B2 | business_signal_library | 0.88 | False | duplicate_id:SIG-001107 | Rejected |
| CAND-6A7B3691C783 | business_signal_library | 0.9 | False | duplicate_id:SIG-001108 | Rejected |
| CAND-F93A8BDEE66C | business_signal_library | 0.9 | False | duplicate_id:SIG-001105 | Rejected |
| CAND-2D25536CEF93 | business_signal_library | 0.92 | False | duplicate_id:SIG-001109 | Rejected |
| CAND-658C1B69699A | business_signal_library | 0.92 | False | duplicate_id:SIG-001106 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001107` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
