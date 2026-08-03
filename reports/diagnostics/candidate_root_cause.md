# Candidate Root Cause

**Generated:** 2026-08-03T19:12:06+00:00
**Session:** `SESSION-20260803-8A72CC`

> Diagnostics only. No recommendations. Evidence only.

## Exactly which rule blocked production?

**Primary integrity block reason:** `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001333`

**dry_run publisher gate:** `False`

## How many candidates?

- Total analyzed: **5**
- Integrity blocked: **5**
- Blocked by primary reason: **5**

## What evidence proves it?

- `session_id=SESSION-20260803-8A72CC`
- `dry_run=False`
- `candidates_analyzed=5`
- `integrity_blocked=5`
- `top_family=duplicate_id count=5`
- `family_histogram={'duplicate_id': 5}`
- `reason_histogram={'duplicate_id:SIG-001333': 1, 'duplicate_id:SIG-001330': 1, 'duplicate_id:SIG-001332': 1, 'duplicate_id:SIG-001334': 1, 'duplicate_id:SIG-001331': 1}`
- `candidate CAND-75892FA5CD2A entity_id=SIG-001333 reason=duplicate_id:SIG-001333 conf=0.9`
- `candidate CAND-ACDC2F2B3153 entity_id=SIG-001330 reason=duplicate_id:SIG-001330 conf=0.9`
- `candidate CAND-50871F8DCA02 entity_id=SIG-001332 reason=duplicate_id:SIG-001332 conf=0.88`
- `candidate CAND-7155D3CBF7E3 entity_id=SIG-001334 reason=duplicate_id:SIG-001334 conf=0.92`
- `candidate CAND-89ABFCADDF4B entity_id=SIG-001331 reason=duplicate_id:SIG-001331 conf=0.92`

## Per-candidate integrity reasons

| candidate_id | dataset | confidence | integrity_ok | reason | publish |
| --- | --- | --- | --- | --- | --- |
| CAND-75892FA5CD2A | business_signal_library | 0.9 | False | duplicate_id:SIG-001333 | Rejected |
| CAND-ACDC2F2B3153 | business_signal_library | 0.9 | False | duplicate_id:SIG-001330 | Rejected |
| CAND-50871F8DCA02 | business_signal_library | 0.88 | False | duplicate_id:SIG-001332 | Rejected |
| CAND-7155D3CBF7E3 | business_signal_library | 0.92 | False | duplicate_id:SIG-001334 | Rejected |
| CAND-89ABFCADDF4B | business_signal_library | 0.92 | False | duplicate_id:SIG-001331 | Rejected |

## Could production continue if that rule were satisfied?

If rule/condition `duplicate_id (primary entity id already exists in target CSV) — e.g. duplicate_id:SIG-001333` were satisfied for 5/5 candidate(s), integrity_guard.validate_row would return ok for those candidates (publisher append still gated by session dry_run=False).

No recommendation is made. Statement is conditional evidence only.
