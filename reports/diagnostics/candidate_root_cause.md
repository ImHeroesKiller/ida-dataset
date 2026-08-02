# Candidate Root Cause

**Generated:** 2026-08-02T09:27:32+00:00
**Session:** `SESSION-20260802-93EFBE`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001256`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-93EFBE`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001256': 1, 'duplicate_id:SIG-001257': 1, 'duplicate_id:SIG-001259': 1, 'duplicate_id:SIG-001258': 1, 'duplicate_id:SIG-001255': 1}`
- `candidate CAND-C44E37165A26 entity_id=SIG-001256 reason=duplicate_id:SIG-001256 conf=0.92`
- `candidate CAND-1C84122FBFCC entity_id=SIG-001257 reason=duplicate_id:SIG-001257 conf=0.88`
- `candidate CAND-25C72D1B7646 entity_id=SIG-001259 reason=duplicate_id:SIG-001259 conf=0.92`
- `candidate CAND-3D89A83A286B entity_id=SIG-001258 reason=duplicate_id:SIG-001258 conf=0.9`
- `candidate CAND-BFD86ECE21E7 entity_id=SIG-001255 reason=duplicate_id:SIG-001255 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-C44E37165A26 | business_signal_library | 0.92 | False | duplicate_id:SIG-001256 | Rejected |
| CAND-1C84122FBFCC | business_signal_library | 0.88 | False | duplicate_id:SIG-001257 | Rejected |
| CAND-25C72D1B7646 | business_signal_library | 0.92 | False | duplicate_id:SIG-001259 | Rejected |
| CAND-3D89A83A286B | business_signal_library | 0.9 | False | duplicate_id:SIG-001258 | Rejected |
| CAND-BFD86ECE21E7 | business_signal_library | 0.9 | False | duplicate_id:SIG-001255 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001256` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
