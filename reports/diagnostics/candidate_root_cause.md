# Candidate Root Cause

**Generated:** 2026-07-30T20:38:59+00:00
**Session:** `SESSION-20260730-6FB524`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001124`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260730-6FB524`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001124': 1, 'duplicate_id:SIG-001122': 1, 'duplicate_id:SIG-001121': 1, 'duplicate_id:SIG-001120': 1, 'duplicate_id:SIG-001123': 1}`
- `candidate CAND-A003B35D3688 entity_id=SIG-001124 reason=duplicate_id:SIG-001124 conf=0.92`
- `candidate CAND-E96BC34795A0 entity_id=SIG-001122 reason=duplicate_id:SIG-001122 conf=0.88`
- `candidate CAND-19EBFE6EF58B entity_id=SIG-001121 reason=duplicate_id:SIG-001121 conf=0.92`
- `candidate CAND-F2450D150040 entity_id=SIG-001120 reason=duplicate_id:SIG-001120 conf=0.9`
- `candidate CAND-41675BE1C54E entity_id=SIG-001123 reason=duplicate_id:SIG-001123 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-A003B35D3688 | business_signal_library | 0.92 | False | duplicate_id:SIG-001124 | Rejected |
| CAND-E96BC34795A0 | business_signal_library | 0.88 | False | duplicate_id:SIG-001122 | Rejected |
| CAND-19EBFE6EF58B | business_signal_library | 0.92 | False | duplicate_id:SIG-001121 | Rejected |
| CAND-F2450D150040 | business_signal_library | 0.9 | False | duplicate_id:SIG-001120 | Rejected |
| CAND-41675BE1C54E | business_signal_library | 0.9 | False | duplicate_id:SIG-001123 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001124` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
