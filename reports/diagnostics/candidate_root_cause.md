# Candidate Root Cause

**Generated:** 2026-08-14T19:09:29+00:00
**Session:** `SESSION-20260814-E4F6B6`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000140`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260814-E4F6B6`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-000140': 1, 'duplicate_id:SIG-000139': 1, 'duplicate_id:SIG-000136': 1, 'duplicate_id:SIG-000138': 1, 'duplicate_id:SIG-000137': 1}`
- `candidate CAND-30F1CEED35B1 entity_id=SIG-000140 reason=duplicate_id:SIG-000140 conf=0.9`
- `candidate CAND-5A08BB854E91 entity_id=SIG-000139 reason=duplicate_id:SIG-000139 conf=0.9`
- `candidate CAND-D470C7E0DCA1 entity_id=SIG-000136 reason=duplicate_id:SIG-000136 conf=0.92`
- `candidate CAND-1575321A7C5C entity_id=SIG-000138 reason=duplicate_id:SIG-000138 conf=0.9`
- `candidate CAND-01F8B6EA46FA entity_id=SIG-000137 reason=duplicate_id:SIG-000137 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-30F1CEED35B1 | business_signal_library | 0.9 | False | duplicate_id:SIG-000140 | Rejected |
| CAND-5A08BB854E91 | business_signal_library | 0.9 | False | duplicate_id:SIG-000139 | Rejected |
| CAND-D470C7E0DCA1 | business_signal_library | 0.92 | False | duplicate_id:SIG-000136 | Rejected |
| CAND-1575321A7C5C | business_signal_library | 0.9 | False | duplicate_id:SIG-000138 | Rejected |
| CAND-01F8B6EA46FA | business_signal_library | 0.9 | False | duplicate_id:SIG-000137 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-000140` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
