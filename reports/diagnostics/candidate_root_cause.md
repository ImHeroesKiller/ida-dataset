# Candidate Root Cause

**Generated:** 2026-08-12T21:05:20+00:00
**Session:** `SESSION-20260812-B48744`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-002002`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260812-B48744`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-002002': 1, 'duplicate_id:SIG-002001': 1, 'duplicate_id:SIG-002003': 1, 'duplicate_id:SIG-002004': 1, 'duplicate_id:SIG-002000': 1}`
- `candidate CAND-5A918C6A9299 entity_id=SIG-002002 reason=duplicate_id:SIG-002002 conf=0.88`
- `candidate CAND-B040608D017A entity_id=SIG-002001 reason=duplicate_id:SIG-002001 conf=0.92`
- `candidate CAND-B6424A3DF845 entity_id=SIG-002003 reason=duplicate_id:SIG-002003 conf=0.9`
- `candidate CAND-037741AC48DC entity_id=SIG-002004 reason=duplicate_id:SIG-002004 conf=0.92`
- `candidate CAND-B9F344241504 entity_id=SIG-002000 reason=duplicate_id:SIG-002000 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-5A918C6A9299 | business_signal_library | 0.88 | False | duplicate_id:SIG-002002 | Rejected |
| CAND-B040608D017A | business_signal_library | 0.92 | False | duplicate_id:SIG-002001 | Rejected |
| CAND-B6424A3DF845 | business_signal_library | 0.9 | False | duplicate_id:SIG-002003 | Rejected |
| CAND-037741AC48DC | business_signal_library | 0.92 | False | duplicate_id:SIG-002004 | Rejected |
| CAND-B9F344241504 | business_signal_library | 0.9 | False | duplicate_id:SIG-002000 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-002002` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
