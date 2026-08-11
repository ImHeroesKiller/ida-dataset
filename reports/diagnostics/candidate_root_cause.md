# Candidate Root Cause

**Generated:** 2026-08-11T22:10:26+00:00
**Session:** `SESSION-20260811-08A4C1`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001925`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260811-08A4C1`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001925': 1, 'duplicate_id:SIG-001928': 1, 'duplicate_id:SIG-001926': 1, 'duplicate_id:SIG-001929': 1, 'duplicate_id:SIG-001927': 1}`
- `candidate CAND-AA24EFB54793 entity_id=SIG-001925 reason=duplicate_id:SIG-001925 conf=0.9`
- `candidate CAND-5FBC4BA175E5 entity_id=SIG-001928 reason=duplicate_id:SIG-001928 conf=0.9`
- `candidate CAND-73CD0042554A entity_id=SIG-001926 reason=duplicate_id:SIG-001926 conf=0.92`
- `candidate CAND-90841643451B entity_id=SIG-001929 reason=duplicate_id:SIG-001929 conf=0.92`
- `candidate CAND-A0978E389F13 entity_id=SIG-001927 reason=duplicate_id:SIG-001927 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-AA24EFB54793 | business_signal_library | 0.9 | False | duplicate_id:SIG-001925 | Rejected |
| CAND-5FBC4BA175E5 | business_signal_library | 0.9 | False | duplicate_id:SIG-001928 | Rejected |
| CAND-73CD0042554A | business_signal_library | 0.92 | False | duplicate_id:SIG-001926 | Rejected |
| CAND-90841643451B | business_signal_library | 0.92 | False | duplicate_id:SIG-001929 | Rejected |
| CAND-A0978E389F13 | business_signal_library | 0.88 | False | duplicate_id:SIG-001927 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001925` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
