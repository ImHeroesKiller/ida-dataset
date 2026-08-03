# Candidate Root Cause

**Generated:** 2026-08-03T03:15:10+00:00
**Session:** `SESSION-20260803-211C6B`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001301`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260803-211C6B`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001301': 1, 'duplicate_id:SIG-001304': 1, 'duplicate_id:SIG-001302': 1, 'duplicate_id:SIG-001303': 1, 'duplicate_id:SIG-001300': 1}`
- `candidate CAND-C553A96A6533 entity_id=SIG-001301 reason=duplicate_id:SIG-001301 conf=0.92`
- `candidate CAND-550CF3D27A30 entity_id=SIG-001304 reason=duplicate_id:SIG-001304 conf=0.92`
- `candidate CAND-12F1677D9158 entity_id=SIG-001302 reason=duplicate_id:SIG-001302 conf=0.88`
- `candidate CAND-0CB0C0132AF0 entity_id=SIG-001303 reason=duplicate_id:SIG-001303 conf=0.9`
- `candidate CAND-041A3ED89B45 entity_id=SIG-001300 reason=duplicate_id:SIG-001300 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C553A96A6533 | business_signal_library | 0.92 | False | duplicate_id:SIG-001301 | Rejected |
| CAND-550CF3D27A30 | business_signal_library | 0.92 | False | duplicate_id:SIG-001304 | Rejected |
| CAND-12F1677D9158 | business_signal_library | 0.88 | False | duplicate_id:SIG-001302 | Rejected |
| CAND-0CB0C0132AF0 | business_signal_library | 0.9 | False | duplicate_id:SIG-001303 | Rejected |
| CAND-041A3ED89B45 | business_signal_library | 0.9 | False | duplicate_id:SIG-001300 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001301` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
