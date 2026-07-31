# Candidate Root Cause

**Generated:** 2026-07-31T13:17:01+00:00
**Session:** `SESSION-20260731-9C6E81`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001157`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260731-9C6E81`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001157': 1, 'duplicate_id:SIG-001155': 1, 'duplicate_id:SIG-001156': 1, 'duplicate_id:SIG-001159': 1, 'duplicate_id:SIG-001158': 1}`
- `candidate CAND-7AEDF6E4D134 entity_id=SIG-001157 reason=duplicate_id:SIG-001157 conf=0.88`
- `candidate CAND-D66B8A5FB26C entity_id=SIG-001155 reason=duplicate_id:SIG-001155 conf=0.9`
- `candidate CAND-56324EF8733C entity_id=SIG-001156 reason=duplicate_id:SIG-001156 conf=0.92`
- `candidate CAND-849A12F81C0A entity_id=SIG-001159 reason=duplicate_id:SIG-001159 conf=0.92`
- `candidate CAND-CFD42544C279 entity_id=SIG-001158 reason=duplicate_id:SIG-001158 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-7AEDF6E4D134 | business_signal_library | 0.88 | False | duplicate_id:SIG-001157 | Rejected |
| CAND-D66B8A5FB26C | business_signal_library | 0.9 | False | duplicate_id:SIG-001155 | Rejected |
| CAND-56324EF8733C | business_signal_library | 0.92 | False | duplicate_id:SIG-001156 | Rejected |
| CAND-849A12F81C0A | business_signal_library | 0.92 | False | duplicate_id:SIG-001159 | Rejected |
| CAND-CFD42544C279 | business_signal_library | 0.9 | False | duplicate_id:SIG-001158 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001157` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
