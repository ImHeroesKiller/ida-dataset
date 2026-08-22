# Candidate Root Cause

**Generated:** 2026-08-22T11:40:03+00:00
**Session:** `SESSION-20260822-4C4D6E`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001008`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260822-4C4D6E`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001008': 1, 'duplicate_id:SIG-001007': 1, 'duplicate_id:SIG-001009': 1, 'duplicate_id:SIG-001010': 1, 'duplicate_id:SIG-001006': 1}`
- `candidate CAND-E508054C50BD entity_id=SIG-001008 reason=duplicate_id:SIG-001008 conf=0.9`
- `candidate CAND-9200EC674BED entity_id=SIG-001007 reason=duplicate_id:SIG-001007 conf=0.9`
- `candidate CAND-858AC072243D entity_id=SIG-001009 reason=duplicate_id:SIG-001009 conf=0.9`
- `candidate CAND-C5A719B9C5EE entity_id=SIG-001010 reason=duplicate_id:SIG-001010 conf=0.9`
- `candidate CAND-BEF4247521D4 entity_id=SIG-001006 reason=duplicate_id:SIG-001006 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E508054C50BD | business_signal_library | 0.9 | False | duplicate_id:SIG-001008 | Rejected |
| CAND-9200EC674BED | business_signal_library | 0.9 | False | duplicate_id:SIG-001007 | Rejected |
| CAND-858AC072243D | business_signal_library | 0.9 | False | duplicate_id:SIG-001009 | Rejected |
| CAND-C5A719B9C5EE | business_signal_library | 0.9 | False | duplicate_id:SIG-001010 | Rejected |
| CAND-BEF4247521D4 | business_signal_library | 0.92 | False | duplicate_id:SIG-001006 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001008` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
