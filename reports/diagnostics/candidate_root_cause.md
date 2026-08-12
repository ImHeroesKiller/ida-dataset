# Candidate Root Cause

**Generated:** 2026-08-12T23:00:21+00:00
**Session:** `SESSION-20260812-9086C4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-002010`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-9086C4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-002010': 1, 'duplicate_id:SIG-002013': 1, 'duplicate_id:SIG-002011': 1, 'duplicate_id:SIG-002014': 1, 'duplicate_id:SIG-002012': 1}`
- `candidate CAND-DFB3DA251F37 entity_id=SIG-002010 reason=duplicate_id:SIG-002010 conf=0.9`
- `candidate CAND-447664B13EF7 entity_id=SIG-002013 reason=duplicate_id:SIG-002013 conf=0.9`
- `candidate CAND-7B83518F33CF entity_id=SIG-002011 reason=duplicate_id:SIG-002011 conf=0.92`
- `candidate CAND-26E23129CEB8 entity_id=SIG-002014 reason=duplicate_id:SIG-002014 conf=0.92`
- `candidate CAND-7916440FFE47 entity_id=SIG-002012 reason=duplicate_id:SIG-002012 conf=0.88`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DFB3DA251F37 | business_signal_library | 0.9 | False | duplicate_id:SIG-002010 | Rejected |
| CAND-447664B13EF7 | business_signal_library | 0.9 | False | duplicate_id:SIG-002013 | Rejected |
| CAND-7B83518F33CF | business_signal_library | 0.92 | False | duplicate_id:SIG-002011 | Rejected |
| CAND-26E23129CEB8 | business_signal_library | 0.92 | False | duplicate_id:SIG-002014 | Rejected |
| CAND-7916440FFE47 | business_signal_library | 0.88 | False | duplicate_id:SIG-002012 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-002010` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
