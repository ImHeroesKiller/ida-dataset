# Candidate Root Cause

**Generated:** 2026-08-03T22:28:56+00:00
**Session:** `SESSION-20260803-36D4B4`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001343`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260803-36D4B4`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001343': 1, 'duplicate_id:SIG-001342': 1, 'duplicate_id:SIG-001341': 1, 'duplicate_id:SIG-001344': 1, 'duplicate_id:SIG-001340': 1}`
- `candidate CAND-86BF7F9CD2E8 entity_id=SIG-001343 reason=duplicate_id:SIG-001343 conf=0.9`
- `candidate CAND-8FFD13D44541 entity_id=SIG-001342 reason=duplicate_id:SIG-001342 conf=0.88`
- `candidate CAND-AF90FC89A96B entity_id=SIG-001341 reason=duplicate_id:SIG-001341 conf=0.92`
- `candidate CAND-F06E61429898 entity_id=SIG-001344 reason=duplicate_id:SIG-001344 conf=0.92`
- `candidate CAND-D1BCA01E04AD entity_id=SIG-001340 reason=duplicate_id:SIG-001340 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-86BF7F9CD2E8 | business_signal_library | 0.9 | False | duplicate_id:SIG-001343 | Rejected |
| CAND-8FFD13D44541 | business_signal_library | 0.88 | False | duplicate_id:SIG-001342 | Rejected |
| CAND-AF90FC89A96B | business_signal_library | 0.92 | False | duplicate_id:SIG-001341 | Rejected |
| CAND-F06E61429898 | business_signal_library | 0.92 | False | duplicate_id:SIG-001344 | Rejected |
| CAND-D1BCA01E04AD | business_signal_library | 0.9 | False | duplicate_id:SIG-001340 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001343` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
