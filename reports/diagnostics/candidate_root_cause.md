# Candidate Root Cause

**Generated:** 2026-07-30T18:36:12+00:00
**Session:** `SESSION-20260730-F2FDC7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001116`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-F2FDC7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001116': 1, 'duplicate_id:SIG-001117': 1, 'duplicate_id:SIG-001115': 1, 'duplicate_id:SIG-001119': 1, 'duplicate_id:SIG-001118': 1}`
- `candidate CAND-5C33A46ACEAD entity_id=SIG-001116 reason=duplicate_id:SIG-001116 conf=0.92`
- `candidate CAND-9CFD10887942 entity_id=SIG-001117 reason=duplicate_id:SIG-001117 conf=0.88`
- `candidate CAND-68886E99F14D entity_id=SIG-001115 reason=duplicate_id:SIG-001115 conf=0.9`
- `candidate CAND-A239E3CBCFC4 entity_id=SIG-001119 reason=duplicate_id:SIG-001119 conf=0.92`
- `candidate CAND-9FC13FB2E8EC entity_id=SIG-001118 reason=duplicate_id:SIG-001118 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5C33A46ACEAD | business_signal_library | 0.92 | False | duplicate_id:SIG-001116 | Rejected |
| CAND-9CFD10887942 | business_signal_library | 0.88 | False | duplicate_id:SIG-001117 | Rejected |
| CAND-68886E99F14D | business_signal_library | 0.9 | False | duplicate_id:SIG-001115 | Rejected |
| CAND-A239E3CBCFC4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001119 | Rejected |
| CAND-9FC13FB2E8EC | business_signal_library | 0.9 | False | duplicate_id:SIG-001118 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001116` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
