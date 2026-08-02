# Candidate Root Cause

**Generated:** 2026-08-02T08:52:04+00:00
**Session:** `SESSION-20260802-CA4712`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001250`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260802-CA4712`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001250': 1, 'duplicate_id:SIG-001254': 1, 'duplicate_id:SIG-001251': 1, 'duplicate_id:SIG-001252': 1, 'duplicate_id:SIG-001253': 1}`
- `candidate CAND-E5FC34EE486D entity_id=SIG-001250 reason=duplicate_id:SIG-001250 conf=0.9`
- `candidate CAND-FB42C65071F6 entity_id=SIG-001254 reason=duplicate_id:SIG-001254 conf=0.92`
- `candidate CAND-6E936F6EF074 entity_id=SIG-001251 reason=duplicate_id:SIG-001251 conf=0.92`
- `candidate CAND-B500BD04580E entity_id=SIG-001252 reason=duplicate_id:SIG-001252 conf=0.88`
- `candidate CAND-D2AFCC834993 entity_id=SIG-001253 reason=duplicate_id:SIG-001253 conf=0.9`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-E5FC34EE486D | business_signal_library | 0.9 | False | duplicate_id:SIG-001250 | Rejected |
| CAND-FB42C65071F6 | business_signal_library | 0.92 | False | duplicate_id:SIG-001254 | Rejected |
| CAND-6E936F6EF074 | business_signal_library | 0.92 | False | duplicate_id:SIG-001251 | Rejected |
| CAND-B500BD04580E | business_signal_library | 0.88 | False | duplicate_id:SIG-001252 | Rejected |
| CAND-D2AFCC834993 | business_signal_library | 0.9 | False | duplicate_id:SIG-001253 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001250` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
