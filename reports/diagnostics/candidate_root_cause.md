# Candidate Root Cause

**Generated:** 2026-07-29T09:57:10+00:00
**Session:** `SESSION-20260729-0438D8`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001041`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260729-0438D8`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001041': 1, 'duplicate_id:SIG-001040': 1, 'duplicate_id:SIG-001043': 1, 'duplicate_id:SIG-001042': 1, 'duplicate_id:SIG-001044': 1}`
- `candidate CAND-DBBC1273DA3C entity_id=SIG-001041 reason=duplicate_id:SIG-001041 conf=0.92`
- `candidate CAND-DE98E2B7477B entity_id=SIG-001040 reason=duplicate_id:SIG-001040 conf=0.9`
- `candidate CAND-8C8AFE74D583 entity_id=SIG-001043 reason=duplicate_id:SIG-001043 conf=0.9`
- `candidate CAND-BB81CF16C346 entity_id=SIG-001042 reason=duplicate_id:SIG-001042 conf=0.88`
- `candidate CAND-0D82CAECF296 entity_id=SIG-001044 reason=duplicate_id:SIG-001044 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-DBBC1273DA3C | business_signal_library | 0.92 | False | duplicate_id:SIG-001041 | Rejected |
| CAND-DE98E2B7477B | business_signal_library | 0.9 | False | duplicate_id:SIG-001040 | Rejected |
| CAND-8C8AFE74D583 | business_signal_library | 0.9 | False | duplicate_id:SIG-001043 | Rejected |
| CAND-BB81CF16C346 | business_signal_library | 0.88 | False | duplicate_id:SIG-001042 | Rejected |
| CAND-0D82CAECF296 | business_signal_library | 0.92 | False | duplicate_id:SIG-001044 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001041` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
