# Candidate Root Cause

**Generated:** 2026-07-13T00:20:13+00:00
**Session:** `SESSION-20260712-9090D7`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000137`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260712-9090D7`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000137': 1, 'duplicate_id:SIG-000136': 1, 'duplicate_id:SIG-000135': 1, 'duplicate_id:SIG-000139': 1, 'duplicate_id:SIG-000138': 1}`
- `candidate CAND-79026F4DEF15 entity_id=SIG-000137 reason=duplicate_id:SIG-000137 conf=0.88`
- `candidate CAND-5D081927C7AC entity_id=SIG-000136 reason=duplicate_id:SIG-000136 conf=0.92`
- `candidate CAND-8E54D8037ACD entity_id=SIG-000135 reason=duplicate_id:SIG-000135 conf=0.9`
- `candidate CAND-7ACB9AF0D86A entity_id=SIG-000139 reason=duplicate_id:SIG-000139 conf=0.92`
- `candidate CAND-9CA0C8658FE5 entity_id=SIG-000138 reason=duplicate_id:SIG-000138 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-79026F4DEF15 | business_signal_library | 0.88 | False | duplicate_id:SIG-000137 | Rejected |
| CAND-5D081927C7AC | business_signal_library | 0.92 | False | duplicate_id:SIG-000136 | Rejected |
| CAND-8E54D8037ACD | business_signal_library | 0.9 | False | duplicate_id:SIG-000135 | Rejected |
| CAND-7ACB9AF0D86A | business_signal_library | 0.92 | False | duplicate_id:SIG-000139 | Rejected |
| CAND-9CA0C8658FE5 | business_signal_library | 0.9 | False | duplicate_id:SIG-000138 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000137` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
