# Candidate Root Cause

**Generated:** 2026-07-28T20:36:19+00:00
**Session:** `SESSION-20260728-05B6DB`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001010`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260728-05B6DB`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001010': 1, 'duplicate_id:SIG-001011': 1, 'duplicate_id:SIG-001013': 1, 'duplicate_id:SIG-001014': 1, 'duplicate_id:SIG-001012': 1}`
- `candidate CAND-048D51C29CD9 entity_id=SIG-001010 reason=duplicate_id:SIG-001010 conf=0.9`
- `candidate CAND-FA1A025AFAF1 entity_id=SIG-001011 reason=duplicate_id:SIG-001011 conf=0.92`
- `candidate CAND-C0AC19FADC9F entity_id=SIG-001013 reason=duplicate_id:SIG-001013 conf=0.9`
- `candidate CAND-A75FD028F7B5 entity_id=SIG-001014 reason=duplicate_id:SIG-001014 conf=0.92`
- `candidate CAND-EC62B0E04A5D entity_id=SIG-001012 reason=duplicate_id:SIG-001012 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-048D51C29CD9 | business_signal_library | 0.9 | False | duplicate_id:SIG-001010 | Rejected |
| CAND-FA1A025AFAF1 | business_signal_library | 0.92 | False | duplicate_id:SIG-001011 | Rejected |
| CAND-C0AC19FADC9F | business_signal_library | 0.9 | False | duplicate_id:SIG-001013 | Rejected |
| CAND-A75FD028F7B5 | business_signal_library | 0.92 | False | duplicate_id:SIG-001014 | Rejected |
| CAND-EC62B0E04A5D | business_signal_library | 0.88 | False | duplicate_id:SIG-001012 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001010` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
