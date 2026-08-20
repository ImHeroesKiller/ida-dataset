# Candidate Root Cause

**Generated:** 2026-08-20T20:47:58+00:00
**Session:** `SESSION-20260820-5313C5`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000829`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260820-5313C5`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000829': 1, 'duplicate_id:SIG-000827': 1, 'duplicate_id:SIG-000826': 1, 'duplicate_id:SIG-000830': 1, 'duplicate_id:SIG-000828': 1}`
- `candidate CAND-277328B30819 entity_id=SIG-000829 reason=duplicate_id:SIG-000829 conf=0.9`
- `candidate CAND-42E05710CD15 entity_id=SIG-000827 reason=duplicate_id:SIG-000827 conf=0.9`
- `candidate CAND-D3C9453C2721 entity_id=SIG-000826 reason=duplicate_id:SIG-000826 conf=0.92`
- `candidate CAND-ED6FCA1986E8 entity_id=SIG-000830 reason=duplicate_id:SIG-000830 conf=0.9`
- `candidate CAND-D7AD586C6F41 entity_id=SIG-000828 reason=duplicate_id:SIG-000828 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-277328B30819 | business_signal_library | 0.9 | False | duplicate_id:SIG-000829 | Rejected |
| CAND-42E05710CD15 | business_signal_library | 0.9 | False | duplicate_id:SIG-000827 | Rejected |
| CAND-D3C9453C2721 | business_signal_library | 0.92 | False | duplicate_id:SIG-000826 | Rejected |
| CAND-ED6FCA1986E8 | business_signal_library | 0.9 | False | duplicate_id:SIG-000830 | Rejected |
| CAND-D7AD586C6F41 | business_signal_library | 0.9 | False | duplicate_id:SIG-000828 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000829` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
