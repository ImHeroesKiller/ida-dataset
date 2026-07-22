# Candidate Root Cause

**Generated:** 2026-07-22T15:24:23+00:00
**Session:** `SESSION-20260722-13FCA6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000687`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260722-13FCA6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000687': 1, 'duplicate_id:SIG-000688': 1, 'duplicate_id:SIG-000689': 1, 'duplicate_id:SIG-000686': 1, 'duplicate_id:SIG-000685': 1}`
- `candidate CAND-3B88CBD84BBF entity_id=SIG-000687 reason=duplicate_id:SIG-000687 conf=0.88`
- `candidate CAND-CDE8C4B38806 entity_id=SIG-000688 reason=duplicate_id:SIG-000688 conf=0.9`
- `candidate CAND-C25F60F6A72A entity_id=SIG-000689 reason=duplicate_id:SIG-000689 conf=0.92`
- `candidate CAND-70720EF8A39B entity_id=SIG-000686 reason=duplicate_id:SIG-000686 conf=0.92`
- `candidate CAND-0EA0DC7C6CC0 entity_id=SIG-000685 reason=duplicate_id:SIG-000685 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-3B88CBD84BBF | business_signal_library | 0.88 | False | duplicate_id:SIG-000687 | Rejected |
| CAND-CDE8C4B38806 | business_signal_library | 0.9 | False | duplicate_id:SIG-000688 | Rejected |
| CAND-C25F60F6A72A | business_signal_library | 0.92 | False | duplicate_id:SIG-000689 | Rejected |
| CAND-70720EF8A39B | business_signal_library | 0.92 | False | duplicate_id:SIG-000686 | Rejected |
| CAND-0EA0DC7C6CC0 | business_signal_library | 0.9 | False | duplicate_id:SIG-000685 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000687` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
