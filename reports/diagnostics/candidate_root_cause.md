# Candidate Root Cause

**Generated:** 2026-07-21T17:42:05+00:00
**Session:** `SESSION-20260721-771B59`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000638`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260721-771B59`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000638': 1, 'duplicate_id:SIG-000636': 1, 'duplicate_id:SIG-000639': 1, 'duplicate_id:SIG-000635': 1, 'duplicate_id:SIG-000637': 1}`
- `candidate CAND-51E383BC1A5B entity_id=SIG-000638 reason=duplicate_id:SIG-000638 conf=0.9`
- `candidate CAND-60B943872A97 entity_id=SIG-000636 reason=duplicate_id:SIG-000636 conf=0.92`
- `candidate CAND-3E1D825DF7D0 entity_id=SIG-000639 reason=duplicate_id:SIG-000639 conf=0.92`
- `candidate CAND-F7602E0B9057 entity_id=SIG-000635 reason=duplicate_id:SIG-000635 conf=0.9`
- `candidate CAND-9B7A5193E409 entity_id=SIG-000637 reason=duplicate_id:SIG-000637 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-51E383BC1A5B | business_signal_library | 0.9 | False | duplicate_id:SIG-000638 | Rejected |
| CAND-60B943872A97 | business_signal_library | 0.92 | False | duplicate_id:SIG-000636 | Rejected |
| CAND-3E1D825DF7D0 | business_signal_library | 0.92 | False | duplicate_id:SIG-000639 | Rejected |
| CAND-F7602E0B9057 | business_signal_library | 0.9 | False | duplicate_id:SIG-000635 | Rejected |
| CAND-9B7A5193E409 | business_signal_library | 0.88 | False | duplicate_id:SIG-000637 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000638` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
