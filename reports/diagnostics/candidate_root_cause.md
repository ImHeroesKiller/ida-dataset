# Candidate Root Cause

**Generated:** 2026-07-15T08:38:40+00:00
**Session:** `SESSION-20260715-512B85`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000246`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260715-512B85`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000246': 1, 'duplicate_id:SIG-000245': 1, 'duplicate_id:SIG-000248': 1, 'duplicate_id:SIG-000249': 1, 'duplicate_id:SIG-000247': 1}`
- `candidate CAND-C910394F4891 entity_id=SIG-000246 reason=duplicate_id:SIG-000246 conf=0.88`
- `candidate CAND-61DAF7743C34 entity_id=SIG-000245 reason=duplicate_id:SIG-000245 conf=0.9`
- `candidate CAND-CC090052C882 entity_id=SIG-000248 reason=duplicate_id:SIG-000248 conf=0.85`
- `candidate CAND-A14DAF94C302 entity_id=SIG-000249 reason=duplicate_id:SIG-000249 conf=0.9`
- `candidate CAND-41373EEF499D entity_id=SIG-000247 reason=duplicate_id:SIG-000247 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C910394F4891 | business_signal_library | 0.88 | False | duplicate_id:SIG-000246 | Rejected |
| CAND-61DAF7743C34 | business_signal_library | 0.9 | False | duplicate_id:SIG-000245 | Rejected |
| CAND-CC090052C882 | business_signal_library | 0.85 | False | duplicate_id:SIG-000248 | Rejected |
| CAND-A14DAF94C302 | business_signal_library | 0.9 | False | duplicate_id:SIG-000249 | Rejected |
| CAND-41373EEF499D | business_signal_library | 0.92 | False | duplicate_id:SIG-000247 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000246` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
