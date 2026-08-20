# Candidate Root Cause

**Generated:** 2026-08-20T08:58:31+00:00
**Session:** `SESSION-20260820-D40743`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000769`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-D40743`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000769': 1, 'duplicate_id:SIG-000768': 1, 'duplicate_id:SIG-000767': 1, 'duplicate_id:SIG-000766': 1, 'duplicate_id:SIG-000770': 1}`
- `candidate CAND-503D04E6A0F2 entity_id=SIG-000769 reason=duplicate_id:SIG-000769 conf=0.9`
- `candidate CAND-81D058CE54FE entity_id=SIG-000768 reason=duplicate_id:SIG-000768 conf=0.9`
- `candidate CAND-ACB4D11F2C03 entity_id=SIG-000767 reason=duplicate_id:SIG-000767 conf=0.9`
- `candidate CAND-F2795B4899DB entity_id=SIG-000766 reason=duplicate_id:SIG-000766 conf=0.92`
- `candidate CAND-1AB50A9CD053 entity_id=SIG-000770 reason=duplicate_id:SIG-000770 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-503D04E6A0F2 | business_signal_library | 0.9 | False | duplicate_id:SIG-000769 | Rejected |
| CAND-81D058CE54FE | business_signal_library | 0.9 | False | duplicate_id:SIG-000768 | Rejected |
| CAND-ACB4D11F2C03 | business_signal_library | 0.9 | False | duplicate_id:SIG-000767 | Rejected |
| CAND-F2795B4899DB | business_signal_library | 0.92 | False | duplicate_id:SIG-000766 | Rejected |
| CAND-1AB50A9CD053 | business_signal_library | 0.9 | False | duplicate_id:SIG-000770 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000769` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
