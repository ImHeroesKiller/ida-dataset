# Candidate Root Cause

**Generated:** 2026-07-25T13:55:36+00:00
**Session:** `SESSION-20260725-125570`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000840`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260725-125570`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000840': 1, 'duplicate_id:SIG-000841': 1, 'duplicate_id:SIG-000842': 1, 'duplicate_id:SIG-000844': 1, 'duplicate_id:SIG-000843': 1}`
- `candidate CAND-4D56DC3DFBE3 entity_id=SIG-000840 reason=duplicate_id:SIG-000840 conf=0.9`
- `candidate CAND-D9D14F3E2961 entity_id=SIG-000841 reason=duplicate_id:SIG-000841 conf=0.92`
- `candidate CAND-E781E7EF8DD3 entity_id=SIG-000842 reason=duplicate_id:SIG-000842 conf=0.88`
- `candidate CAND-8D6E47370BB1 entity_id=SIG-000844 reason=duplicate_id:SIG-000844 conf=0.92`
- `candidate CAND-EB19FCFE2F09 entity_id=SIG-000843 reason=duplicate_id:SIG-000843 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-4D56DC3DFBE3 | business_signal_library | 0.9 | False | duplicate_id:SIG-000840 | Rejected |
| CAND-D9D14F3E2961 | business_signal_library | 0.92 | False | duplicate_id:SIG-000841 | Rejected |
| CAND-E781E7EF8DD3 | business_signal_library | 0.88 | False | duplicate_id:SIG-000842 | Rejected |
| CAND-8D6E47370BB1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000844 | Rejected |
| CAND-EB19FCFE2F09 | business_signal_library | 0.9 | False | duplicate_id:SIG-000843 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000840` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
